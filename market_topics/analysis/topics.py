from __future__ import annotations

import re
from collections import defaultdict

from ..models import Article, Company, CompanyRelation, Topic


GENERIC_DIRECT_ALIAS_DENYLIST = {
    "ai",
    "ai server",
    "asic",
    "battery",
    "chip",
    "cowos",
    "datacenter",
    "data center",
    "electric vehicle",
    "ev",
    "gpu",
    "hardware",
    "hbm",
    "semiconductor",
    "server",
    "smartphone",
    "supply chain",
    "advanced packaging",
    "晶片",
    "半導體",
    "伺服器",
    "手機",
    "電動車",
    "電池",
    "供應鏈",
    "先進封裝",
    "晶圓代工",
}


BROAD_INFERENCE_TAGS = {
    "ai",
    "artificial intelligence",
    "ai server",
    "cloud",
    "datacenter",
    "data center",
    "hardware",
    "semiconductor",
    "chip",
    "server",
    "supply chain",
    "advanced packaging",
    "hbm",
    "資料中心",
    "雲端伺服器",
    "半導體",
    "晶片",
    "伺服器",
    "供應鏈",
    "先進封裝",
}


BROAD_TOPICS = {
    "AI 伺服器與資料中心",
    "半導體與晶片供應鏈",
    "綜合市場情緒",
}


class TopicAnalyzer:
    def __init__(
        self,
        topic_keywords: dict[str, list[str]],
        companies: list[Company],
        sentiment_keywords: dict[str, list[str]] | None = None,
    ) -> None:
        self.topic_keywords = topic_keywords
        self.companies = companies
        self.sentiment_keywords = sentiment_keywords or {"positive": [], "negative": []}

    def analyze(
        self,
        articles: list[Article],
        max_topics: int = 8,
        max_companies_per_topic: int = 8,
    ) -> list[Topic]:
        topic_articles = self._group_articles_by_topic(articles)
        scored_topics: list[Topic] = []
        for name, items in topic_articles.items():
            if not items:
                continue
            sentiment_score, _ = _sentiment_signal(
                " ".join(_article_text(article) for article in items),
                self.sentiment_keywords,
            )
            scored_topics.append(
                Topic(
                    name=name,
                    score=len(items),
                    summary=self._summarize_topic(name, items),
                    articles=items[:6],
                    direction=_direction_label(sentiment_score),
                    sentiment_score=sentiment_score,
                )
            )
        scored_topics.sort(key=lambda topic: topic.score, reverse=True)
        for topic in scored_topics[:max_topics]:
            topic.related_companies = self._related_companies(topic, max_companies_per_topic)
        return scored_topics[:max_topics]

    def _group_articles_by_topic(self, articles: list[Article]) -> dict[str, list[Article]]:
        grouped: dict[str, list[Article]] = defaultdict(list)
        for article in articles:
            text = _article_text(article)
            matched_topics: list[str] = []
            for topic, keywords in self.topic_keywords.items():
                if any(_contains_keyword(text, keyword) for keyword in keywords):
                    matched_topics.append(topic)
            if not matched_topics:
                grouped["綜合市場情緒"].append(article)
                continue
            specialized_topics = [topic for topic in matched_topics if topic not in BROAD_TOPICS]
            selected_topics = specialized_topics or matched_topics
            for topic in selected_topics:
                grouped[topic].append(article)
        return grouped

    def _summarize_topic(self, topic_name: str, articles: list[Article]) -> str:
        titles = [article.title for article in articles[:3]]
        if not titles:
            return f"{topic_name} 相關新聞量增加，但目前缺少可摘要標題。"
        joined = "；".join(titles)
        return f"{topic_name} 相關新聞集中在：{joined}"

    def _related_companies(self, topic: Topic, limit: int) -> list[CompanyRelation]:
        topic_keywords = self.topic_keywords.get(topic.name, [])
        candidates: list[tuple[float, int, int, CompanyRelation]] = []

        for company in self.companies:
            tag_overlap = _matching_tags(company.tags, topic_keywords)
            direct_hits, title_hits, aliases = _direct_alias_hits(topic.articles, company)
            tag_article_hits = _tag_article_hits(topic.articles, tag_overlap)
            relevant_articles = _relevant_articles(topic.articles, company, tag_overlap, direct_hits > 0)
            impact_score, impact_terms = _sentiment_signal(
                " ".join(_article_text(article) for article in relevant_articles),
                self.sentiment_keywords,
            )
            if impact_score == 0 and (direct_hits or tag_article_hits):
                impact_score = topic.sentiment_score
            impact_direction = _direction_label(impact_score)

            if not direct_hits and not tag_overlap:
                continue

            if direct_hits:
                confidence = _direct_confidence(direct_hits, title_hits, len(tag_overlap), tag_article_hits)
                alias_text = "、".join(aliases[:3])
                reason = f"新聞直接提及「{alias_text}」，共 {direct_hits} 篇新聞命中。"
                if tag_overlap:
                    reason += f" 同時符合主題標籤：{', '.join(tag_overlap[:4])}。"
                relation_type = "新聞直接提及"
            else:
                specific_overlap_count = _specific_overlap_count(tag_overlap)
                confidence = _inferred_confidence(
                    len(tag_overlap),
                    tag_article_hits,
                    topic.score,
                    specific_overlap_count,
                )
                reason = (
                    f"產業/供應鏈推估：公司標籤符合「{topic.name}」關鍵字 "
                    f"{', '.join(tag_overlap[:4])}；其中 {tag_article_hits} 篇新聞出現相關標籤。"
                )
                relation_type = "產業/供應鏈推估"
            if impact_terms:
                reason += f" 方向判斷命中詞：{', '.join(impact_terms[:5])}。"

            candidates.append(
                (
                    confidence,
                    direct_hits,
                    len(tag_overlap),
                    CompanyRelation(
                        company=company,
                        relation_type=relation_type,
                        reason=reason,
                        confidence=round(confidence, 2),
                        impact_direction=impact_direction,
                        impact_score=impact_score,
                    ),
                )
            )

        candidates.sort(key=lambda item: (item[0], item[1], item[2]), reverse=True)
        return [candidate[-1] for candidate in candidates[:limit]]


