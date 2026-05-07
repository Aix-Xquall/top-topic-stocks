from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import Company


DEFAULT_CONFIG_DIR = Path("config")
DEFAULT_REPORTS_DIR = Path("reports")


def load_company_universe(config_dir: Path = DEFAULT_CONFIG_DIR) -> list[Company]:
    path = config_dir / "company_universe.csv"
    companies: list[Company] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            companies.append(
                Company(
                    market=row["market"].strip(),
                    ticker=row["ticker"].strip(),
                    name_zh=row["name_zh"].strip(),
                    name_en=row["name_en"].strip(),
                    aliases=_split_multi(row.get("aliases", "")),
                    industry=row.get("industry", "").strip(),
                    tags=_split_multi(row.get("tags", "")),
                    cik=row.get("cik", "").strip(),
                )
            )
    return companies


def load_topic_keywords(config_dir: Path = DEFAULT_CONFIG_DIR) -> dict[str, list[str]]:
    path = config_dir / "topic_keywords.json"
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    return {str(topic): [str(item) for item in keywords] for topic, keywords in raw.items()}


def load_sentiment_keywords(config_dir: Path = DEFAULT_CONFIG_DIR) -> dict[str, list[str]]:
    path = config_dir / "sentiment_keywords.json"
    if not path.exists():
        return {"positive": [], "negative": []}
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    return {
        "positive": [str(item) for item in raw.get("positive", [])],
        "negative": [str(item) for item in raw.get("negative", [])],
    }


def load_rss_feeds(config_dir: Path = DEFAULT_CONFIG_DIR) -> list[str]:
    path = config_dir / "rss_feeds.txt"
    if not path.exists():
        return []
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


def _split_multi(value: str) -> tuple[str, ...]:
    return tuple(item.strip() for item in value.split("|") if item.strip())
