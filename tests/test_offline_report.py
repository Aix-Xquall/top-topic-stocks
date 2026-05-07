from __future__ import annotations

import unittest
from datetime import date
from pathlib import Path

from market_topics.cli import run_report


class OfflineReportTest(unittest.TestCase):
    def test_offline_report_outputs_chinese_markdown_and_html(self) -> None:
        output_dir = Path("reports") / "_test_output"
        result = run_report(
            report_date=date(2026, 5, 7),
            config_dir=Path("config"),
            reports_dir=output_dir,
            offline_sample=True,
            max_topics=5,
            max_companies=4,
        )
        markdown = Path(result.output_markdown).read_text(encoding="utf-8")
        html = Path(result.output_html).read_text(encoding="utf-8")

        self.assertIn("每日股市熱門話題分析 - 2026-05-07", markdown)
        self.assertIn("重點摘要", markdown)
        self.assertIn("市場驗證", markdown)
        self.assertIn("相關公司", markdown)
        self.assertIn("新聞直接提及", markdown)
        self.assertIn('<html lang="zh-Hant">', html)
        self.assertIn('<meta charset="utf-8">', html)

    def test_report_survives_missing_api_keys(self) -> None:
        output_dir = Path("reports") / "_test_output"
        result = run_report(
            report_date=date(2026, 5, 7),
            config_dir=Path("config"),
            reports_dir=output_dir,
            offline_sample=True,
            max_topics=2,
            max_companies=2,
        )
        joined_gaps = "\n".join(result.data_gaps)
        self.assertIn("使用離線樣本新聞", joined_gaps)
        self.assertTrue(Path(result.output_markdown).exists())
        self.assertTrue(Path(result.output_html).exists())


if __name__ == "__main__":
    unittest.main()
