from __future__ import annotations

import unittest

from market_topics.analysis.topics import TopicAnalyzer
from market_topics.models import Article, Company


class ConfidenceScoringTest(unittest.TestCase):
    def test_confidence_scores_are_differentiated_by_evidence_strength(self) -> None:
        analyzer = TopicAnalyzer(
            topic_keywords={
                "AI 伺服器與資料中心": ["AI", "AI server", "GPU", "datacenter"],
            },
            companies=[
                Company(
                    market="US",
                    ticker="NVDA",
                    name_zh="輝達",
                    name_en="NVIDIA",
                    aliases=("Nvidia",),
                    industry="半導體",
                    tags=("AI", "AI server", "GPU", "datacenter"),
                ),
                Company(
                    market="TW",
                    ticker="6669",
                    name_zh="緯穎",
                    name_en="Wiwynn",
                    aliases=("server",),
                    industry="伺服器",
                    tags=("AI server", "datacenter"),
                ),
                Company(
                    market="TW",
                    ticker="2454",
                    name_zh="聯發科",
                    name_en="MediaTek",
                    aliases=("MediaTek",),
                    industry="IC 設計",
                    tags=("AI",),
                ),
            ],
        )
        topics = analyzer.analyze(
            [
                Article(
                    title="Nvidia rises as AI server GPU demand expands",
                    url="https://example.com/1",
                    source="sample",
                    summary="Datacenter spending increases.",
                ),
                Article(
                    title="AI server suppliers benefit from datacenter upgrades",
                    url="https://example.com/2",
                    source="sample",
                    summary="GPU and server demand remain strong.",
                ),
            ]
        )

        relations = topics[0].related_companies
        scores = {relation.company.ticker: relation.confidence for relation in relations}

        self.assertGreater(scores["NVDA"], scores["6669"])
        self.assertGreater(scores["6669"], scores["2454"])
        self.assertGreater(len(set(scores.values())), 1)


if __name__ == "__main__":
    unittest.main()

