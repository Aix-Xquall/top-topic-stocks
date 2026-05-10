from __future__ import annotations

import hashlib
import json
import math
import re
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .analysis.validation import direction_sign, parse_percent
from .collectors import NewsCollector, PricePerformanceCollector
from .collectors.news import load_sample_articles
from .analysis import TopicAnalyzer
from .config import load_company_universe, load_model_weights, load_sentiment_keywords, load_topic_keywords
from .models import Article, CompanyRelation, Topic


SAMPLES_FILE = "keyword-company-samples.jsonl"
STATS_FILE = "keyword-company-stats.json"
DEFAULT_SAMPLE_DAYS = 30
DAILY_SAMPLE_REFRESH_DAYS = 10
MIN_REPORT_GROUP_SAMPLES = 5
MIN_LEARNING_SAMPLES = 30
SHRINKAGE_PRIOR = 8


def run_samples(
    days: int,
    end_date: date,
    config_dir: Path,
    reports_dir: Path,
    offline_sample: bool = False,
    max_topics: int = 8,
    max_companies: int = 8,
) -> tuple[Path, Path]:
    output_dir = reports_dir / "backtests"
    news_cache_dir = output_dir / "news-cache"
    output_dir.mkdir(parents=True, exist_ok=True)
    news_cache_dir.mkdir(parents=True, exist_ok=True)

    existing = load_samples(output_dir / SAMPLES_FILE)
    new_samples: list[dict[str, Any]] = []
    data_gaps: list[str] = []
    start_date = end_date - timedelta(days=max(1, days) - 1)
    for offset in range(max(1, days)):
        signal_date = start_date + timedelta(days=offset)
        topics, topic_keywords, article_count = _topics_for_date(
            signal_date=signal_date,
            config_dir=config_dir,
            data_gaps=data_gaps,
            offline_sample=offline_sample,
            max_topics=max_topics,
            max_companies=max_companies,
            news_cache_dir=news_cache_dir,
        )
        new_samples.extend(
            build_keyword_company_samples(
                topics=topics,
                topic_keywords=topic_keywords,
                signal_date=signal_date,
                data_gaps=data_gaps,
                article_count=article_count,
            )
        )

    samples = upsert_samples(existing, new_samples)
    samples_path = output_dir / SAMPLES_FILE
    write_samples(samples_path, samples)
    stats = aggregate_keyword_company_stats(samples, end_date=end_date)
    stats["data_gaps"] = sorted(set(data_gaps))[:50]
    stats_path = output_dir / STATS_FILE
    stats_path.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    return samples_path, stats_path


def build_keyword_company_samples(
    topics: list[Topic],
    topic_keywords: dict[str, list[str]],
    signal_date: date,
    data_gaps: list[str],
    article_count: int | None = None,
) -> list[dict[str, Any]]:
    prices = PricePerformanceCollector(data_gaps=data_gaps, report_date=signal_date)
    rows: list[dict[str, Any]] = []
    for topic in topics:
        for relation in topic.related_companies:
            keywords = relation_keywords(topic, relation, topic_keywords)
            if not keywords:
                keywords = [topic.name]
            source_urls = _source_urls(topic.articles, relation)
            source_domains = _source_domains(source_urls)
            forward = prices.collect_forward_returns(
                relation.company,
                relation.impact_direction,
                signal_date=signal_date,
            )
            for keyword in keywords[:5]:
                row = {
                    "sample_id": sample_id(signal_date, keyword, topic.name, relation),
                    "signal_date": signal_date.isoformat(),
                    "keyword": keyword,
                    "topic": topic.name,
                    "market": relation.company.market,
                    "ticker": relation.company.ticker,
                    "name_zh": relation.company.name_zh,
                    "name_en": relation.company.name_en,
                    "relation_type": relation.relation_type,
                    "impact_direction": relation.impact_direction,
                    "direction_sign": direction_sign(relation.impact_direction),
                    "confidence": round(float(relation.confidence), 4),
                    "topic_heat": int(topic.score),
                    "article_count": article_count,
                    "source_count": len(source_urls),
                    "source_domains": source_domains,
                    "source_urls": source_urls[:5],
                    "forward_return_3d": forward.get("forward_return_3d"),
                    "forward_return_5d": forward.get("forward_return_5d"),
                    "directional_return_3d": _directional_return(forward.get("forward_return_3d"), relation),
                    "directional_return_5d": _directional_return(forward.get("forward_return_5d"), relation),
                    "outcome_status": forward.get("outcome_status", "missing_price"),
                    "price_source": forward.get("source", "N/A"),
                    "base_date": forward.get("base_date", "N/A"),
                    "target_date_3d": forward.get("target_date_3d", "N/A"),
                    "target_date_5d": forward.get("target_date_5d", "N/A"),
                }
                rows.append(row)
    return rows


