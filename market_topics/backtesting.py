from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from .analysis import TopicAnalyzer
from .analysis.validation import daily_market_validation, parse_percent, relation_directional_return
from .collectors import NewsCollector, PricePerformanceCollector
from .collectors.news import load_sample_articles
from .config import (
    DEFAULT_MODEL_WEIGHTS,
    load_company_universe,
    load_model_weights,
    load_sentiment_keywords,
    load_topic_keywords,
    write_model_weights,
)
from .models import Article, Topic


DEFAULT_BACKTEST_DAYS = 5
MIN_BACKTEST_DAYS = 3
MAX_BACKTEST_DAYS = 5
MIN_DAILY_SAMPLES = 3
MIN_DAILY_ARTICLES = 5
MAX_DAILY_WEIGHT_CHANGE = 0.10
WEIGHT_BOUNDS = {
    "news_heat_weight": (0.50, 1.50),
    "current_market_confirmation_weight": (0.00, 1.50),
    "historical_topic_score_weight": (0.00, 1.50),
    "direct_mention_weight": (0.60, 1.30),
    "inferred_supply_chain_weight": (0.20, 1.30),
    "broad_topic_penalty": (0.50, 1.00),
    "price_divergence_penalty": (0.20, 0.80),
}


def run_backtest(
    days: int,
    end_date: date,
    config_dir: Path,
    reports_dir: Path,
    offline_sample: bool = False,
    max_topics: int = 8,
    max_companies: int = 8,
) -> tuple[Path, Path]:
    days = normalize_backtest_days(days)
    output_dir = reports_dir / "backtests"
    news_cache_dir = output_dir / "news-cache"
    output_dir.mkdir(parents=True, exist_ok=True)
    news_cache_dir.mkdir(parents=True, exist_ok=True)
    weights_before = load_model_weights(config_dir)
    daily_results = []
    data_gaps: list[str] = []
    start_date = end_date - timedelta(days=days - 1)

    for offset in range(days):
        current_date = start_date + timedelta(days=offset)
        daily_results.append(
            _backtest_day(
                report_date=current_date,
                config_dir=config_dir,
                weights=weights_before,
                data_gaps=data_gaps,
                offline_sample=offline_sample,
                max_topics=max_topics,
                max_companies=max_companies,
                news_cache_dir=news_cache_dir,
            )
        )

    aggregate = aggregate_backtest(daily_results)
    aggregate["days"] = days
    aggregate["minimum_required_samples"] = minimum_required_samples(days)
    adjustment = adjust_model_weights(weights_before, aggregate)
    if adjustment["updated"]:
        write_model_weights(config_dir, adjustment["weights_after"])
    _append_weight_history(output_dir / "model-weight-history.json", end_date, aggregate, adjustment)

    payload = {
        "date": end_date.isoformat(),
        "days": days,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "aggregate": aggregate,
        "weight_adjustment": adjustment,
        "daily_results": daily_results,
        "data_gaps": sorted(set(data_gaps)),
    }
    json_path = output_dir / f"{end_date.isoformat()}-backtest.json"
    html_path = output_dir / f"{end_date.isoformat()}-backtest.html"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    html_path.write_text(render_backtest_html(payload), encoding="utf-8")
    return json_path, html_path


def aggregate_backtest(daily_results: list[dict[str, Any]]) -> dict[str, Any]:
    valid_days = [item for item in daily_results if not item["low_confidence"]]
    validated_count = sum(int(item["validation"].get("validated_count", 0)) for item in valid_days)
    aligned_count = sum(int(item["validation"].get("aligned_count", 0)) for item in valid_days)
    diverged_count = sum(int(item["validation"].get("diverged_count", 0)) for item in valid_days)
    sample_count_3d = sum(int(item["validation"].get("sample_count_3d", 0)) for item in valid_days)
    sample_count_5d = sum(int(item["validation"].get("sample_count_5d", 0)) for item in valid_days)
    avg_corr_3d = _weighted_average(
        [
            (item["validation"].get("correlation_3d"), int(item["validation"].get("sample_count_3d", 0)))
            for item in valid_days
        ]
    )
    avg_corr_5d = _weighted_average(
        [
            (item["validation"].get("correlation_5d"), int(item["validation"].get("sample_count_5d", 0)))
            for item in valid_days
        ]
    )
    aligned_ratio = aligned_count / validated_count if validated_count else None
    topic_scores = _aggregate_topic_scores(valid_days)
    relation_stats = _aggregate_relation_stats(valid_days)
    keyword_returns = _aggregate_keyword_returns(valid_days)
    return {
        "valid_days": len(valid_days),
        "low_confidence_days": len(daily_results) - len(valid_days),
        "sample_count_3d": sample_count_3d,
        "sample_count_5d": sample_count_5d,
        "validated_count": validated_count,
        "aligned_count": aligned_count,
        "diverged_count": diverged_count,
        "aligned_ratio": _round(aligned_ratio),
        "correlation_3d": _round(avg_corr_3d),
        "correlation_5d": _round(avg_corr_5d),
        "method_quality_score": _round(_method_quality_score(avg_corr_3d, aligned_ratio)),
        "topic_scores": topic_scores,
        "relation_stats": relation_stats,
        "keyword_returns": keyword_returns,
    }