def _article_text(article: Article) -> str:
    return f"{article.title} {article.summary}".lower()


def _contains_keyword(text: str, keyword: str) -> bool:
    keyword_lower = keyword.lower()
    if re.search(r"[a-zA-Z0-9]", keyword_lower):
        return re.search(rf"\b{re.escape(keyword_lower)}\b", text) is not None
    return keyword_lower in text


def _matched_alias(text: str, company: Company) -> str:
    aliases = [company.ticker, company.name_zh, company.name_en, *company.aliases]
    for alias in aliases:
        if alias and alias.lower() not in GENERIC_DIRECT_ALIAS_DENYLIST and _contains_keyword(text, alias):
            return alias
    return ""


def _matching_tags(company_tags: tuple[str, ...], topic_keywords: list[str]) -> list[str]:
    keyword_by_lower = {keyword.lower(): keyword for keyword in topic_keywords}
    matches: list[str] = []
    for tag in company_tags:
        if tag.lower() in keyword_by_lower:
            matches.append(tag)
    return matches


def _direct_alias_hits(articles: list[Article], company: Company) -> tuple[int, int, list[str]]:
    direct_hits = 0
    title_hits = 0
    aliases: list[str] = []
    for article in articles:
        article_alias = _matched_alias(_article_text(article), company)
        if not article_alias:
            continue
        direct_hits += 1
        aliases.append(article_alias)
        if _matched_alias(article.title.lower(), company):
            title_hits += 1
    return direct_hits, title_hits, _unique_preserve_order(aliases)


def _tag_article_hits(articles: list[Article], tags: list[str]) -> int:
    if not tags:
        return 0
    hits = 0
    for article in articles:
        text = _article_text(article)
        if any(_contains_keyword(text, tag) for tag in tags):
            hits += 1
    return hits


def _specific_overlap_count(tags: list[str]) -> int:
    return sum(1 for tag in tags if tag.lower() not in BROAD_INFERENCE_TAGS)


def _relevant_articles(
    articles: list[Article],
    company: Company,
    tags: list[str],
    has_direct_hit: bool,
) -> list[Article]:
    relevant: list[Article] = []
    for article in articles:
        text = _article_text(article)
        if has_direct_hit and _matched_alias(text, company):
            relevant.append(article)
            continue
        if tags and any(_contains_keyword(text, tag) for tag in tags):
            relevant.append(article)
    return relevant


def _sentiment_signal(text: str, sentiment_keywords: dict[str, list[str]]) -> tuple[int, list[str]]:
    positive_terms = _matched_terms(text, sentiment_keywords.get("positive", []))
    negative_terms = _matched_terms(text, sentiment_keywords.get("negative", []))
    score = len(positive_terms) - len(negative_terms)
    return score, _unique_preserve_order([*negative_terms, *positive_terms])


def _matched_terms(text: str, keywords: list[str]) -> list[str]:
    return [keyword for keyword in keywords if keyword and _contains_keyword(text, keyword)]


def _direction_label(score: int) -> str:
    if score > 0:
        return "正向"
    if score < 0:
        return "負向"
    return "中性"


def _direct_confidence(
    direct_hits: int,
    title_hits: int,
    tag_overlap_count: int,
    tag_article_hits: int,
) -> float:
    return min(
        0.95,
        0.58
        + min(direct_hits, 4) * 0.08
        + min(title_hits, 3) * 0.04
        + min(tag_overlap_count, 5) * 0.025
        + min(tag_article_hits, 4) * 0.02,
    )


def _inferred_confidence(
    tag_overlap_count: int,
    tag_article_hits: int,
    topic_score: int,
    specific_overlap_count: int = 0,
) -> float:
    confidence = (
        0.22
        + min(tag_overlap_count, 6) * 0.025
        + min(specific_overlap_count, 4) * 0.075
        + min(tag_article_hits, 5) * 0.025
        + min(topic_score, 8) * 0.008
    )
    cap = 0.78 if specific_overlap_count else 0.42
    return min(cap, confidence)


def _unique_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
    return output
