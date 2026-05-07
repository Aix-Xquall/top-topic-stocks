from __future__ import annotations

import unittest

from market_topics.notification import build_line_message, github_pages_report_url


class LineNotificationTest(unittest.TestCase):
    def test_line_message_limits_topics_and_companies(self) -> None:
        summary = {
            "date": "2026-05-07",
            "topics": [
                {
                    "name": f"topic-{topic_index}",
                    "direction": "正向",
                    "companies": [
                        {
                            "ticker": f"T{company_index}",
                            "name_zh": f"公司{company_index}",
                            "directional_confidence": "+0.90",
                            "return_3d": "+1.00%",
                            "return_5d": "+2.00%",
                            "price_validation": "同向",
                        }
                        for company_index in range(1, 5)
                    ],
                }
                for topic_index in range(1, 5)
            ],
        }

        message = build_line_message(summary, "https://example.com/report.html")

        self.assertIn("每日股市熱門話題分析 - 2026-05-07", message)
        self.assertIn("報告：https://example.com/report.html", message)
        self.assertIn("1. topic-1｜正向", message)
        self.assertIn("3. topic-3｜正向", message)
        self.assertNotIn("4. topic-4｜正向", message)
        self.assertIn("T3 公司3", message)
        self.assertNotIn("T4 公司4", message)

    def test_github_pages_report_url(self) -> None:
        url = github_pages_report_url("octocat", "top-topic-stocks", "2026-05-07")

        self.assertEqual(
            "https://octocat.github.io/top-topic-stocks/reports/2026-05-07-market-topics.html",
            url,
        )


if __name__ == "__main__":
    unittest.main()
