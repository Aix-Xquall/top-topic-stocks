from __future__ import annotations

import unittest
from datetime import date

from market_topics.analysis.validation import daily_market_validation, topic_market_validation
from market_topics.models import Company, CompanyRelation, PricePerformance, Topic
from market_topics.reporting.renderer import ReportRenderer


class MarketValidationTest(unittest.TestCase):
    def test_topic_validation_scores_directional_returns(self) -> None:
        topic = Topic(
            name="記憶體與 HBM 供應鏈",
            score=3,
            summary="測試",
            articles=[],
            related_companies=[
                _relation("MU", "正向", "+10.00%", "同向"),
                _relation("SNDK", "正向", "+4.00%", "同向"),
                _relation("3017", "負向", "-3.00%", "同向"),
                _relation("NVDA", "負向", "+2.00%", "背離"),
            ],
        )

        validation = topic_market_validation(topic)

        self.assertEqual(validation["validated_count"], 4)
        self.assertEqual(validation["aligned_count"], 3)
        self.assertEqual(validation["diverged_count"], 1)
        self.assertGreater(validation["avg_directional_return_3d"], 0)
        self.assertGreater(validation["market_confirmation_score"], 50)

    def test_daily_validation_outputs_correlation_fields(self) -> None:
        topic = Topic(
            name="測試題材",
            score=4,
            summary="測試",
            articles=[],
            related_companies=[
                _relation("A", "正向", "+5.00%", "同向", confidence=0.90),
                _relation("B", "正向", "+2.00%", "同向", confidence=0.70),
                _relation("C", "負向", "-4.00%", "同向", confidence=0.80),
                _relation("D", "負向", "+3.00%", "背離", confidence=0.60),
            ],
        )

        validation = daily_market_validation([topic])

        self.assertEqual(validation["sample_count_3d"], 4)
        self.assertIn("correlation_3d", validation)
        self.assertEqual(len(validation["topics"]), 1)

    def test_html_contains_market_confirmation_chart_when_prices_exist(self) -> None:
        topic = Topic(
            name="測試題材",
            score=1,
            summary="測試",
            articles=[],
            related_companies=[_relation("A", "正向", "+5.00%", "同向")],
        )
        renderer = ReportRenderer()
        markdown = renderer.render_markdown(date(2026, 5, 7), [topic], [])
        html = renderer.render_html(markdown, [topic])

        self.assertIn("市場確認圖表", html)
        self.assertIn("bar-row", html)


def _relation(
    ticker: str,
    direction: str,
    return_3d: str,
    validation: str,
    confidence: float = 0.80,
) -> CompanyRelation:
    company = Company(
        market="US",
        ticker=ticker,
        name_zh=ticker,
        name_en=ticker,
        aliases=(),
        industry="測試",
        tags=(),
    )
    relation = CompanyRelation(
        company=company,
        relation_type="新聞直接提及",
        reason="測試",
        confidence=confidence,
        impact_direction=direction,
    )
    relation.price_performance = PricePerformance(
        return_3d=return_3d,
        return_5d=return_3d,
        validation=validation,
        source="測試",
    )
    return relation


if __name__ == "__main__":
    unittest.main()
