from __future__ import annotations

import html
from datetime import date
from pathlib import Path

from ..models import Topic


DISCLAIMER = "本報告由自動化流程產生，僅供研究輔助，不構成任何投資建議。"


class ReportRenderer:
    def render_markdown(self, report_date: date, topics: list[Topic], data_gaps: list[str]) -> str:
        lines: list[str] = [
            f"# 每日股市熱門話題分析 - {report_date.isoformat()}",
            "",
            DISCLAIMER,
            "",
            "## 今日熱門話題排行",
            "",
        ]
        if not topics:
            lines.extend(["目前沒有足夠新聞可形成熱門話題。", ""])
        else:
            for index, topic in enumerate(topics, start=1):
                lines.append(f"{index}. **{topic.name}**：熱度分數 {topic.score}，方向 {topic.direction}")
            lines.append("")

        for topic in topics:
            lines.extend(
                [
                    f"## {topic.name}",
                    "",
                    f"- 熱度分數：{topic.score}",
                    f"- 話題方向：{topic.direction}（分數 {topic.sentiment_score}）",
                    f"- 中文摘要：{topic.summary}",
                    "",
                    "### 可能相關公司",
                    "",
                ]
            )
            if topic.related_companies:
                lines.append(
                    "| 市場 | Ticker | 公司 | 關聯類型 | 方向性信心 | 3日漲幅 | 5日漲幅 | 價格驗證 | EPS | 本益比 | 營收 | 營收 YoY | 資料日期 | 來源 |"
                )
                lines.append("| --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- | --- |")
                for relation in topic.related_companies:
                    company = relation.company
                    metrics = relation.metrics
                    price = relation.price_performance
                    sources = "<br>".join(metrics.sources) if metrics.sources else "N/A"
                    combined_sources = _join_sources(sources, price.source)
                    lines.append(
                        "| "
                        + " | ".join(
                            [
                                company.market,
                                company.ticker,
                                f"{company.name_zh} / {company.name_en}",
                                relation.relation_type,
                                _directional_confidence(
                                    relation.impact_direction,
                                    relation.confidence,
                                    price.validation,
                                ),
                                price.return_3d,
                                price.return_5d,
                                price.validation,
                                metrics.eps,
                                metrics.pe,
                                f"{metrics.revenue} {metrics.currency}".strip(),
                                metrics.revenue_yoy,
                                metrics.as_of_date,
                                combined_sources,
                            ]
                        )
                        + " |"
                    )
                lines.append("")
                lines.append("關聯理由：")
                for relation in topic.related_companies:
                    lines.append(f"- {relation.company.ticker}：{relation.reason}")
                    if relation.metrics.notes:
                        lines.append(f"  - 資料備註：{'；'.join(relation.metrics.notes)}")
            else:
                lines.append("目前沒有足夠依據推估相關公司。")
            lines.extend(["", "### 主要來源", ""])
            for article in topic.articles:
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

    def render_html(self, markdown_text: str) -> str:
        body = _markdown_subset_to_html(markdown_text)
        return "\n".join(
            [
                "<!doctype html>",
                '<html lang="zh-Hant">',
                "<head>",
                '<meta charset="utf-8">',
                '<meta name="viewport" content="width=device-width, initial-scale=1">',
                "<title>每日股市熱門話題分析</title>",
                "<style>",
                "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans TC',sans-serif;line-height:1.65;margin:32px;color:#1f2937;background:#f8fafc}",
                "main{max-width:1180px;margin:0 auto;background:#fff;padding:28px;border:1px solid #e5e7eb;border-radius:8px}",
                "h1,h2,h3{line-height:1.25;color:#111827} table{border-collapse:collapse;width:100%;font-size:14px;margin:12px 0 20px}",
                "th,td{border:1px solid #d1d5db;padding:8px;vertical-align:top} th{background:#f3f4f6;text-align:left}",
                "a{color:#0f766e} code{background:#f3f4f6;padding:2px 4px;border-radius:4px}",
                "</style>",
                "</head>",
                "<body><main>",
                body,
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


def _directional_confidence(direction: str, confidence: float, price_validation: str = "N/A") -> str:
    if direction == "正向":
        return f"+{_market_adjusted_confidence(confidence, price_validation):.2f}"
    if direction == "負向":
        return f"-{_market_adjusted_confidence(confidence, price_validation):.2f}"
    return "0.00"


def _market_adjusted_confidence(confidence: float, price_validation: str) -> float:
    if price_validation == "同向":
        return confidence
    if price_validation == "背離":
        return confidence * 0.50
    if price_validation == "未明確":
        return confidence * 0.75
    return confidence


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
