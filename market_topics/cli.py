from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .analysis import TopicAnalyzer
from .collectors import FundamentalsCollector, NewsCollector, PricePerformanceCollector
from .config import load_company_universe, load_rss_feeds, load_sentiment_keywords, load_topic_keywords
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
    rss_feeds = load_rss_feeds(config_dir)

    articles = NewsCollector(rss_feeds=rss_feeds, data_gaps=data_gaps).collect(
        report_date=report_date,
        offline_sample=offline_sample,
    )
    topics = TopicAnalyzer(
        topic_keywords=topic_keywords,
        companies=companies,
        sentiment_keywords=sentiment_keywords,
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

    renderer = ReportRenderer()
    markdown_text = renderer.render_markdown(report_date, topics, data_gaps)
    html_text = renderer.render_html(markdown_text)
    markdown_path, html_path = renderer.write(reports_dir, report_date, markdown_text, html_text)
    summary_path = write_summary(reports_dir, report_date, topics, data_gaps)

    return RunResult(
        report_date=report_date,
        topics=topics,
        data_gaps=data_gaps,
        output_markdown=str(markdown_path),
        output_html=str(html_path),
        output_summary=str(summary_path),
    )


def write_summary(reports_dir: Path, report_date: date, topics: list, data_gaps: list[str]) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = summary_path_for_date(reports_dir, report_date.isoformat())
    payload = {
        "date": report_date.isoformat(),
        "topics": [_topic_to_summary(topic) for topic in topics],
        "data_gaps": sorted(set(data_gaps)),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


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
        "price_validation": price.validation,
    }


def _directional_confidence_value(direction: str, confidence: float, price_validation: str) -> str:
    adjusted = confidence
    if price_validation == "背離":
        adjusted *= 0.50
    elif price_validation == "未明確":
        adjusted *= 0.75
    if direction == "正向":
        return f"+{adjusted:.2f}"
    if direction == "負向":
        return f"-{adjusted:.2f}"
    return "0.00"
