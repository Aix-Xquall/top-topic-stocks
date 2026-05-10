from __future__ import annotations

import html
from datetime import date
from pathlib import Path

from ..analysis.validation import (
    adjusted_directional_confidence,
    daily_market_validation,
    format_optional_number,
    format_optional_percent,
)
from ..models import Topic


DISCLAIMER = "本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。"


class ReportRenderer:
    def render_markdown(
        self,
        report_date: date,
        topics: list[Topic],
        data_gaps: list[str],
        validation_history: list[dict] | None = None,
        backtest_summary: dict | None = None,
        reference_sources: list[dict[str, str]] | None = None,
    ) -> str:
        validation = daily_market_validation(topics)
        lines: list[str] = [
            f"# 每日股市熱門話題分析 - {report_date.isoformat()}",
            "",
            DISCLAIMER,
            "",
            "## 重點摘要",
            "",
        ]
        if not topics:
            lines.extend(["目前沒有足夠新聞可形成熱門話題。", ""])
        else:
            for index, topic in enumerate(topics[:5], start=1):
                topic_validation = next(
                    (item for item in validation["topics"] if item["topic"] == topic.name),
                    {},
                )
                confirmation = format_optional_number(topic_validation.get("market_confirmation_score"))
                aligned = topic_validation.get("aligned_count", 0)
                validated = topic_validation.get("validated_count", 0)
                lines.append(
                    f"{index}. **{topic.name}**｜{topic.direction}｜熱度 {topic.score}｜"
                    f"市場確認 {confirmation}｜同向 {aligned}/{validated}"
                )
            lines.append("")

        lines.extend(_validation_markdown(validation))
        lines.extend(_history_markdown(validation_history or []))
        lines.extend(_backtest_summary_markdown(backtest_summary or {}))
        lines.extend(_reference_sources_markdown(reference_sources or []))

        for topic in topics:
            lines.extend(
                [
                    f"## {topic.name}",
                    "",
                    f"摘要：{topic.summary}",
                    "",
                    "### 相關公司",
                    "",
                ]
            )
            if topic.related_companies:
                lines.append(
                    "| 公司 | 關聯 | 方向性信心 | 3日 | 5日 | 現價 | 歷高 | 距高點 | 驗證 | EPS | PER | 營收 / YoY | 日期 |"
                )
                lines.append("| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | ---: | ---: | --- | --- |")
                for relation in topic.related_companies:
                    company = relation.company
                    metrics = relation.metrics
                    price = relation.price_performance
                    lines.append(
                        "| "
                        + " | ".join(
                            [
                                f"{company.ticker} {company.name_zh}",
                                relation.relation_type,
                                _directional_confidence(
                                    relation.impact_direction,
                                    relation.confidence,
                                    price.validation,
                                ),
                                price.return_3d,
                                price.return_5d,
                                price.current_price,
                                price.all_time_high,
                                price.drawdown_from_high,
                                price.validation,
                                metrics.eps,
                                metrics.pe,
                                _revenue_cell(metrics.revenue, metrics.currency, metrics.revenue_yoy),
                                metrics.as_of_date,
                            ]
                        )
                        + " |"
                    )
                lines.append("")
                lines.append("關聯理由（前 3）：")
                for relation in topic.related_companies[:3]:
                    lines.append(f"- {relation.company.ticker}：{relation.reason}")
                    if relation.metrics.notes:
                        lines.append(f"  - 資料備註：{'；'.join(relation.metrics.notes)}")
            else:
                lines.append("目前沒有足夠依據推估相關公司。")
            lines.extend(["", "### 主要來源", ""])
            for article in topic.articles[:3]:
                title = _escape_md(article.title)
                lines.append(f"- [{title}]({article.url}) - {article.source} {article.published_at}".strip())
            lines.append("")

        lines.extend(["## 資料缺口與需人工確認", ""])
        if data_gaps:
            for gap in sorted(set(data_gaps)):
                lines.append(f"- {gap}")
        else:
            lines.append("- 無重大資料缺口。")
        lines.append("")
        return "\n".join(lines)

    def render_html(
        self,
        markdown_text: str,
        topics: list[Topic] | None = None,
        validation_history: list[dict] | None = None,
        backtest_summary: dict | None = None,
    ) -> str:
        if topics:
            return _compact_html_report(topics, validation_history or [], backtest_summary or {})
        body = _markdown_subset_to_html(markdown_text)
        chart = _validation_chart_html(topics or [])
        history_chart = _history_chart_html(validation_history or [])
        return "\n".join(
            [
                "<!doctype html>",
                '<html lang="zh-Hant">',
                "<head>",
                '<meta charset="utf-8">',
                '<meta name="viewport" content="width=device-width, initial-scale=1">',
                "<title>每日股市熱門話題分析</title>",
                "<style>",
                "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans TC',sans-serif;line-height:1.55;margin:24px;color:#1f2937;background:#f8fafc}",
                "main{max-width:1180px;margin:0 auto;background:#fff;padding:24px;border:1px solid #e5e7eb;border-radius:8px}",
                "h1,h2,h3{line-height:1.25;color:#111827} h1{margin-top:0} table{border-collapse:collapse;width:100%;font-size:13px;margin:10px 0 18px}",
                "th,td{border:1px solid #d1d5db;padding:7px;vertical-align:top} th{background:#f3f4f6;text-align:left}",
                "a{color:#0f766e} code{background:#f3f4f6;padding:2px 4px;border-radius:4px} .chart{margin:16px 0 24px;padding:14px;border:1px solid #e5e7eb;border-radius:8px;background:#fbfdff}.bar-row{display:grid;grid-template-columns:minmax(120px,220px) 1fr 64px;gap:10px;align-items:center;margin:8px 0}.bar-track{height:14px;background:#e5e7eb;border-radius:999px;overflow:hidden}.bar{height:100%;background:#0f766e}.bar.low{background:#b45309}.bar.mid{background:#2563eb}.muted{color:#6b7280;font-size:13px}",
                "</style>",
                "</head>",
                "<body><main>",
                body,
                chart,
                history_chart,
                "</main></body></html>",
            ]
        )

    def write(self, reports_dir: Path, report_date: date, markdown_text: str, html_text: str) -> tuple[Path, Path]:
        reports_dir.mkdir(parents=True, exist_ok=True)
        stem = f"{report_date.isoformat()}-market-topics"
        markdown_path = reports_dir / f"{stem}.md"
        html_path = reports_dir / f"{stem}.html"
        markdown_path.write_text(markdown_text, encoding="utf-8")
        html_path.write_text(html_text, encoding="utf-8")
        return markdown_path, html_path