def sample_id(signal_date: date, keyword: str, topic: str, relation: CompanyRelation) -> str:
    raw = "|".join(
        [
            signal_date.isoformat(),
            keyword.strip().lower(),
            topic.strip().lower(),
            relation.company.market.upper(),
            relation.company.ticker.upper(),
            relation.relation_type.strip().lower(),
        ]
    )
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:20]


def relation_keywords(topic: Topic, relation: CompanyRelation, topic_keywords: dict[str, list[str]]) -> list[str]:
    text = " ".join([topic.name, *(_article_text(article) for article in topic.articles)])
    configured = topic_keywords.get(topic.name, [])
    keywords: list[str] = []
    for keyword in configured:
        if _contains(text, keyword):
            keywords.append(keyword)
    for tag in relation.company.tags:
        if _contains(text, tag):
            keywords.append(tag)
    for alias in [relation.company.ticker, relation.company.name_zh, relation.company.name_en, *relation.company.aliases]:
        if alias and _contains(text, alias):
            keywords.append(alias)
    for term in re.findall(r"\b[A-Z][A-Za-z0-9]{2,12}\b", text):
        if _looks_like_signal_term(term):
            keywords.append(term)
    return _unique([item for item in keywords if item.strip()])[:8]


def load_samples(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(item, dict) and item.get("sample_id"):
            rows.append(item)
    return rows


def write_samples(path: Path, samples: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(samples, key=lambda item: (str(item.get("signal_date", "")), str(item.get("sample_id", ""))))
    text = "\n".join(json.dumps(item, ensure_ascii=False, sort_keys=True) for item in ordered)
    path.write_text(text + ("\n" if text else ""), encoding="utf-8")


def upsert_samples(existing: list[dict[str, Any]], new_samples: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {str(item.get("sample_id")): item for item in existing if item.get("sample_id")}
    for item in new_samples:
        by_id[str(item["sample_id"])] = item
    return list(by_id.values())[-5000:]


def aggregate_keyword_company_stats(samples: list[dict[str, Any]], end_date: date | None = None) -> dict[str, Any]:
    valid = [item for item in samples if item.get("outcome_status") == "valid" and _number(item.get("directional_return_5d")) is not None]
    groups = {
        "keyword": _group_stats(valid, lambda item: str(item.get("keyword", ""))),
        "topic": _group_stats(valid, lambda item: str(item.get("topic", ""))),
        "keyword_ticker": _group_stats(valid, lambda item: f"{item.get('keyword', '')}|{item.get('ticker', '')}"),
        "topic_ticker": _group_stats(valid, lambda item: f"{item.get('topic', '')}|{item.get('ticker', '')}"),
        "relation_type": _group_stats(valid, lambda item: str(item.get("relation_type", ""))),
    }
    top_edges = _top_groups(groups["keyword_ticker"], reverse=True)
    weak_edges = _top_groups(groups["keyword_ticker"], reverse=False)
    return {
        "generated_at": end_date.isoformat() if end_date else "",
        "sample_count": len(samples),
        "valid_sample_count": len(valid),
        "pending_sample_count": sum(1 for item in samples if item.get("outcome_status") == "pending"),
        "missing_price_sample_count": sum(1 for item in samples if item.get("outcome_status") == "missing_price"),
        "neutral_sample_count": sum(1 for item in samples if item.get("outcome_status") == "neutral"),
        "overall": _stats_for_rows(valid),
        "groups": groups,
        "top_keyword_company_edges": top_edges[:12],
        "weak_keyword_company_edges": weak_edges[:12],
    }


def load_keyword_company_stats(reports_dir: Path) -> dict[str, Any]:
    path = reports_dir / "backtests" / STATS_FILE
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def keyword_company_learning_summary(reports_dir: Path) -> dict[str, Any]:
    stats = load_keyword_company_stats(reports_dir)
    if not stats:
        return {}
    overall = stats.get("overall", {}) if isinstance(stats.get("overall"), dict) else {}
    return {
        "sample_count": stats.get("sample_count", 0),
        "valid_sample_count": stats.get("valid_sample_count", 0),
        "pending_sample_count": stats.get("pending_sample_count", 0),
        "hit_rate_5d": overall.get("hit_rate_5d"),
        "confidence_correlation_5d": overall.get("confidence_correlation_5d"),
        "avg_directional_return_5d": overall.get("avg_directional_return_5d"),
        "top_edges": stats.get("top_keyword_company_edges", [])[:5],
        "weak_edges": stats.get("weak_keyword_company_edges", [])[:5],
    }


def historical_edge_for_topic(topic: Topic, stats: dict[str, Any]) -> float | None:
    values: list[tuple[float, int]] = []
    for relation in topic.related_companies:
        edge = historical_edge_for_relation(topic.name, relation, stats)
        if edge is not None:
            values.append((edge, 1))
    if not values:
        return None
    return sum(value for value, _ in values) / len(values)


def historical_edge_for_relation(topic_name: str, relation: CompanyRelation, stats: dict[str, Any]) -> float | None:
    groups = stats.get("groups", {}) if isinstance(stats.get("groups"), dict) else {}
    ticker = relation.company.ticker
    candidates = [
        _group_edge(groups, "topic_ticker", f"{topic_name}|{ticker}"),
        _group_edge(groups, "topic", topic_name),
    ]
    clean = [value for value in candidates if value is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def keyword_learning_adjustment_factor(aggregate: dict[str, Any]) -> float:
    learning = aggregate.get("keyword_company_learning", {})
    if not isinstance(learning, dict):
        return 1.0
    valid_count = int(learning.get("valid_sample_count", 0) or 0)
    if valid_count < MIN_LEARNING_SAMPLES:
        return 1.0
    hit_rate = learning.get("hit_rate_5d")
    correlation = learning.get("confidence_correlation_5d")
    if isinstance(hit_rate, (int, float)) and hit_rate >= 0.58:
        return 1.10
    if isinstance(correlation, (int, float)) and correlation > 0.10:
        return 1.08
    if isinstance(hit_rate, (int, float)) and hit_rate <= 0.42:
        return 0.90
    if isinstance(correlation, (int, float)) and correlation < -0.10:
        return 0.90
    return 1.0


def _topics_for_date(
    signal_date: date,
    config_dir: Path,
    data_gaps: list[str],
    offline_sample: bool,
    max_topics: int,
    max_companies: int,
    news_cache_dir: Path,
) -> tuple[list[Topic], dict[str, list[str]], int]:
    companies = load_company_universe(config_dir)
    topic_keywords = load_topic_keywords(config_dir)
    sentiment_keywords = load_sentiment_keywords(config_dir)
    weights = load_model_weights(config_dir)
    if offline_sample:
        articles = load_sample_articles()
    else:
        articles = _load_or_collect_articles(signal_date, news_cache_dir, data_gaps)
    topics = TopicAnalyzer(
        topic_keywords=topic_keywords,
        companies=companies,
        sentiment_keywords=sentiment_keywords,
        model_weights=weights,
    ).analyze(articles, max_topics=max_topics, max_companies_per_topic=max_companies)
    return topics, topic_keywords, len(articles)


def _load_or_collect_articles(signal_date: date, news_cache_dir: Path, data_gaps: list[str]) -> list[Article]:
    path = news_cache_dir / f"{signal_date.isoformat()}.json"
    if path.exists():
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            payload = []
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
    articles = NewsCollector(rss_feeds=[], data_gaps=data_gaps).collect_historical(signal_date)
    if articles:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(
                [
                    {
                        "title": article.title,
                        "url": article.url,
                        "source": article.source,
                        "published_at": article.published_at,
                        "summary": article.summary,
                        "language": article.language,
                    }
                    for article in articles
                ],
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
    return articles


def _group_stats(valid_rows: list[dict[str, Any]], key_func) -> dict[str, dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in valid_rows:
        key = key_func(item)
        if key.strip():
            buckets[key].append(item)
    return {
        key: stats
        for key, stats in sorted(
            ((key, _stats_for_rows(rows)) for key, rows in buckets.items()),
            key=lambda item: (item[1].get("edge_score_5d") or 0.0, item[1].get("valid_count", 0)),
            reverse=True,
        )
    }


def _stats_for_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    returns_3d = [_number(item.get("directional_return_3d")) for item in rows]
    returns_5d = [_number(item.get("directional_return_5d")) for item in rows]
    returns_3d = [value for value in returns_3d if value is not None]
    returns_5d = [value for value in returns_5d if value is not None]
    valid_count = len(returns_5d)
    wins_5d = sum(1 for value in returns_5d if value > 0)
    hit_rate_5d = wins_5d / valid_count if valid_count else None
    shrunk_hit_rate = ((wins_5d + SHRINKAGE_PRIOR * 0.5) / (valid_count + SHRINKAGE_PRIOR)) if valid_count else None
    avg_5d = _mean(returns_5d)
    edge = _edge_score(avg_5d, shrunk_hit_rate, valid_count)
    pairs = [
        (float(item["confidence"]), float(item["directional_return_5d"]))
        for item in rows
        if _number(item.get("confidence")) is not None and _number(item.get("directional_return_5d")) is not None
    ]
    return {
        "valid_count": valid_count,
        "hit_rate_3d": _round(sum(1 for value in returns_3d if value > 0) / len(returns_3d) if returns_3d else None),
        "hit_rate_5d": _round(hit_rate_5d),
        "shrunk_hit_rate_5d": _round(shrunk_hit_rate),
        "avg_directional_return_3d": _round(_mean(returns_3d)),
        "avg_directional_return_5d": _round(avg_5d),
        "confidence_correlation_5d": _round(_pearson(pairs)),
        "overconfident_miss_rate_5d": _round(_overconfident_miss_rate(rows)),
        "edge_score_5d": _round(edge),
        "last_seen": max((str(item.get("signal_date", "")) for item in rows), default=""),
    }


def _edge_score(avg_return: float | None, hit_rate: float | None, valid_count: int) -> float | None:
    if avg_return is None and hit_rate is None:
        return None
    hit_component = 0.0 if hit_rate is None else (hit_rate - 0.5) * 70.0
    return_component = 0.0 if avg_return is None else max(-8.0, min(8.0, avg_return)) * 2.5
    sample_component = min(8.0, math.log(max(valid_count, 1), 2))
    return max(0.0, min(100.0, 50.0 + hit_component + return_component + sample_component))


def _top_groups(groups: dict[str, dict[str, Any]], reverse: bool) -> list[dict[str, Any]]:
    rows = []
    for key, stats in groups.items():
        if int(stats.get("valid_count", 0) or 0) < MIN_REPORT_GROUP_SAMPLES:
            continue
        rows.append({"key": key, **stats})
    return sorted(rows, key=lambda item: float(item.get("edge_score_5d") or 0.0), reverse=reverse)


def _group_edge(groups: dict[str, Any], group_name: str, key: str) -> float | None:
    bucket = groups.get(group_name, {}) if isinstance(groups.get(group_name), dict) else {}
    stats = bucket.get(key, {}) if isinstance(bucket.get(key), dict) else {}
    if int(stats.get("valid_count", 0) or 0) < MIN_REPORT_GROUP_SAMPLES:
        return None
    value = stats.get("edge_score_5d")
    return float(value) if isinstance(value, (int, float)) else None


def _directional_return(raw_return: Any, relation: CompanyRelation) -> float | None:
    value = _number(raw_return)
    sign = direction_sign(relation.impact_direction)
    if value is None or sign == 0:
        return None
    return round(sign * value, 4)


def _source_urls(articles: list[Article], relation: CompanyRelation) -> list[str]:
    text_terms = [relation.company.ticker, relation.company.name_zh, relation.company.name_en, *relation.company.aliases]
    urls = []
    for article in articles:
        text = _article_text(article)
        if any(term and _contains(text, term) for term in text_terms):
            urls.append(article.url)
    if not urls:
        urls = [article.url for article in articles]
    return _unique([url for url in urls if url])


def _source_domains(urls: list[str]) -> list[str]:
    domains = []
    for url in urls:
        host = urlparse(url).netloc.lower()
        if host.startswith("www."):
            host = host[4:]
        if host:
            domains.append(host)
    return _unique(domains)


def _article_text(article: Article) -> str:
    return f"{article.title} {article.summary}".lower()


def _contains(text: str, keyword: str) -> bool:
    keyword = str(keyword).strip()
    if not keyword:
        return False
    pattern = keyword.lower()
    if re.search(r"[a-zA-Z0-9]", pattern):
        return re.search(rf"\b{re.escape(pattern)}\b", text.lower()) is not None
    return pattern in text.lower()


def _looks_like_signal_term(term: str) -> bool:
    return bool(re.search(r"Co(?:PoS|WoS)|FOPLP|HBM\d*[A-Z]*|GDDR\d+|MI\d+|Rubin|Blackwell", term))


def _unique(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output


def _number(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        return parse_percent(value)
    return None


def _mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def _overconfident_miss_rate(rows: list[dict[str, Any]]) -> float | None:
    high = [
        item
        for item in rows
        if isinstance(item.get("confidence"), (int, float)) and float(item.get("confidence", 0.0)) >= 0.70
    ]
    if not high:
        return None
    misses = sum(1 for item in high if _number(item.get("directional_return_5d")) is not None and float(item["directional_return_5d"]) <= 0)
    return misses / len(high)


def _pearson(pairs: list[tuple[float, float]]) -> float | None:
    if len(pairs) < 3:
        return None
    xs = [item[0] for item in pairs]
    ys = [item[1] for item in pairs]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    denominator_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denominator_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if denominator_x == 0 or denominator_y == 0:
        return None
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in pairs)
    return numerator / (denominator_x * denominator_y)


def _round(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 4)
