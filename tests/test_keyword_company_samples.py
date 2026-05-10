from __future__ import annotations

import unittest
from datetime import date
from unittest.mock import patch

from market_topics.collectors.prices import PricePerformanceCollector
from market_topics.models import Article, Company, CompanyRelation, Topic
from market_topics.samples import (
    aggregate_keyword_company_stats,
    build_keyword_company_samples,
    upsert_samples,
)


class KeywordCompanySamplesTest(unittest.TestCase):
    def test_upsert_samples_replaces_same_sample_id(self) -> None:
        first = {"sample_id": "abc", "signal_date": "2026-05-01", "confidence": 0.5}
        second = {"sample_id": "abc", "signal_date": "2026-05-01", "confidence": 0.8}

        rows = upsert_samples([first], [second])

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["confidence"], 0.8)

    def test_forward_returns_use_prices_after_signal_date(self) -> None:
        company = Company(
            market="US",
            ticker="ABC",
            name_zh="ABC",
            name_en="ABC",
            aliases=(),
            industry="test",
            tags=(),
        )
        rows = [
            ("2026-05-01", 100.0),
            ("2026-05-04", 101.0),
            ("2026-05-05", 102.0),
            ("2026-05-06", 103.0),
            ("2026-05-07", 104.0),
            ("2026-05-08", 105.0),
        ]
        collector = PricePerformanceCollector([], report_date=date(2026, 5, 1))
        with patch.object(collector, "_collect_yahoo_rows", return_value=rows):
            result = collector.collect_forward_returns(company, "正向", signal_date=date(2026, 5, 1))

        self.assertEqual(result["outcome_status"], "valid")
        self.assertEqual(result["base_date"], "2026-05-01")
        self.assertEqual(result["target_date_3d"], "2026-05-06")
        self.assertAlmostEqual(result["forward_return_3d"], 3.0)
        self.assertAlmostEqual(result["forward_return_5d"], 5.0)

    def test_forward_returns_mark_pending_when_future_prices_are_missing(self) -> None:
        company = Company(
            market="US",
            ticker="ABC",
            name_zh="ABC",
            name_en="ABC",
            aliases=(),
            industry="test",
            tags=(),
        )
        collector = PricePerformanceCollector([], report_date=date(2026, 5, 1))
        with patch.object(collector, "_collect_yahoo_rows", return_value=[("2026-05-01", 100.0), ("2026-05-04", 101.0)]):
            result = collector.collect_forward_returns(company, "正向", signal_date=date(2026, 5, 1))

        self.assertEqual(result["outcome_status"], "pending")
        self.assertIsNone(result["forward_return_5d"])

    def test_copos_topic_generates_keyword_company_sample(self) -> None:
        company = Company(
            market="TW",
            ticker="2330",
            name_zh="台積電",
            name_en="Taiwan Semiconductor Manufacturing",
            aliases=("TSMC", "CoPoS"),
            industry="半導體",
            tags=("CoPoS", "advanced packaging"),
        )
        relation = CompanyRelation(
            company=company,
            relation_type="新聞直接提及",
            reason="TSMC CoPoS",
            confidence=0.9,
            impact_direction="正向",
        )
        topic = Topic(
            name="先進封裝與 CoPoS",
            score=2,
            summary="CoPoS",
            articles=[
                Article(
                    title="TSMC CoPoS pilot line ramps as advanced packaging demand rises",
                    url="https://example.com/copos",
                    source="example",
                )
            ],
            related_companies=[relation],
        )
        with patch(
            "market_topics.collectors.prices.PricePerformanceCollector.collect_forward_returns",
            return_value={
                "outcome_status": "valid",
                "source": "test",
                "base_date": "2026-05-01",
                "target_date_3d": "2026-05-06",
                "target_date_5d": "2026-05-08",
                "forward_return_3d": 2.0,
                "forward_return_5d": 4.0,
            },
        ):
            rows = build_keyword_company_samples(
                topics=[topic],
                topic_keywords={"先進封裝與 CoPoS": ["CoPoS", "advanced packaging"]},
                signal_date=date(2026, 5, 1),
                data_gaps=[],
                article_count=1,
            )

        self.assertTrue(any(row["keyword"] == "CoPoS" and row["ticker"] == "2330" for row in rows))
        copos = next(row for row in rows if row["keyword"] == "CoPoS")
        self.assertEqual(copos["outcome_status"], "valid")
        self.assertEqual(copos["directional_return_5d"], 4.0)

    def test_keyword_company_stats_use_valid_forward_returns_only(self) -> None:
        samples = []
        for index in range(6):
            samples.append(
                {
                    "sample_id": str(index),
                    "signal_date": f"2026-05-0{index + 1}",
                    "keyword": "CoPoS",
                    "topic": "先進封裝與 CoPoS",
                    "ticker": "2330",
                    "relation_type": "新聞直接提及",
                    "confidence": 0.8,
                    "directional_return_3d": 1.0,
                    "directional_return_5d": 2.0,
                    "outcome_status": "valid",
                }
            )
        samples.append({"sample_id": "pending", "keyword": "CoPoS", "ticker": "2330", "outcome_status": "pending"})

        stats = aggregate_keyword_company_stats(samples, end_date=date(2026, 5, 9))

        self.assertEqual(stats["sample_count"], 7)
        self.assertEqual(stats["valid_sample_count"], 6)
        self.assertEqual(stats["pending_sample_count"], 1)
        self.assertIn("CoPoS|2330", stats["groups"]["keyword_ticker"])
        self.assertGreater(stats["groups"]["keyword_ticker"]["CoPoS|2330"]["edge_score_5d"], 50)


if __name__ == "__main__":
    unittest.main()