def _escape_md(value: str) -> str:
    return value.replace("[", "\\[").replace("]", "\\]")


def _revenue_cell(revenue: str, currency: str, revenue_yoy: str) -> str:
    revenue_text = f"{revenue} {currency}".strip()
    return f"{revenue_text} / {revenue_yoy}"


def _validation_markdown(validation: dict) -> list[str]:
    correlation_3d = validation.get("correlation_3d")
    correlation_5d = validation.get("correlation_5d")
    aligned = validation.get("aligned_count", 0)
    validated = validation.get("validated_count", 0)
    lines = [
        "## 市場驗證",
        "",
        "為避免循環驗證，相關係數使用「價格調整前」方向信心與股價報酬計算。",
        "",
        f"- 3日相關係數：{format_optional_number(correlation_3d)}（樣本 {validation.get('sample_count_3d', 0)}）",
        f"- 5日相關係數：{format_optional_number(correlation_5d)}（樣本 {validation.get('sample_count_5d', 0)}）",
        f"- 同向比例：{aligned}/{validated}",
        "",
        "| 話題 | 市場確認 | 同向 | 背離 | 3日方向報酬 | 5日方向報酬 |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in validation.get("topics", [])[:8]:
        lines.append(
            "| "
            + " | ".join(
                [
                    item["topic"],
                    format_optional_number(item.get("market_confirmation_score")),
                    f"{item.get('aligned_count', 0)}/{item.get('validated_count', 0)}",
                    str(item.get("diverged_count", 0)),
                    format_optional_percent(item.get("avg_directional_return_3d")),
                    format_optional_percent(item.get("avg_directional_return_5d")),
                ]
            )
            + " |"
        )
    lines.append("")
    lines.extend(_method_suggestions_markdown(validation))
    return lines


def _method_suggestions_markdown(validation: dict) -> list[str]:
    validated = int(validation.get("validated_count", 0) or 0)
    correlation = validation.get("correlation_3d")
    aligned_ratio = validation.get("aligned_ratio")
    lines = ["### 方法調整建議", ""]
    if validated < 10:
        lines.append("- 有效樣本少於 10，先累積多日資料；目前不做大幅調參。")
    elif correlation is not None and correlation < -0.10:
        lines.append("- 方向信心與股價呈負相關；應檢查正負向詞庫，並降低新聞直接提及但股價背離的權重。")
    elif correlation is not None and correlation < 0.10:
        lines.append("- 相關性偏弱；應提高同向價格確認權重，降低泛 AI、泛半導體等寬標籤推估權重。")
    else:
        lines.append("- 方向信心與股價大致正相關；維持目前方法，優先擴充樣本與資料源。")
    if aligned_ratio is not None and aligned_ratio < 0.45:
        lines.append("- 同向比例偏低；隔日排序應降低背離題材與低信心供應鏈推估。")
    lines.append("")
    return lines


def _history_markdown(history: list[dict]) -> list[str]:
    rows = [item for item in history if item.get("validated_count", 0)]
    if not rows:
        return []
    lines = [
        "## 每日迭代追蹤",
        "",
        "此表用來觀察每日模型分數是否逐步貼近市場表現。",
        "",
        "| 日期 | 3日相關 | 5日相關 | 同向比例 | 樣本 |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for item in rows[-14:]:
        aligned_ratio = item.get("aligned_ratio")
        lines.append(
            "| "
            + " | ".join(
                [
                    str(item.get("date", "")),
                    format_optional_number(item.get("correlation_3d")),
                    format_optional_number(item.get("correlation_5d")),
                    format_optional_percent(aligned_ratio * 100 if aligned_ratio is not None else None),
                    str(item.get("validated_count", 0)),
                ]
            )
            + " |"
        )
    lines.append("")
    return lines


def _backtest_summary_markdown(summary: dict) -> list[str]:
    if not summary:
        return []
    aligned_ratio = summary.get("aligned_ratio")
    adjusted = "已調整" if summary.get("updated") else "未調整"
    days = int(summary.get("days", 5) or 5)
    lines = [
        "## 歷史回測摘要",
        "",
        f"- 回測日期：{summary.get('date', 'N/A')}",
        f"- 近{days}日 3日相關：{format_optional_number(summary.get('correlation_3d'))}",
        f"- 近{days}日 5日相關：{format_optional_number(summary.get('correlation_5d'))}",
        f"- 同向比例：{format_optional_percent(aligned_ratio * 100 if aligned_ratio is not None else None)}",
        f"- 權重狀態：{adjusted}",
        "",
    ]
    direction_accuracy = summary.get("direction_accuracy", summary.get("aligned_ratio"))
    confidence_calibration = summary.get("confidence_calibration", summary.get("correlation_3d"))
    lines.extend(
        [
            f"- 方向準確度：{format_optional_percent(direction_accuracy * 100 if direction_accuracy is not None else None)}",
            f"- 信心排序準確度：{format_optional_number(confidence_calibration)}",
            f"- 診斷：{summary.get('calibration_strategy') or summary.get('adjustment_strategy') or 'N/A'}",
            "",
        ]
    )
    misses = summary.get("overconfident_misses") or []
    if misses:
        lines.extend(["主要錯誤來源（高信心但報酬不佳）：", ""])
        for item in misses[:5]:
            lines.append(
                f"- {item.get('topic', 'N/A')}｜{item.get('ticker', '')} {item.get('name_zh', '')}｜"
                f"信心 {item.get('confidence', 'N/A')}｜3日 {item.get('return_3d', 'N/A')}｜"
                f"{item.get('price_validation', 'N/A')}"
            )
        lines.append("")
    if summary.get("reason"):
        lines.extend([f"調整原因：{summary['reason']}", ""])
    return lines


def _reference_sources_markdown(sources: list[dict[str, str]]) -> list[str]:
    if not sources:
        return []
    lines = [
        "## 參考來源",
        "",
        "| 類別 | 平台 | 用途 | 讀取方式 |",
        "| --- | --- | --- | --- |",
    ]
    for source in sources:
        name = source.get("name", "")
        url = source.get("url", "")
        display_name = f"[{_escape_md(name)}]({url})" if url else _escape_md(name)
        lines.append(
            "| "
            + " | ".join(
                [
                    source.get("category", ""),
                    display_name,
                    source.get("usage", ""),
                    source.get("mode", ""),
                ]
            )
            + " |"
        )
    lines.append("")
    return lines


def _compact_html_report(topics: list[Topic], validation_history: list[dict], backtest_summary: dict) -> str:
    validation = daily_market_validation(topics)
    topic_metrics = {item.get("topic"): item for item in validation.get("topics", [])}
    top_topics = topics[:5]
    topic_rows = "\n".join(
        _compact_topic_row(index, topic, topic_metrics.get(topic.name, {}))
        for index, topic in enumerate(top_topics, start=1)
    )
    sections = "\n".join(
        _compact_topic_section(index, topic, topic_metrics.get(topic.name, {}))
        for index, topic in enumerate(top_topics, start=1)
    )
    validation_chart = _validation_chart_html(topics)
    history_chart = _history_chart_html(validation_history)
    backtest_html = _compact_backtest_html(backtest_summary)
    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="zh-Hant">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            "<title>每日股市熱門話題分析</title>",
            "<style>",
            "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans TC',sans-serif;line-height:1.5;margin:0;color:#172033;background:#f6f7f9}",
            "main{max-width:1120px;margin:0 auto;padding:22px 16px 40px}",
            "header{margin-bottom:18px}.eyebrow{color:#667085;font-size:13px;margin:0 0 6px}h1{font-size:26px;margin:0;color:#101828}h2{font-size:19px;margin:22px 0 10px}h3{font-size:16px;margin:0 0 6px}",
            ".summary-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:14px 0}.metric,.topic-card,.panel{background:#fff;border:1px solid #e3e7ee;border-radius:8px;padding:12px}.metric strong{display:block;font-size:20px;color:#101828}.metric span{color:#667085;font-size:13px}",
            "table{border-collapse:collapse;width:100%;font-size:13px;background:#fff}th,td{border-bottom:1px solid #e5e7eb;padding:8px;text-align:left;vertical-align:top}th{color:#475467;background:#f8fafc;font-weight:600}.topic-table td:first-child{font-weight:700}",
            ".topic-card{margin:12px 0}.topic-head{display:flex;gap:10px;justify-content:space-between;align-items:flex-start}.topic-title{display:flex;gap:8px;align-items:center}.rank{display:inline-flex;align-items:center;justify-content:center;width:24px;height:24px;border-radius:999px;background:#172033;color:#fff;font-size:12px}.muted{color:#667085}.compact-note{font-size:13px;color:#475467;margin:4px 0 10px}",
            ".badge{display:inline-block;border-radius:999px;padding:2px 8px;font-size:12px;background:#eef4ff;color:#175cd3}.pos{color:#087443}.neg{color:#b42318}.flat{color:#667085}details{margin-top:8px}summary{cursor:pointer;color:#175cd3;font-size:13px}.sources{margin:8px 0 0;padding-left:18px;font-size:13px}",
            ".chart{margin:16px 0 24px;padding:14px;border:1px solid #e5e7eb;border-radius:8px;background:#fff}.bar-row{display:grid;grid-template-columns:minmax(120px,220px) 1fr 64px;gap:10px;align-items:center;margin:8px 0}.bar-track{height:12px;background:#e5e7eb;border-radius:999px;overflow:hidden}.bar{height:100%;background:#0f766e}.bar.low{background:#b45309}.bar.mid{background:#2563eb}",
            "@media(max-width:760px){.summary-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.topic-head{display:block}table{font-size:12px}th,td{padding:7px 6px}}",
            "</style>",
            "</head>",
            "<body><main>",
            "<header>",
            '<p class="eyebrow">研究輔助，不構成投資建議</p>',
            "<h1>每日股市熱門話題分析</h1>",
            "</header>",
            _compact_summary_grid(validation, backtest_summary),
            "<h2>熱門題材排行</h2>",
            f'<table class="topic-table"><tr><th>#</th><th>題材</th><th>方向</th><th>市場確認</th><th>同向</th><th>前三家公司</th></tr>{topic_rows}</table>',
            backtest_html,
            validation_chart,
            "<h2>題材摘要</h2>",
            sections,
            history_chart,
            "</main></body></html>",
        ]
    )


