from __future__ import annotations

import json
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from market_topics.backtesting import adjust_model_weights, normalize_backtest_days, run_backtest
from market_topics.collectors.news import NewsCollector
from market_topics.models import PricePerformance


class BacktestingTest(unittest.TestCase):
    def test_google_news_historical_query_uses_date_range(self) -> None:
        captured: dict[str, str] = {}

        def fake_get_text(url: str, headers=None):
            captured.setdefault("url", url)
            return """<?xml version="1.0" encoding="UTF-8" ?>
<rss><channel>
<item><title>台積電 AI 新聞</title><link>https://example.com/a</link><pubDate>Thu, 07 May 2026 08:00:00 GMT</pubDate><description>半導體</description></item>
</channel></rss>"""

        with patch("market_topics.collectors.news.get_text", fake_get_text):
            articles = NewsCollector([], []).collect_historical(date(2026, 5, 7))

        self.assertIn("after%3A2026-05-07", captured["url"])
        self.assertIn("before%3A2026-05-08", captured["url"])
        self.assertEqual(len(articles), 1)

    def test_gdelt_historical_query_uses_start_and_end_datetime(self) -> None:
        captured: dict[str, str] = {}

        def fake_get_json(url: str, headers=None):
            captured["url"] = url
            return {"articles": []}

        with patch("market_topics.collectors.news.get_text", return_value="<rss><channel></channel></rss>"):
            with patch("market_topics.collectors.news.get_json", fake_get_json):
                NewsCollector([], []).collect_historical(date(2026, 5, 7))

        self.assertIn("startdatetime=20260507000000", captured["url"])
        self.assertIn("enddatetime=20260508000000", captured["url"])
        self.assertNotIn("timespan=1d", captured["url"])

    def test_low_sample_backtest_does_not_update_weights(self) -> None:
        adjustment = adjust_model_weights(
            {"direct_mention_weight": 1.0, "inferred_supply_chain_weight": 0.65},
            {"days": 5, "minimum_required_samples": 15, "sample_count_3d": 10, "correlation_3d": 0.5},
        )

        self.assertFalse(adjustment["updated"])

    def test_weight_adjustment_is_capped_and_inferred_never_exceeds_direct(self) -> None:
        weights = {
            "news_heat_weight": 1.0,
            "current_market_confirmation_weight": 1.0,
            "historical_topic_score_weight": 1.0,
            "direct_mention_weight": 0.8,
            "inferred_supply_chain_weight": 0.8,
            "broad_topic_penalty": 0.8,
            "price_divergence_penalty": 0.5,
        }
        adjustment = adjust_model_weights(
            weights,
            {"days": 5, "minimum_required_samples": 15, "sample_count_3d": 80, "correlation_3d": 0.0},
        )

        self.assertTrue(adjustment["updated"])
        after = adjustment["weights_after"]
        self.assertLessEqual(after["current_market_confirmation_weight"], 1.1)
        self.assertLessEqual(after["inferred_supply_chain_weight"], after["direct_mention_weight"])

    def test_backtest_days_are_limited_to_three_to_five_days(self) -> None:
        self.assertEqual(normalize_backtest_days(1), 3)
        self.assertEqual(normalize_backtest_days(4), 4)
        self.assertEqual(normalize_backtest_days(30), 5)

    def test_run_backtest_outputs_json_and_html_without_network_news(self) -> None:
        reports_dir = Path("reports") / "_test_output" / "backtest_case"

        def fake_price(self, company, direction):
            return PricePerformance(
                return_3d="+2.00%" if direction != "負向" else "-2.00%",
                return_5d="+3.00%" if direction != "負向" else "-3.00%",
                validation="同向" if direction != "中性" else "不適用",
                source="test",
            )

        with patch("market_topics.collectors.prices.PricePerformanceCollector.collect_for_company", fake_price):
            json_path, html_path = run_backtest(
                days=2,
                end_date=date(2026, 5, 7),
                config_dir=Path("config"),
                reports_dir=reports_dir,
                offline_sample=True,
                max_topics=3,
                max_companies=3,
            )

        payload = json.loads(json_path.read_text(encoding="utf-8"))
        self.assertTrue(json_path.exists())
        self.assertTrue(html_path.exists())
        self.assertIn("aggregate", payload)
        self.assertIn("weight_adjustment", payload)


if __name__ == "__main__":
    unittest.main()
