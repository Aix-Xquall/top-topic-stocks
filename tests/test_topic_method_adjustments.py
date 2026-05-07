from __future__ import annotations

import unittest

from market_topics.analysis.topics import TopicAnalyzer
from market_topics.models import Article, Company


class TopicMethodAdjustmentsTest(unittest.TestCase):
    def test_broad_ai_tags_keep_microsoft_inferred_confidence_low(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "AI 伺服器與資料中心": ["AI", "datacenter"],
            },
            sentiment_keywords={"positive": ["rally"], "negative": []},
            companies=[
                Company(
                    market="US",
                    ticker="MSFT",
                    name_zh="微軟",
                    name_en="Microsoft",
                    aliases=("Microsoft",),
                    industry="雲端軟體",
                    tags=("AI", "cloud", "datacenter"),
                )
            ],
        )

        topics = analyzer.analyze(
            [
                Article(
                    title="AI chip stocks extend rally",
                    url="https://example.com/ai",
                    source="sample",
                    summary="Datacenter hardware demand remains strong.",
                )
            ]
        )

        relation = topics[0].related_companies[0]
        self.assertEqual(relation.company.ticker, "MSFT")
        self.assertLessEqual(relation.confidence, 0.42)

    def test_memory_topic_ranks_memory_company_above_nvidia_consumer_link(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "記憶體與 HBM 供應鏈": ["memory", "HBM", "Micron", "MU"],
            },
            sentiment_keywords={"positive": ["surge", "strong", "record highs"], "negative": ["risk"]},
            companies=[
                Company(
                    market="US",
                    ticker="MU",
                    name_zh="美光",
                    name_en="Micron Technology",
                    aliases=("Micron", "MU"),
                    industry="記憶體",
                    tags=("memory", "HBM", "DRAM", "NAND"),
                ),
                Company(
                    market="US",
                    ticker="NVDA",
                    name_zh="輝達",
                    name_en="NVIDIA",
                    aliases=("Nvidia",),
                    industry="半導體",
                    tags=("AI", "GPU", "HBM"),
                ),
            ],
        )

        topics = analyzer.analyze(
            [
                Article(
                    title="Micron MU stock surges as HBM memory demand stays strong",
                    url="https://example.com/mu",
                    source="sample",
                    summary="AI memory remains tight.",
                )
            ]
        )

        relations = topics[0].related_companies
        self.assertEqual(relations[0].company.ticker, "MU")
        self.assertGreater(relations[0].confidence, relations[1].confidence)
        self.assertEqual(relations[0].impact_direction, "正向")

    def test_specialized_memory_topic_does_not_inflate_broad_ai_topic(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "AI 伺服器與資料中心": ["AI"],
                "記憶體與 HBM 供應鏈": ["Micron", "HBM", "memory"],
            },
            companies=[],
        )

        topics = analyzer.analyze(
            [
                Article(
                    title="Micron rallies as HBM memory demand rises for AI",
                    url="https://example.com/memory",
                    source="sample",
                )
            ]
        )

        topic_names = [topic.name for topic in topics]
        self.assertIn("記憶體與 HBM 供應鏈", topic_names)
        self.assertNotIn("AI 伺服器與資料中心", topic_names)


if __name__ == "__main__":
    unittest.main()
