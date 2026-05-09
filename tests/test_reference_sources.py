from __future__ import annotations

import unittest
from pathlib import Path

from market_topics.config import load_reference_sources, load_rss_feeds
from market_topics.reporting.renderer import ReportRenderer


class ReferenceSourcesTest(unittest.TestCase):
    def test_reference_sources_include_requested_platforms(self) -> None:
        names = {item["name"] for item in load_reference_sources(Path("config"))}

        self.assertIn("公開資訊觀測站 MOPS", names)
        self.assertIn("臺灣證券交易所 TWSE", names)
        self.assertIn("櫃買中心 TPEx", names)
        self.assertIn("Yahoo 奇摩股市", names)
        self.assertIn("鉅亨網", names)
        self.assertIn("MoneyDJ", names)
        self.assertIn("經濟日報 money", names)
        self.assertIn("中央社財經", names)
        self.assertIn("TechNews 科技新報", names)
        self.assertIn("Reuters Markets", names)

    def test_unstable_old_rss_feeds_are_removed(self) -> None:
        feeds = "\n".join(load_rss_feeds(Path("config")))

        self.assertNotIn("marketwatch.com", feeds)
        self.assertNotIn("feeds.a.dj.com", feeds)
        self.assertIn("tw.stock.yahoo.com/rss", feeds)
        self.assertIn("cnyes.com", feeds)

    def test_report_renders_reference_sources(self) -> None:
        markdown = ReportRenderer().render_markdown(
            report_date=__import__("datetime").date(2026, 5, 7),
            topics=[],
            data_gaps=[],
            reference_sources=load_reference_sources(Path("config")),
        )

        self.assertIn("## 參考來源", markdown)
        self.assertIn("Yahoo 奇摩股市", markdown)


if __name__ == "__main__":
    unittest.main()
