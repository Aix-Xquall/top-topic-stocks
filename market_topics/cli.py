from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .analysis import TopicAnalyzer
from .analysis.validation import adjusted_directional_confidence, daily_market_validation
from .backtesting import DEFAULT_BACKTEST_DAYS, latest_backtest_summary, run_backtest
from .collectors import FundamentalsCollector, NewsCollector, PricePerformanceCollector
from .config import (
    load_company_universe,
    load_model_weights,
    load_reference_sources,
    load_rss_feeds,
    load_sentiment_keywords,
    load_topic_keywords,
)
from .models import RunResult
from .notification import notify_from_summary, summary_path_for_date
from .reporting import ReportRenderer


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="market_topics", description="每日股市熱門話題中文分析系統")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="產生每日股市熱門話題報告")
    run_parser.add_argument("--date", dest="report_date", default=date.today().isoformat(), help="報告日期 YYYY-MM-DD")
    run_parser.add_argument("--config-dir", default="config", help="設定檔目錄")
    run_parser.add_argument("--reports-dir", default="reports", help="報告輸出目錄")
    run_parser.add_argument("--offline-sample", action="store_true", help="使用內建樣本新聞，不連線抓取新聞")
    run_parser.add_argument("--max-topics", type=int, default=8, help="最多輸出話題數")
    run_parser.add_argument("--max-companies", type=int, default=8, help="每個話題最多公司數")

    notify_parser = subparsers.add_parser("notify-line", help="透過 LINE Messaging API 推送報告摘要")
    notify_parser.add_argument("--date", dest="report_date", default=date.today().isoformat(), help="報告日期 YYYY-MM-DD")
    notify_parser.add_argument("--reports-dir", default="reports", help="報告輸出目錄")
    notify_parser.add_argument("--report-url", required=True, help="HTML 報告公開網址")

    backtest_parser = subparsers.add_parser("backtest", help="回測近 N 天並自動調整模型權重")
    backtest_parser.add_argument(
        "--days",
        type=int,
        default=DEFAULT_BACKTEST_DAYS,
        help="回測天數，系統會限制在 3 到 5 日",
    )
    backtest_parser.add_argument("--end-date", default=date.today().isoformat(), help="回測結束日期 YYYY-MM-DD")
    backtest_parser.add_argument("--config-dir", default="config", help="設定檔目錄")
    backtest_parser.add_argument("--reports-dir", default="reports", help="報告輸出目錄")
    backtest_parser.add_argument("--offline-sample", action="store_true", help="使用內建樣本新聞測試回測流程")
    backtest_parser.add_argument("--max-topics", type=int, default=8, help="每日最多話題數")
    backtest_parser.add_argument("--max-companies", type=int, default=8, help="每個話題最多公司數")

    args = parser.parse_args(argv)
    if args.command == "run":
        result = run_report(
            report_date=date.fromisoformat(args.report_date),
            config_dir=Path(args.config_dir),
            reports_dir=Path(args.reports_dir),
            offline_sample=args.offline_sample,
            max_topics=args.max_topics,
            max_companies=args.max_companies,
        )
        print(f"已產生中文 Markdown 報告：{result.output_markdown}")
        print(f"已產生中文 HTML 報告：{result.output_html}")
        if result.data_gaps:
            print(f"資料缺口：{len(set(result.data_gaps))} 項，詳見報告末段。")
        return 0
    if args.command == "notify-line":
        summary_path = summary_path_for_date(Path(args.reports_dir), args.report_date)
        status = notify_from_summary(summary_path=summary_path, report_url=args.report_url)
        print(status)
        return 0
    if args.command == "backtest":
        json_path, html_path = run_backtest(
            days=args.days,
            end_date=date.fromisoformat(args.end_date),
            config_dir=Path(args.config_dir),
            reports_dir=Path(args.reports_dir),
            offline_sample=args.offline_sample,
            max_topics=args.max_topics,
            max_companies=args.max_companies,
        )
        print(f"已產生回測 JSON：{json_path}")
        print(f"已產生回測 HTML：{html_path}")
        return 0
    return 1


def run_report(
    report_date: date,
    config_dir: Path,
    reports_dir: Path,
    offline_sample: bool = False,
    max_topics: int = 8,
    max_companies: int = 8,
) -> RunResult:
    data_gaps: list[str] = []
    companies = load_company_universe(config_dir)
    topic_keywords = load_topic_keywords(config_dir)
    sentiment_keywords = load_sentiment_keywords(config_dir)
    model_weights = load_model_weights(config_dir)
    rss_feeds = load_rss_feeds(config_dir)
    reference_sources = load_reference_sources(config_dir)

    articles = NewsCollector(rss_feeds=rss_feeds, data_gaps=data_gaps).collect(
        report_date=report_date,
        offline_sample=offline_sample,
    )
    topics = TopicAnalyzer(
        topic_keywords=topic_keywords,
        companies=companies,
        sentiment_keywords=sentiment_keywords,
        model_weights=model_weights,
    ).analyze(
        articles,
        max_topics=max_topics,
        max_companies_per_topic=max_companies,
    )

    fundamentals = FundamentalsCollector(data_gaps=data_gaps, report_date=report_date)
    prices = PricePerformanceCollector(data_gaps=data_gaps, report_date=report_date)
    for topic in topics:
        for relation in topic.related_companies:
            relation.metrics = fundamentals.collect_for_company(relation.company)
            relation.price_performance = prices.collect_for_company(relation.company, relation.impact_direction)

    validation = daily_market_validation(topics)
    historical_topic_scores = load_historical_topic_scores(reports_dir, report_date.isoformat())
    topics = optimize_topic_order(topics, validation, historical_topic_scores, model_weights)
    validation = daily_market_validation(topics)
    validation_history = load_validation_history(reports_dir, report_date.isoformat(), validation)
    backtest_summary = latest_backtest_summary(reports_dir)
    renderer = ReportRenderer()
    markdown_text = renderer.render_markdown(
        report_date,
        topics,
        data_gaps,
        validation_history,
        backtest_summary,
        reference_sources,
    )
    html_text = renderer.render_html(markdown_text, topics, validation_history)
    markdown_path, html_path = renderer.write(reports_dir, report_date, markdown_text, html_text)
    summary_path = write_summary(
        reports_dir,
        report_date,
        topics,
        data_gaps,
        validation,
        backtest_summary,
        reference_sources,
    )

    return RunResult(
        report_date=report_date,
        topics=topics,
        data_gaps=data_gaps,
        output_markdown=str(markdown_path),
        output_html=str(html_path),
        output_summary=str(summary_path),
    )


