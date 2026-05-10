from __future__ import annotations

import json
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

from market_topics.backtesting import aggregate_backtest, adjust_model_weights, normalize_backtest_days, run_backtest
from market_topics.collectors.news import DEFAULT_SOURCE_TIERS, NewsCollector
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

    def test_current_news_uses_google_source_discovery_when_rss_is_empty(self) -> None:
        captured: dict[str, str] = {}

        def fake_get_text(url: str, headers=None):
            captured.setdefault("url", url)
            return """<?xml version="1.0" encoding="UTF-8" ?>
<rss><channel>
<item><title>CoPoS packaging becomes market focus</title><link>https://example.com/copos</link><pubDate>Fri, 08 May 2026 08:00:00 GMT</pubDate><description>TSMC advanced packaging demand.</description></item>
</channel></rss>"""

        with patch("market_topics.collectors.news.get_text", fake_get_text):
            articles = NewsCollector([], []).collect(date(2026, 5, 8), max_articles=10)

        self.assertIn("news.google.com", captured["url"])
        self.assertIn("site%3Amops.twse.com.tw", captured["url"])
        self.assertEqual(len(articles), 1)

    def test_source_discovery_includes_recommended_financial_sources(self) -> None:
        domains = {str(item["domain"]) for item in DEFAULT_SOURCE_TIERS}

        self.assertIn("cna.com.tw", domains)
        self.assertIn("ctee.com.tw", domains)
        self.assertIn("technews.tw", domains)
        self.assertIn("reuters.com", domains)
        self.assertIn("cnbc.com", domains)
        self.assertIn("nasdaq.com", domains)
        self.assertIn("investing.com", domains)

    def test_source_discovery_tags_article_source_tier(self) -> None:
        def fake_get_text(url: str, headers=None):
            return """<?xml version="1.0" encoding="UTF-8" ?>
<rss><channel>
<item><title>CoPoS packaging becomes market focus</title><link>https://example.com/copos</link><pubDate>Fri, 08 May 2026 08:00:00 GMT</pubDate><description>TSMC advanced packaging demand.</description></item>
</channel></rss>"""

        with patch("market_topics.collectors.news.get_text", fake_get_text):
            articles = NewsCollector([], []).collect(date(2026, 5, 8), max_articles=10)

        self.assertIn("來源層級", articles[0].summary)
        self.assertIn("來源權重", articles[0].summary)

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
            "keyword_company_score_weight": 0.2,
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
        self.assertLessEqual(after["keyword_company_score_weight"], 0.22)

    def test_keyword_company_learning_adjusts_weight_only_with_enough_samples(self) -> None:
        weights = {
            "news_heat_weight": 1.0,
            "current_market_confirmation_weight": 0.65,
            "historical_topic_score_weight": 0.35,
            "keyword_company_score_weight": 0.2,
            "direct_mention_weight": 0.95,
            "inferred_supply_chain_weight": 0.65,
            "broad_topic_penalty": 0.75,
            "price_divergence_penalty": 0.5,
        }
        adjustment = adjust_model_weights(
            weights,
            {
                "days": 5,
                "minimum_required_samples": 15,
                "sample_count_3d": 80,
                "correlation_3d": 0.25,
                "keyword_company_learning": {"valid_sample_count": 40, "hit_rate_5d": 0.62},
            },
        )

        self.assertTrue(adjustment["updated"])
        self.assertEqual(adjustment["weights_after"]["keyword_company_score_weight"], 0.22)

    def test_high_direction_accuracy_negative_correlation_triggers_confidence_calibration(self) -> None:
        weights = {
            "news_heat_weight": 1.0,
            "current_market_confirmation_weight": 0.65,
            "historical_topic_score_weight": 0.35,
            "direct_mention_weight": 0.95,
            "inferred_supply_chain_weight": 0.65,
            "broad_topic_penalty": 0.75,
            "price_divergence_penalty": 0.5,
        }
        adjustment = adjust_model_weights(
            weights,
            {
                "days": 5,
                "minimum_required_samples": 15,
                "sample_count_3d": 45,
                "correlation_3d": -0.3707,
                "aligned_ratio": 0.8889,
                "direction_accuracy": 0.8889,
            },
        )

        self.assertTrue(adjustment["updated"])
        self.assertEqual(adjustment["strategy"], "信心校準問題")
        self.assertEqual(adjustment["weights_after"]["direct_mention_weight"], weights["direct_mention_weight"])
        self.assertLess(adjustment["weights_after"]["inferred_supply_chain_weight"], weights["inferred_supply_chain_weight"])
        self.assertLess(adjustment["weights_after"]["broad_topic_penalty"], weights["broad_topic_penalty"])

    def test_low_direction_accuracy_negative_correlation_lowers_direct_weight(self) -> None:
        weights = {
            "news_heat_weight": 1.0,
            "current_market_confirmation_weight": 0.65,
            "historical_topic_score_weight": 0.35,
            "direct_mention_weight": 0.95,
            "inferred_supply_chain_weight": 0.65,
            "broad_topic_penalty": 0.75,
            "price_divergence_penalty": 0.5,
        }
        adjustment = adjust_model_weights(
            weights,
            {
                "days": 5,
                "minimum_required_samples": 15,
                "sample_count_3d": 45,
                "correlation_3d": -0.3707,
                "aligned_ratio": 0.4,
                "direction_accuracy": 0.4,
            },
        )

        self.assertEqual(adjustment["strategy"], "方向與信心皆需修正")
        self.assertLess(adjustment["weights_after"]["direct_mention_weight"], weights["direct_mention_weight"])

    def test_aggregate_reports_confidence_diagnostics_and_misses(self) -> None:
        aggregate = aggregate_backtest(
            [
                {
                    "date": "2026-05-07",
                    "low_confidence": False,
                    "validation": {
                        "validated_count": 2,
                        "aligned_count": 2,
                        "diverged_count": 0,
                        "sample_count_3d": 2,
                        "sample_count_5d": 2,
                        "correlation_3d": -0.5,
                        "correlation_5d": -0.4,
                        "topics": [{"topic": "記憶體與 HBM 供應鏈", "market_confirmation_score": 80}],
                    },
                    "relation_stats": {"新聞直接提及": {"validated": 1, "aligned": 1, "diverged": 0}},
                    "keyword_returns": {"記憶體與 HBM 供應鏈": [2.0, -1.0]},
                    "relations": [
                        {
                            "topic": "記憶體與 HBM 供應鏈",
                            "ticker": "ABC",
                            "name_zh": "測試公司",
                            "relation_type": "新聞直接提及",
                            "impact_direction": "正向",
                            "confidence": 0.91,
                            "return_3d": "-2.00%",
                            "return_5d": "-1.00%",
                            "directional_return_3d": -2.0,
                            "price_validation": "背離",
                        }
                    ],
                }
            ]
        )

        self.assertEqual(aggregate["direction_accuracy"], 1.0)
        self.assertEqual(aggregate["confidence_calibration"], -0.5)
        self.assertEqual(aggregate["calibration_strategy"], "信心校準問題")
        self.assertEqual(aggregate["overconfident_misses"][0]["ticker"], "ABC")

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

        fake_forward = {
            "outcome_status": "valid",
            "source": "test",
            "base_date": "2026-05-07",
            "target_date_3d": "2026-05-12",
            "target_date_5d": "2026-05-14",
            "forward_return_3d": 2.0,
            "forward_return_5d": 3.0,
        }
        with patch("market_topics.collectors.prices.PricePerformanceCollector.collect_for_company", fake_price):
            with patch(
                "market_topics.collectors.prices.PricePerformanceCollector.collect_forward_returns",
                return_value=fake_forward,
            ):
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
        self.assertIn("keyword_company_learning", payload["aggregate"])


if __name__ == "__main__":
    unittest.main()