def _compact_summary_grid(validation: dict, backtest_summary: dict) -> str:
    aligned_ratio = validation.get("aligned_ratio")
    backtest_ratio = backtest_summary.get("direction_accuracy", backtest_summary.get("aligned_ratio"))
    items = [
        ("今日 3日相關", format_optional_number(validation.get("correlation_3d"))),
        ("今日同向比例", format_optional_percent(aligned_ratio * 100 if aligned_ratio is not None else None)),
        ("近5日信心排序", format_optional_number(backtest_summary.get("confidence_calibration"))),
        ("近5日方向準確", format_optional_percent(backtest_ratio * 100 if backtest_ratio is not None else None)),
    ]
    return '<section class="summary-grid">' + "".join(
        f'<div class="metric"><strong>{html.escape(value)}</strong><span>{html.escape(label)}</span></div>'
        for label, value in items
    ) + "</section>"


def _compact_topic_row(index: int, topic: Topic, metrics: dict) -> str:
    top_companies = "、".join(
        f"{relation.company.ticker} {relation.company.name_zh}" for relation in topic.related_companies[:3]
    ) or "待確認"
    aligned = f"{metrics.get('aligned_count', 0)}/{metrics.get('validated_count', 0)}"
    return (
        "<tr>"
        f"<td>{index}</td>"
        f"<td>{html.escape(topic.name)}</td>"
        f"<td>{html.escape(topic.direction)}</td>"
        f"<td>{html.escape(format_optional_number(metrics.get('market_confirmation_score')))}</td>"
        f"<td>{html.escape(aligned)}</td>"
        f"<td>{html.escape(top_companies)}</td>"
        "</tr>"
    )


