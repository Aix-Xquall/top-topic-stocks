from __future__ import annotations

import unittest

from market_topics.analysis.topics import TopicAnalyzer
from market_topics.models import Article, Company


class SentimentDirectionTest(unittest.TestCase):
    def test_thermal_supplier_can_be_negative_when_news_is_negative(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "散熱與液冷供應鏈": ["散熱", "均熱片", "奇鋐", "Rubin"],
            },
            sentiment_keywords={
                "positive": ["受惠", "成長"],
                "negative": ["改單片", "單價縮水", "跌停", "低於預期"],
            },
            companies=[
                Company(
                    market="TW",
                    ticker="3017",
                    name_zh="奇鋐",
                    name_en="AVC",
                    aliases=("AVC",),
                    industry="散熱",
                    tags=("散熱", "AI server"),
                )
            ],
        )

        topics = analyzer.analyze(
            [
                Article(
                    title="散熱股重挫，輝達 Rubin 均熱片傳改單片，奇鋐跌停",
                    url="https://example.com/negative-cooling",
                    source="sample",
                    summary="市場擔心單價縮水，相關供應鏈拉貨低於預期。",
                )
            ]
        )

        relation = topics[0].related_companies[0]
        self.assertEqual(topics[0].direction, "負向")
        self.assertEqual(relation.company.ticker, "3017")
        self.assertEqual(relation.impact_direction, "負向")
        self.assertLess(relation.impact_score, 0)

    def test_inferred_company_without_relevant_article_stays_neutral(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "AI 伺服器與資料中心": ["AI", "AI server", "datacenter", "server"],
            },
            sentiment_keywords={
                "positive": ["buoy"],
                "negative": ["跌停"],
            },
            companies=[
                Company(
                    market="TW",
                    ticker="3017",
                    name_zh="奇鋐",
                    name_en="AVC",
                    aliases=("AVC",),
                    industry="散熱",
                    tags=("AI server", "datacenter", "server"),
                )
            ],
        )

        topics = analyzer.analyze(
            [
                Article(
                    title="AI outlooks buoy stock markets",
                    url="https://example.com/ai",
                    source="sample",
                    summary="The article discusses broad market sentiment.",
                )
            ]
        )

        self.assertEqual(topics[0].direction, "正向")
        self.assertEqual(topics[0].related_companies[0].impact_direction, "中性")


if __name__ == "__main__":
    unittest.main()