def adjust_model_weights(weights_before: dict[str, float], aggregate: dict[str, Any]) -> dict[str, Any]:
    weights = {key: float(weights_before.get(key, value)) for key, value in DEFAULT_MODEL_WEIGHTS.items()}
    sample_count = int(aggregate.get("sample_count_3d", 0) or 0)
    days = int(aggregate.get("days", DEFAULT_BACKTEST_DAYS) or DEFAULT_BACKTEST_DAYS)
    minimum_samples = int(aggregate.get("minimum_required_samples", minimum_required_samples(days)))
    correlation = aggregate.get("correlation_3d")
    reasons: list[str] = []
    factors = {key: 1.0 for key in weights}

    if sample_count < minimum_samples or correlation is None:
        reasons.append(f"近 {days} 日有效樣本 {sample_count} 未達 {minimum_samples}，不自動調權重。")
        return {
            "updated": False,
            "reason": "；".join(reasons),
            "weights_before": weights,
            "weights_after": weights,
            "changes": {},
        }

    if correlation > 0.20:
        reasons.append(f"近 {days} 日相關性為正，提高市場確認與歷史題材分數權重。")
        factors["current_market_confirmation_weight"] = 1.05
        factors["historical_topic_score_weight"] = 1.05
        factors["direct_mention_weight"] = 1.03
    elif -0.10 <= correlation <= 0.10:
        reasons.append(f"近 {days} 日相關性偏弱，提高價格確認，降低泛題材推估。")
        factors["current_market_confirmation_weight"] = 1.10
        factors["historical_topic_score_weight"] = 1.05
        factors["inferred_supply_chain_weight"] = 0.90
        factors["broad_topic_penalty"] = 0.90
    else:
        reasons.append(f"近 {days} 日方向信心與股價呈負相關，降低推估權重並加重背離扣分。")
        factors["direct_mention_weight"] = 0.95
        factors["inferred_supply_chain_weight"] = 0.90
        factors["broad_topic_penalty"] = 0.90
        factors["price_divergence_penalty"] = 0.90

    weights_after = {key: _bounded_weight(key, value * factors[key]) for key, value in weights.items()}
    if weights_after["inferred_supply_chain_weight"] > weights_after["direct_mention_weight"]:
        weights_after["inferred_supply_chain_weight"] = weights_after["direct_mention_weight"]
        reasons.append("供應鏈推估權重上限套用：不得高於新聞直接提及。")

    changes = {
        key: {"before": round(weights[key], 4), "after": round(weights_after[key], 4)}
        for key in weights
        if round(weights[key], 4) != round(weights_after[key], 4)
    }
    return {
        "updated": bool(changes),
        "reason": "；".join(reasons),
        "weights_before": weights,
        "weights_after": weights_after,
        "changes": changes,
    }