def _compact_topic_section(index: int, topic: Topic, metrics: dict) -> str:
    company_rows = "\n".join(_compact_company_row(relation) for relation in topic.related_companies[:3])
    if not company_rows:
        company_rows = '<tr><td colspan="7">目前未對應到可驗證公司</td></tr>'
    source_rows = "\n".join(
        f'<li><a href="{html.escape(article.url)}" target="_blank" rel="noopener noreferrer">{html.escape(article.title)}</a></li>'
        for article in topic.articles[:2]
    )
    details_rows = "\n".join(_detail_company_row(relation) for relation in topic.related_companies[3:])
    details = ""
    if details_rows:
        details = (
            "<details><summary>更多公司</summary>"
            f"<table><tr><th>公司</th><th>方向性信心</th><th>3日</th><th>5日</th><th>現價</th><th>高點跌幅</th></tr>{details_rows}</table>"
            "</details>"
        )
    return (
        '<section class="topic-card">'
        '<div class="topic-head">'
        f'<div class="topic-title"><span class="rank">{index}</span><div><h3>{html.escape(topic.name)}</h3>'
        f'<div class="muted">方向：{html.escape(topic.direction)}｜熱度：{topic.score}｜市場確認：{html.escape(format_optional_number(metrics.get("market_confirmation_score")))}</div></div></div>'
        f'<span class="badge">同向 {metrics.get("aligned_count", 0)}/{metrics.get("validated_count", 0)}</span>'
        "</div>"
        f'<p class="compact-note">{html.escape(_short_text(topic.summary, 120))}</p>'
        f"<table><tr><th>公司</th><th>關聯</th><th>方向性信心</th><th>3日</th><th>5日</th><th>高點跌幅</th><th>驗證</th></tr>{company_rows}</table>"
        f"{details}"
        f'<details><summary>主要來源</summary><ul class="sources">{source_rows or "<li>無來源</li>"}</ul></details>'
        "</section>"
    )