def write_summary(
    reports_dir: Path,
    report_date: date,
    topics: list,
    data_gaps: list[str],
    validation: dict | None = None,
    backtest_summary: dict | None = None,
    reference_sources: list[dict[str, str]] | None = None,
) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = summary_path_for_date(reports_dir, report_date.isoformat())
    payload = {
        "date": report_date.isoformat(),
        "topics": [_topic_to_summary(topic) for topic in topics],
        "market_validation": validation or daily_market_validation(topics),
        "backtest_summary": backtest_summary or {},
        "reference_sources": reference_sources or [],
        "data_gaps": sorted(set(data_gaps)),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def load_validation_history(reports_dir: Path, report_date: str, current_validation: dict) -> list[dict]:
    history: dict[str, dict] = {}
    if reports_dir.exists():
        for path in reports_dir.glob("*-market-topics.json"):
            try:
                payload = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            validation = payload.get("market_validation")
            date_text = str(payload.get("date", ""))
            if not date_text or not isinstance(validation, dict):
                continue
            history[date_text] = _history_item(date_text, validation)
    history[report_date] = _history_item(report_date, current_validation)
    return [history[key] for key in sorted(history)][-30:]


def _history_item(report_date: str, validation: dict) -> dict:
    return {
        "date": report_date,
        "correlation_3d": validation.get("correlation_3d"),
        "correlation_5d": validation.get("correlation_5d"),
        "aligned_ratio": validation.get("aligned_ratio"),
        "validated_count": validation.get("validated_count", 0),
    }


def load_historical_topic_scores(reports_dir: Path, report_date: str) -> dict[str, float]:
    scores: dict[str, list[float]] = {}
    if not reports_dir.exists():
        return {}
    for path in reports_dir.glob("*-market-topics.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if str(payload.get("date", "")) >= report_date:
            continue
        validation = payload.get("market_validation", {})
        for item in validation.get("topics", []) if isinstance(validation, dict) else []:
            topic = str(item.get("topic", ""))
            score = item.get("market_confirmation_score")
            if topic and isinstance(score, (int, float)):
                scores.setdefault(topic, []).append(float(score))
    return {topic: sum(values) / len(values) for topic, values in scores.items() if values}


def optimize_topic_order(
    topics: list,
    validation: dict,
    historical_topic_scores: dict[str, float],
    model_weights: dict[str, float] | None = None,
) -> list:
    weights = model_weights or {}
    current_scores = {
        item["topic"]: item.get("market_confirmation_score")
        for item in validation.get("topics", [])
        if item.get("market_confirmation_score") is not None
    }

    def sort_key(topic) -> tuple[float, int]:
        optimized = float(topic.score) * 10.0 * float(weights.get("news_heat_weight", 1.0))
        current_score = current_scores.get(topic.name)
        history_score = historical_topic_scores.get(topic.name)
        if isinstance(current_score, (int, float)):
            current_component = (float(current_score) - 50.0) * float(
                weights.get("current_market_confirmation_weight", 0.65)
            )
            if float(current_score) < 50.0:
                current_component /= max(0.1, float(weights.get("price_divergence_penalty", 0.5)))
            optimized += current_component
        if isinstance(history_score, (int, float)):
            optimized += (float(history_score) - 50.0) * float(weights.get("historical_topic_score_weight", 0.35))
        return (optimized, topic.score)

    return sorted(topics, key=sort_key, reverse=True)


def _topic_to_summary(topic) -> dict:
    return {
        "name": topic.name,
        "score": topic.score,
        "direction": topic.direction,
        "sentiment_score": topic.sentiment_score,
        "companies": [_relation_to_summary(relation) for relation in topic.related_companies],
    }


def _relation_to_summary(relation) -> dict:
    company = relation.company
    price = relation.price_performance
    return {
        "market": company.market,
        "ticker": company.ticker,
        "name_zh": company.name_zh,
        "name_en": company.name_en,
        "relation_type": relation.relation_type,
        "directional_confidence": _directional_confidence_value(
            relation.impact_direction,
            relation.confidence,
            price.validation,
        ),
        "return_3d": price.return_3d,
        "return_5d": price.return_5d,
        "current_price": price.current_price,
        "all_time_high": price.all_time_high,
        "drawdown_from_high": price.drawdown_from_high,
        "all_time_high_date": price.all_time_high_date,
        "price_validation": price.validation,
    }


def _directional_confidence_value(direction: str, confidence: float, price_validation: str) -> str:
    return adjusted_directional_confidence(direction, confidence, price_validation)