def render_backtest_html(payload: dict[str, Any]) -> str:
    aggregate = payload["aggregate"]
    adjustment = payload["weight_adjustment"]
    days = int(payload.get("days", DEFAULT_BACKTEST_DAYS))
    topic_rows = "\n".join(
        f"<tr><td>{_html(topic)}</td><td>{score:.2f}</td></tr>"
        for topic, score in list(aggregate.get("topic_scores", {}).items())[:12]
    )
    change_rows = "\n".join(
        f"<tr><td>{_html(key)}</td><td>{value['before']}</td><td>{value['after']}</td></tr>"
        for key, value in adjustment.get("changes", {}).items()
    ) or '<tr><td colspan="3">本次未調整</td></tr>'
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>近 {days} 日歷史回測</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans TC',sans-serif;line-height:1.6;margin:24px;color:#1f2937;background:#f8fafc}}
main{{max-width:1080px;margin:0 auto;background:#fff;padding:24px;border:1px solid #e5e7eb;border-radius:8px}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0 20px}}th,td{{border:1px solid #d1d5db;padding:8px;text-align:left}}th{{background:#f3f4f6}}
</style>
</head>
<body><main>
<h1>近 {days} 日歷史回測 - {_html(payload['end_date'])}</h1>
<p>區間：{_html(payload['start_date'])} 至 {_html(payload['end_date'])}</p>
<h2>方法品質</h2>
<ul>
<li>有效天數：{aggregate['valid_days']}，低可信天數：{aggregate['low_confidence_days']}</li>
<li>3日相關：{aggregate['correlation_3d']}，5日相關：{aggregate['correlation_5d']}</li>
<li>同向比例：{aggregate['aligned_ratio']}，樣本：{aggregate['validated_count']}</li>
<li>方法品質分數：{aggregate['method_quality_score']}</li>
</ul>
<h2>權重調整</h2>
<p>{_html(adjustment['reason'])}</p>
<table><tr><th>權重</th><th>調整前</th><th>調整後</th></tr>{change_rows}</table>
<h2>題材市場確認分數</h2>
<table><tr><th>題材</th><th>平均分數</th></tr>{topic_rows}</table>
</main></body></html>"""


def latest_backtest_summary(reports_dir: Path) -> dict[str, Any]:
    history_path = reports_dir / "backtests" / "model-weight-history.json"
    if not history_path.exists():
        return {}
    try:
        payload = json.loads(history_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(payload, list) or not payload:
        return {}
    latest = payload[-1]
    aggregate = latest.get("aggregate", {})
    adjustment = latest.get("weight_adjustment", {})
    return {
        "date": latest.get("date", ""),
        "days": aggregate.get("days", latest.get("days", DEFAULT_BACKTEST_DAYS)),
        "correlation_3d": aggregate.get("correlation_3d"),
        "correlation_5d": aggregate.get("correlation_5d"),
        "aligned_ratio": aggregate.get("aligned_ratio"),
        "validated_count": aggregate.get("validated_count", 0),
        "updated": adjustment.get("updated", False),
        "reason": adjustment.get("reason", ""),
    }


def normalize_backtest_days(days: int) -> int:
    return max(MIN_BACKTEST_DAYS, min(MAX_BACKTEST_DAYS, int(days)))


def minimum_required_samples(days: int) -> int:
    return max(MIN_DAILY_SAMPLES * normalize_backtest_days(days), 9)


def _backtest_day(
    report_date: date,
    config_dir: Path,
    weights: dict[str, float],
    data_gaps: list[str],
    offline_sample: bool,
    max_topics: int,
    max_companies: int,
    news_cache_dir: Path | None = None,
) -> dict[str, Any]:
    companies = load_company_universe(config_dir)
    topic_keywords = load_topic_keywords(config_dir)
    sentiment_keywords = load_sentiment_keywords(config_dir)
    collector = NewsCollector(rss_feeds=[], data_gaps=data_gaps)
    if offline_sample:
        articles = load_sample_articles()
        news_cache_hit = False
    else:
        articles = _load_cached_articles(news_cache_dir, report_date) if news_cache_dir else []
        news_cache_hit = bool(articles)
        if not articles:
            articles = collector.collect_historical(report_date)
            if articles and news_cache_dir:
                _write_cached_articles(news_cache_dir, report_date, articles)
    topics = TopicAnalyzer(
        topic_keywords=topic_keywords,
        companies=companies,
        sentiment_keywords=sentiment_keywords,
        model_weights=weights,
    ).analyze(articles, max_topics=max_topics, max_companies_per_topic=max_companies)
    prices = PricePerformanceCollector(data_gaps=data_gaps, report_date=report_date)
    for topic in topics:
        for relation in topic.related_companies:
            relation.price_performance = prices.collect_for_company(relation.company, relation.impact_direction)
    validation = daily_market_validation(topics)
    low_confidence_reasons = []
    if len(articles) < MIN_DAILY_ARTICLES:
        low_confidence_reasons.append(f"新聞樣本 {len(articles)} 少於 {MIN_DAILY_ARTICLES}")
    if int(validation.get("validated_count", 0) or 0) < MIN_DAILY_SAMPLES:
        low_confidence_reasons.append(f"價格驗證樣本 {validation.get('validated_count', 0)} 少於 {MIN_DAILY_SAMPLES}")
    return {
        "date": report_date.isoformat(),
        "article_count": len(articles),
        "news_cache_hit": news_cache_hit,
        "low_confidence": bool(low_confidence_reasons),
        "low_confidence_reasons": low_confidence_reasons,
        "validation": validation,
        "relation_stats": _relation_stats(topics),
        "keyword_returns": _keyword_returns(topics),
    }


def _append_weight_history(path: Path, end_date: date, aggregate: dict[str, Any], adjustment: dict[str, Any]) -> None:
    history = []
    if path.exists():
        try:
            history = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            history = []
    history = [item for item in history if item.get("date") != end_date.isoformat()]
    history.append(
        {
            "date": end_date.isoformat(),
            "aggregate": aggregate,
            "weight_adjustment": adjustment,
        }
    )
    path.write_text(json.dumps(history[-90:], ensure_ascii=False, indent=2), encoding="utf-8")


def _relation_stats(topics: list[Topic]) -> dict[str, dict[str, int]]:
    stats: dict[str, dict[str, int]] = {}
    for topic in topics:
        for relation in topic.related_companies:
            directional_return = relation_directional_return(relation, "3d")
            if directional_return is None:
                continue
            bucket = stats.setdefault(relation.relation_type, {"validated": 0, "aligned": 0, "diverged": 0})
            bucket["validated"] += 1
            if relation.price_performance.validation == "同向":
                bucket["aligned"] += 1
            elif relation.price_performance.validation == "背離":
                bucket["diverged"] += 1
    return stats


def _keyword_returns(topics: list[Topic]) -> dict[str, list[float]]:
    output: dict[str, list[float]] = {}
    for topic in topics:
        values = [
            value
            for value in (relation_directional_return(relation, "3d") for relation in topic.related_companies)
            if value is not None
        ]
        if values:
            output[topic.name] = values
    return output


def _aggregate_relation_stats(valid_days: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    aggregate: dict[str, dict[str, int]] = {}
    for day in valid_days:
        for relation_type, stats in day.get("relation_stats", {}).items():
            bucket = aggregate.setdefault(relation_type, {"validated": 0, "aligned": 0, "diverged": 0})
            bucket["validated"] += int(stats.get("validated", 0))
            bucket["aligned"] += int(stats.get("aligned", 0))
            bucket["diverged"] += int(stats.get("diverged", 0))
    return {
        key: {
            **value,
            "aligned_ratio": _round(value["aligned"] / value["validated"] if value["validated"] else None),
        }
        for key, value in aggregate.items()
    }


def _load_cached_articles(cache_dir: Path | None, report_date: date) -> list[Article]:
    if cache_dir is None:
        return []
    path = cache_dir / f"{report_date.isoformat()}.json"
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [
        Article(
            title=str(item.get("title", "")),
            url=str(item.get("url", "")),
            source=str(item.get("source", "")),
            published_at=str(item.get("published_at", "")),
            summary=str(item.get("summary", "")),
            language=str(item.get("language", "")),
        )
        for item in payload
        if item.get("title") and item.get("url")
    ]


def _write_cached_articles(cache_dir: Path, report_date: date, articles: list[Article]) -> None:
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"{report_date.isoformat()}.json"
    payload = [
        {
            "title": article.title,
            "url": article.url,
            "source": article.source,
            "published_at": article.published_at,
            "summary": article.summary,
            "language": article.language,
        }
        for article in articles
    ]
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _aggregate_keyword_returns(valid_days: list[dict[str, Any]]) -> dict[str, float]:
    values: dict[str, list[float]] = {}
    for day in valid_days:
        for topic, returns in day.get("keyword_returns", {}).items():
            values.setdefault(topic, []).extend(float(item) for item in returns)
    averaged = {topic: sum(items) / len(items) for topic, items in values.items() if items}
    return dict(sorted(((key, round(value, 4)) for key, value in averaged.items()), key=lambda item: item[1], reverse=True))


def _aggregate_topic_scores(valid_days: list[dict[str, Any]]) -> dict[str, float]:
    scores: dict[str, list[float]] = {}
    for day in valid_days:
        for item in day.get("validation", {}).get("topics", []):
            score = item.get("market_confirmation_score")
            topic = item.get("topic")
            if topic and isinstance(score, (int, float)):
                scores.setdefault(str(topic), []).append(float(score))
    averaged = {topic: sum(items) / len(items) for topic, items in scores.items() if items}
    return dict(sorted(((key, round(value, 4)) for key, value in averaged.items()), key=lambda item: item[1], reverse=True))


def _weighted_average(values: list[tuple[Any, int]]) -> float | None:
    clean = [(float(value), weight) for value, weight in values if isinstance(value, (int, float)) and weight > 0]
    total_weight = sum(weight for _, weight in clean)
    if not clean or total_weight == 0:
        return None
    return sum(value * weight for value, weight in clean) / total_weight


def _method_quality_score(correlation: float | None, aligned_ratio: float | None) -> float | None:
    if correlation is None and aligned_ratio is None:
        return None
    corr_component = 0.0 if correlation is None else max(-1.0, min(1.0, correlation)) * 30.0
    aligned_component = 0.0 if aligned_ratio is None else (aligned_ratio - 0.5) * 40.0
    return max(0.0, min(100.0, 50.0 + corr_component + aligned_component))


def _bounded_weight(key: str, value: float) -> float:
    lower, upper = WEIGHT_BOUNDS[key]
    return round(max(lower, min(upper, value)), 4)


def _round(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 4)


def _html(value: Any) -> str:
    import html

    return html.escape(str(value))