def _compact_company_row(relation) -> str:
    company = relation.company
    price = relation.price_performance
    confidence = _directional_confidence(relation.impact_direction, relation.confidence, price.validation)
    confidence_class = "pos" if confidence.startswith("+") else "neg" if confidence.startswith("-") else "flat"
    return (
        "<tr>"
        f"<td>{html.escape(company.ticker)} {html.escape(company.name_zh)}</td>"
        f"<td>{html.escape(relation.relation_type)}</td>"
        f'<td class="{confidence_class}">{html.escape(confidence)}</td>'
        f"<td>{html.escape(price.return_3d)}</td>"
        f"<td>{html.escape(price.return_5d)}</td>"
        f"<td>{html.escape(price.drawdown_from_high)}</td>"
        f"<td>{html.escape(price.validation)}</td>"
        "</tr>"
    )


def _detail_company_row(relation) -> str:
    company = relation.company
    price = relation.price_performance
    confidence = _directional_confidence(relation.impact_direction, relation.confidence, price.validation)
    confidence_class = "pos" if confidence.startswith("+") else "neg" if confidence.startswith("-") else "flat"
    return (
        "<tr>"
        f"<td>{html.escape(company.ticker)} {html.escape(company.name_zh)}</td>"
        f'<td class="{confidence_class}">{html.escape(confidence)}</td>'
        f"<td>{html.escape(price.return_3d)}</td>"
        f"<td>{html.escape(price.return_5d)}</td>"
        f"<td>{html.escape(price.current_price)}</td>"
        f"<td>{html.escape(price.drawdown_from_high)}</td>"
        "</tr>"
    )


