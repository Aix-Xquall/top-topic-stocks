from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    source: str
    published_at: str = ""
    summary: str = ""
    language: str = ""


@dataclass(frozen=True)
class Company:
    market: str
    ticker: str
    name_zh: str
    name_en: str
    aliases: tuple[str, ...]
    industry: str
    tags: tuple[str, ...]
    cik: str = ""


@dataclass
class CompanyMetrics:
    eps: str = "N/A"
    pe: str = "N/A"
    revenue: str = "N/A"
    revenue_yoy: str = "N/A"
    currency: str = ""
    as_of_date: str = "N/A"
    sources: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


@dataclass
class PricePerformance:
    return_3d: str = "N/A"
    return_5d: str = "N/A"
    current_price: str = "N/A"
    all_time_high: str = "N/A"
    drawdown_from_high: str = "N/A"
    all_time_high_date: str = "N/A"
    as_of_date: str = "N/A"
    validation: str = "N/A"
    source: str = "N/A"
    notes: list[str] = field(default_factory=list)


@dataclass
class CompanyRelation:
    company: Company
    relation_type: str
    reason: str
    confidence: float
    impact_direction: str = "中性"
    impact_score: int = 0
    metrics: CompanyMetrics = field(default_factory=CompanyMetrics)
    price_performance: PricePerformance = field(default_factory=PricePerformance)


@dataclass
class Topic:
    name: str
    score: int
    summary: str
    articles: list[Article]
    direction: str = "中性"
    sentiment_score: int = 0
    related_companies: list[CompanyRelation] = field(default_factory=list)


@dataclass
class RunResult:
    report_date: date
    topics: list[Topic]
    data_gaps: list[str]
    output_markdown: str
    output_html: str
    output_summary: str = ""
