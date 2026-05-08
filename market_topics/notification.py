from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


LINE_PUSH_URL = "https://api.line.me/v2/bot/message/push"


def summary_path_for_date(reports_dir: Path, report_date: str) -> Path:
    return reports_dir / f"{report_date}-market-topics.json"


def github_pages_report_url(github_user: str, repo: str, report_date: str) -> str:
    user = github_user.strip().strip("/")
    repo_name = repo.strip().strip("/")
    return f"https://{user}.github.io/{repo_name}/reports/{report_date}-market-topics.html"


def build_line_message(summary: dict[str, Any], report_url: str) -> str:
    report_date = str(summary.get("date", ""))
    lines = [
        f"每日股市熱門話題分析 - {report_date}",
        f"報告：{report_url}",
    ]
    backtest = summary.get("backtest_summary", {})
    if backtest:
        days = int(backtest.get("days", 5) or 5)
        aligned_ratio = backtest.get("aligned_ratio")
        aligned_text = "N/A" if aligned_ratio is None else f"{float(aligned_ratio) * 100:.0f}%"
        correlation = backtest.get("correlation_3d")
        correlation_text = "N/A" if correlation is None else f"{float(correlation):+.2f}"
        updated_text = "已調整" if backtest.get("updated") else "未調整"
        lines.append(f"近{days}日驗證：3日相關 {correlation_text}，同向 {aligned_text}，權重{updated_text}")
    lines.append("")

    for index, topic in enumerate(summary.get("topics", [])[:3], start=1):
        topic_name = topic.get("name", "N/A")
        direction = topic.get("direction", "N/A")
        lines.append(f"{index}. {topic_name}｜{direction}")
        companies = topic.get("companies", [])[:3]
        if not companies:
            lines.append("- 無相關公司")
            lines.append("")
            continue
        for company in companies:
            lines.append(
                "- "
                + f"{company.get('ticker', 'N/A')} {company.get('name_zh', '')}："
                + f"{company.get('directional_confidence', '0.00')}，"
                + f"3日 {company.get('return_3d', 'N/A')}，"
                + f"5日 {company.get('return_5d', 'N/A')}，"
                + f"{company.get('price_validation', 'N/A')}"
            )
        lines.append("")

    return "\n".join(lines).strip()


def load_summary(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def send_line_message(message: str, token: str, to: str) -> None:
    payload = {
        "to": to,
        "messages": [{"type": "text", "text": message}],
    }
    request = urllib.request.Request(
        LINE_PUSH_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status < 200 or response.status >= 300:
                raise RuntimeError(f"LINE push failed with HTTP {response.status}")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"LINE push failed with HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"LINE push failed: {exc}") from exc


def notify_from_summary(summary_path: Path, report_url: str) -> str:
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    to = os.getenv("LINE_TO", "").strip()
    summary = load_summary(summary_path)
    message = build_line_message(summary, report_url)
    if not token or not to:
        return "LINE secrets are missing; skipped notification."
    send_line_message(message, token=token, to=to)
    return "LINE notification sent."
