from __future__ import annotations

import unittest

from market_topics.models import Company, CompanyRelation, Topic
from market_topics.reporting.renderer import ReportRenderer


class ReportDirectionalConfidenceTest(unittest.TestCase):
    def test_table_uses_directional_confidence_column(self) -> None:
        company = Company(
            market="TW",
            ticker="3017",
            name_zh="奇鋐",
            name_en="AVC",
            aliases=(),
            industry="散熱",
            tags=(),
        )
        topic = Topic(
            name="散熱與液冷供應鏈",
            score=1,
            summary="測試",
            articles=[],
            direction="負向",
            sentiment_score=-1,
            related_companies=[
                CompanyRelation(
                    company=company,
                    relation_type="新聞直接提及",
                    reason="測試",
                    confidence=0.95,
                    impact_direction="負向",
                    impact_score=-1,
                )
            ],
        )

        markdown = ReportRenderer().render_markdown(
            report_date=__import__("datetime").date(2026, 5, 7),
            topics=[topic],
            data_gaps=[],
        )

        self.assertIn("方向性信心", markdown)
        self.assertNotIn("影響方向", markdown)
        self.assertNotIn("信心分數", markdown)
        self.assertIn("| TW | 3017 | 奇鋐 / AVC | 新聞直接提及 | -0.95 | N/A | N/A | N/A |", markdown)

    def test_diverging_price_validation_dampens_directional_confidence(self) -> None:
        company = Company(
            market="US",
            ticker="NVDA",
            name_zh="輝達",
            name_en="NVIDIA",
            aliases=(),
            industry="半導體",
            tags=(),
        )
        relation = CompanyRelation(
            company=company,
            relation_type="新聞直接提及",
            reason="測試",
            confidence=0.90,
            impact_direction="負向",
        )
        relation.price_performance.validation = "背離"
        topic = Topic(
            name="散熱與液冷供應鏈",
            score=1,
            summary="測試",
            articles=[],
            related_companies=[relation],
        )

        markdown = ReportRenderer().render_markdown(
            report_date=__import__("datetime").date(2026, 5, 7),
            topics=[topic],
            data_gaps=[],
        )

        self.assertIn("| US | NVDA | 輝達 / NVIDIA | 新聞直接提及 | -0.45 |", markdown)


if __name__ == "__main__":
    unittest.main()