def _compact_backtest_html(summary: dict) -> str:
    if not summary:
        return ""
    learning = summary.get("keyword_company_learning", {})
    learning_html = ""
    if isinstance(learning, dict) and learning:
        hit_rate = learning.get("hit_rate_5d")
        learning_html = (
            "<p>"
            f"樣本學習：有效 {html.escape(str(learning.get('valid_sample_count', 0)))} 筆，"
            f"5日同向 {html.escape(format_optional_percent(float(hit_rate) * 100 if isinstance(hit_rate, (int, float)) else None))}，"
            f"信心排序 {html.escape(format_optional_number(learning.get('confidence_correlation_5d')))}"
            "</p>"
        )
    return (
        '<section class="panel">'
        "<h2>近5日方法驗證</h2>"
        f"<p>診斷：{html.escape(str(summary.get('calibration_strategy') or summary.get('adjustment_strategy') or 'N/A'))}｜"
        f"3日相關 {html.escape(format_optional_number(summary.get('correlation_3d')))}｜"
        f"5日相關 {html.escape(format_optional_number(summary.get('correlation_5d')))}｜"
        f"樣本 {html.escape(str(summary.get('validated_count', 0)))}</p>"
        f"{learning_html}"
        f'<p class="muted">{html.escape(str(summary.get("reason", "")))}</p>'
        "</section>"
    )


def _short_text(value: str, limit: int) -> str:
    clean = " ".join(str(value).split())
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1] + "…"


def _validation_chart_html(topics: list[Topic]) -> str:
    validation = daily_market_validation(topics)
    rows = [
        item
        for item in validation.get("topics", [])[:8]
        if item.get("market_confirmation_score") is not None
    ]
    if not rows:
        return ""
    output = [
        '<section class="chart">',
        "<h2>市場確認圖表</h2>",
        '<p class="muted">分數越高，代表題材方向與近 3 日股價表現越一致；低於 50 代表市場確認偏弱。</p>',
    ]
    for item in rows:
        score = float(item["market_confirmation_score"])
        width = max(0.0, min(100.0, score))
        css_class = "low" if score < 50 else "mid" if score < 70 else ""
        output.append(
            '<div class="bar-row">'
            f"<div>{html.escape(str(item['topic']))}</div>"
            '<div class="bar-track">'
            f'<div class="bar {css_class}" style="width:{width:.1f}%"></div>'
            "</div>"
            f"<strong>{score:.1f}</strong>"
            "</div>"
        )
    output.append("</section>")
    return "\n".join(output)


