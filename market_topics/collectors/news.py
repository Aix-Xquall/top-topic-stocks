from __future__ import annotations

import json
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta
from email.utils import parsedate_to_datetime
from pathlib import Path

from ..models import Article
from .http import HttpError, get_json, get_text


GDELT_DOC_URL = "https://api.gdeltproject.org/api/v2/doc/doc"


class NewsCollector:
    def __init__(self, rss_feeds: list[str], data_gaps: list[str]) -> None:
        self.rss_feeds = rss_feeds
        self.data_gaps = data_gaps

    def collect(
        self,
        report_date: date,
        offline_sample: bool = False,
        max_articles: int = 120,
    ) -> list[Article]:
        if offline_sample:
            self.data_gaps.append("使用離線樣本新聞，未連線抓取即時新聞。")
            return load_sample_articles()

        articles: list[Article] = []
        articles.extend(self._fetch_rss(max_articles=max_articles))
        deduped = _filter_fresh_articles(_dedupe_articles(articles), report_date)
        if not deduped:
            self.data_gaps.append("未取得符合報告日期的即時新聞，改用內建樣本新聞產生報告。")
            return load_sample_articles()
        return deduped[:max_articles]

    def collect_historical(self, report_date: date, max_articles: int = 120) -> list[Article]:
        articles = self._fetch_gdelt(
            max_articles=max_articles,
            start_date=report_date,
            end_date=report_date + timedelta(days=1),
        )
        return _filter_fresh_articles(_dedupe_articles(articles), report_date)[:max_articles]

    def _fetch_gdelt(
        self,
        max_articles: int,
        start_date: date | None = None,
        end_date: date | None = None,
    ) -> list[Article]:
        query = (
            "stock OR market OR earnings OR revenue OR semiconductor OR AI "
            "OR tariff OR inflation OR electric vehicle OR datacenter"
        )
        params = {
            "query": query,
            "mode": "artlist",
            "format": "json",
            "maxrecords": str(max_articles),
            "sort": "hybridrel",
        }
        if start_date and end_date:
            params["startdatetime"] = _gdelt_datetime(start_date)
            params["enddatetime"] = _gdelt_datetime(end_date)
        else:
            params["timespan"] = "1d"
        url = f"{GDELT_DOC_URL}?{urllib.parse.urlencode(params)}"
        try:
            payload = get_json(url, headers={"User-Agent": "market-topics-research/0.1"})
        except HttpError as exc:
            self.data_gaps.append(f"GDELT 新聞抓取失敗：{exc}")
            return []

        output: list[Article] = []
        for item in payload.get("articles", []):
            title = str(item.get("title", "")).strip()
            article_url = str(item.get("url", "")).strip()
            if not title or not article_url:
                continue
            output.append(
                Article(
                    title=title,
                    url=article_url,
                    source=str(item.get("sourceCountry", "") or item.get("domain", "GDELT")),
                    published_at=str(item.get("seendate", "")),
                    summary=str(item.get("snippet", "")),
                    language=str(item.get("language", "")),
                )
            )
        return output

    def _fetch_rss(self, max_articles: int) -> list[Article]:
        output: list[Article] = []
        if not self.rss_feeds:
            return output
        per_feed_limit = max(5, max_articles // len(self.rss_feeds))
        for feed_url in self.rss_feeds:
            try:
                text = get_text(feed_url)
            except HttpError as exc:
                self.data_gaps.append(f"RSS 抓取失敗：{feed_url}，原因：{exc}")
                continue
            output.extend(_parse_rss(text, feed_url)[:per_feed_limit])
        return output[:max_articles]


def load_sample_articles() -> list[Article]:
    path = Path(__file__).resolve().parents[1] / "data" / "sample_news.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [
        Article(
            title=item["title"],
            url=item["url"],
            source=item.get("source", "sample"),
            published_at=item.get("published_at", ""),
            summary=item.get("summary", ""),
            language=item.get("language", ""),
        )
        for item in payload
    ]


def _parse_rss(text: str, feed_url: str) -> list[Article]:
    try:
        root = ET.fromstring(text)
    except ET.ParseError:
        return []
    output: list[Article] = []
    for item in root.findall(".//item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        if not title or not link:
            continue
        output.append(
            Article(
                title=title,
                url=link,
                source=feed_url,
                published_at=(item.findtext("pubDate") or "").strip(),
                summary=(item.findtext("description") or "").strip(),
            )
        )
    return output


def _dedupe_articles(articles: list[Article]) -> list[Article]:
    seen: set[str] = set()
    output: list[Article] = []
    for article in articles:
        key = article.url or article.title.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(article)
    return output


def _filter_fresh_articles(articles: list[Article], report_date: date) -> list[Article]:
    fresh: list[Article] = []
    for article in articles:
        article_date = _parse_article_date(article.published_at)
        if article_date is None:
            fresh.append(article)
            continue
        if report_date - timedelta(days=2) <= article_date <= report_date + timedelta(days=1):
            fresh.append(article)
    return fresh


def _parse_article_date(value: str) -> date | None:
    text = value.strip()
    if not text:
        return None
    for parser in (_parse_iso_date, _parse_rss_date):
        parsed = parser(text)
        if parsed is not None:
            return parsed
    return None


def _parse_iso_date(value: str) -> date | None:
    try:
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).date()
    except ValueError:
        return None


def _parse_rss_date(value: str) -> date | None:
    try:
        return parsedate_to_datetime(value).date()
    except (TypeError, ValueError, IndexError, AttributeError):
        return None


def _gdelt_datetime(value: date) -> str:
    return value.strftime("%Y%m%d%H%M%S")
