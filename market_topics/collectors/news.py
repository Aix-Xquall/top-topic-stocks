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
GOOGLE_NEWS_RSS_URL = "https://news.google.com/rss/search"
DEFAULT_SOURCE_TIERS = [
    {"tier": "official", "name": "MOPS", "domain": "mops.twse.com.tw", "weight": 1.25, "query": "重大訊息 OR 月營收 OR 財報 OR 法說會"},
    {"tier": "official", "name": "TWSE", "domain": "twse.com.tw", "weight": 1.20, "query": "上市公司 OR 注意股票 OR 法人 OR 成交資訊"},
    {"tier": "official", "name": "TPEx", "domain": "tpex.org.tw", "weight": 1.20, "query": "上櫃 OR 興櫃 OR 注意股票 OR 公告"},
    {"tier": "financial_news", "name": "Yahoo 奇摩股市", "domain": "tw.stock.yahoo.com", "weight": 1.00, "query": "台股 OR 個股 OR 美股 OR 半導體 OR 財報 OR 營收"},
    {"tier": "financial_news", "name": "鉅亨網", "domain": "news.cnyes.com", "weight": 1.00, "query": "台股 OR 個股 OR 美股 OR 半導體 OR 財報 OR 營收"},
    {"tier": "financial_news", "name": "MoneyDJ", "domain": "moneydj.com", "weight": 0.95, "query": "台股 OR 個股 OR 產業 OR 半導體 OR 財報 OR 營收"},
    {"tier": "financial_news", "name": "經濟日報 money", "domain": "money.udn.com", "weight": 0.95, "query": "證券 OR 台股 OR 個股 OR 美股 OR 半導體 OR 財報"},
    {"tier": "financial_news", "name": "中央社財經", "domain": "cna.com.tw", "weight": 1.05, "query": "財經 OR 證券 OR 台股 OR 半導體 OR 公司"},
    {"tier": "financial_news", "name": "工商時報", "domain": "ctee.com.tw", "weight": 0.95, "query": "台股 OR 個股 OR 產業 OR 半導體 OR 法人"},
    {"tier": "financial_news", "name": "TechNews 科技新報", "domain": "technews.tw", "weight": 0.95, "query": "半導體 OR AI OR 晶片 OR 先進封裝 OR 伺服器"},
    {"tier": "financial_news", "name": "Reuters Markets", "domain": "reuters.com", "weight": 1.05, "query": "markets OR stocks OR earnings OR revenue OR semiconductor OR AI"},
    {"tier": "financial_news", "name": "CNBC Markets", "domain": "cnbc.com", "weight": 0.95, "query": "markets OR stocks OR earnings OR semiconductor OR AI"},
    {"tier": "event_calendar", "name": "Nasdaq Earnings", "domain": "nasdaq.com", "weight": 0.70, "query": "earnings OR dividend OR IPO OR split"},
    {"tier": "event_calendar", "name": "Investing.com Calendar", "domain": "investing.com", "weight": 0.65, "query": "economic calendar OR CPI OR rate decision OR PMI OR GDP"},
]
SOURCE_DISCOVERY_QUERIES = [f"site:{item['domain']} {item['query']}" for item in DEFAULT_SOURCE_TIERS]
HISTORICAL_GOOGLE_NEWS_QUERIES = SOURCE_DISCOVERY_QUERIES


class NewsCollector:
    def __init__(self, rss_feeds: list[str], data_gaps: list[str]) -> None:
        self.rss_feeds = rss_feeds
        self.data_gaps = data_gaps
        self.source_tiers = DEFAULT_SOURCE_TIERS

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
        if len(articles) < max_articles:
            articles.extend(self._fetch_google_news_current(max_articles=max_articles - len(articles)))
        deduped = _filter_fresh_articles(_dedupe_articles(articles), report_date)
        if not deduped:
            self.data_gaps.append("未取得符合報告日期的即時新聞，改用內建樣本新聞產生報告。")
            return load_sample_articles()
        return deduped[:max_articles]

    def _fetch_google_news_current(self, max_articles: int) -> list[Article]:
        if max_articles <= 0:
            return []
        output: list[Article] = []
        per_query_limit = max(5, max_articles // len(self.source_tiers))
        for source in self.source_tiers:
            query = f"site:{source['domain']} {source['query']}"
            params = {
                "q": f"{query} when:3d",
                "hl": "zh-TW",
                "gl": "TW",
                "ceid": "TW:zh-Hant",
            }
            url = f"{GOOGLE_NEWS_RSS_URL}?{urllib.parse.urlencode(params)}"
            try:
                text = get_text(url, headers={"User-Agent": "Mozilla/5.0"})
            except HttpError as exc:
                self.data_gaps.append(f"Google News 財經來源抓取失敗：{query}，原因：{exc}")
                continue
            output.extend(_tag_articles(_parse_rss(text, "Google News source discovery"), source)[:per_query_limit])
            if len(output) >= max_articles:
                break
        return output[:max_articles]

    def collect_historical(self, report_date: date, max_articles: int = 120) -> list[Article]:
        articles = self._fetch_google_news_historical(report_date, max_articles=max_articles)
        if len(articles) < 5:
            articles.extend(
                self._fetch_gdelt(
                    max_articles=max_articles,
                    start_date=report_date,
                    end_date=report_date + timedelta(days=1),
                )
            )
        return _filter_fresh_articles(_dedupe_articles(articles), report_date)[:max_articles]

    def _fetch_google_news_historical(self, report_date: date, max_articles: int) -> list[Article]:
        output: list[Article] = []
        per_query_limit = max(8, max_articles // len(HISTORICAL_GOOGLE_NEWS_QUERIES))
        next_date = report_date + timedelta(days=1)
        for query in HISTORICAL_GOOGLE_NEWS_QUERIES:
            dated_query = f"{query} after:{report_date.isoformat()} before:{next_date.isoformat()}"
            params = {
                "q": dated_query,
                "hl": "zh-TW",
                "gl": "TW",
                "ceid": "TW:zh-Hant",
            }
            url = f"{GOOGLE_NEWS_RSS_URL}?{urllib.parse.urlencode(params)}"
            try:
                text = get_text(url, headers={"User-Agent": "Mozilla/5.0"})
            except HttpError as exc:
                self.data_gaps.append(f"Google News 歷史新聞抓取失敗：{report_date.isoformat()}，原因：{exc}")
                continue
            output.extend(_parse_rss(text, "Google News historical")[:per_query_limit])
            if len(output) >= max_articles:
                break
        return output[:max_articles]

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


def _tag_articles(articles: list[Article], source: dict[str, object]) -> list[Article]:
    suffix = (
        f"來源層級：{source.get('tier', '')}；"
        f"來源名稱：{source.get('name', '')}；"
        f"來源權重：{source.get('weight', 1.0)}"
    )
    output: list[Article] = []
    for article in articles:
        summary = f"{article.summary}\n{suffix}".strip()
        output.append(
            Article(
                title=article.title,
                url=article.url,
                source=f"{article.source} | {source.get('name', '')}",
                published_at=article.published_at,
                summary=summary,
                language=article.language,
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