def _history_chart_html(history: list[dict]) -> str:
    rows = [item for item in history[-14:] if item.get("validated_count", 0)]
    if not rows:
        return ""
    output = [
        '<section class="chart">',
        "<h2>每日相關性追蹤</h2>",
        '<p class="muted">長條為 3 日相關係數，0 在中線；越往右代表方向信心與個股表現越正相關。</p>',
    ]
    for item in rows:
        correlation = item.get("correlation_3d")
        if correlation is None:
            width = 0.0
            offset = 50.0
            label = "N/A"
        else:
            bounded = max(-1.0, min(1.0, float(correlation)))
            width = abs(bounded) * 50.0
            offset = 50.0 if bounded >= 0 else 50.0 - width
            label = f"{bounded:.2f}"
        color = "#0f766e" if correlation is None or float(correlation) >= 0 else "#b91c1c"
        output.append(
            '<div class="bar-row">'
            f"<div>{html.escape(str(item.get('date', '')))}</div>"
            '<div class="bar-track" style="position:relative">'
            '<div style="position:absolute;left:50%;top:0;width:1px;height:100%;background:#64748b"></div>'
            f'<div style="position:absolute;left:{offset:.1f}%;top:0;width:{width:.1f}%;height:100%;background:{color}"></div>'
            "</div>"
            f"<strong>{label}</strong>"
            "</div>"
        )
    output.append("</section>")
    return "\n".join(output)


def _directional_confidence(direction: str, confidence: float, price_validation: str = "N/A") -> str:
    return adjusted_directional_confidence(direction, confidence, price_validation)


def _market_adjusted_confidence(confidence: float, price_validation: str) -> float:
    from ..analysis.validation import market_adjusted_confidence

    return market_adjusted_confidence(confidence, price_validation)


def _join_sources(fundamental_sources: str, price_source: str) -> str:
    parts = []
    if fundamental_sources and fundamental_sources != "N/A":
        parts.append(fundamental_sources)
    if price_source and price_source != "N/A":
        parts.append(price_source)
    return "<br>".join(parts) if parts else "N/A"


def _markdown_subset_to_html(markdown_text: str) -> str:
    lines = markdown_text.splitlines()
    output: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            output.append("</ul>")
            in_ul = False
        if in_ol:
            output.append("</ol>")
            in_ol = False

    for line in lines:
        if line.startswith("| "):
            close_lists()
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if set(cells) == {"---"} or all(cell.replace(":", "").replace("-", "") == "" for cell in cells):
                continue
            tag = "th" if not in_table else "td"
            if not in_table:
                output.append("<table>")
                in_table = True
            output.append("<tr>" + "".join(f"<{tag}>{_inline(cell)}</{tag}>" for cell in cells) + "</tr>")
            continue
        if in_table:
            output.append("</table>")
            in_table = False

        stripped = line.strip()
        if not stripped:
            close_lists()
            output.append("")
            continue
        if stripped.startswith("# "):
            close_lists()
            output.append(f"<h1>{_inline(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            close_lists()
            output.append(f"<h2>{_inline(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            close_lists()
            output.append(f"<h3>{_inline(stripped[4:])}</h3>")
        elif stripped.startswith("- "):
            if not in_ul:
                close_lists()
                output.append("<ul>")
                in_ul = True
            output.append(f"<li>{_inline(stripped[2:])}</li>")
        elif len(stripped) > 3 and stripped[0].isdigit() and ". " in stripped[:4]:
            if not in_ol:
                close_lists()
                output.append("<ol>")
                in_ol = True
            output.append(f"<li>{_inline(stripped.split('. ', 1)[1])}</li>")
        else:
            close_lists()
            output.append(f"<p>{_inline(stripped)}</p>")
    if in_table:
        output.append("</table>")
    close_lists()
    return "\n".join(output)


def _inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = escaped.replace("&lt;br&gt;", "<br>")
    escaped = re_link(escaped)
    return escaped.replace("**", "")


def re_link(text: str) -> str:
    import re

    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    return pattern.sub(r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', text)
