from __future__ import annotations

import csv
import json
from pathlib import Path

from .models import Company


DEFAULT_CONFIG_DIR = Path("config")
DEFAULT_REPORTS_DIR = Path("reports")
DEFAULT_MODEL_WEIGHTS = {
    "news_heat_weight": 1.0,
    "current_market_confirmation_weight": 0.65,
    "historical_topic_score_weight": 0.35,
    "direct_mention_weight": 1.0,
    "inferred_supply_chain_weight": 0.65,
    "broad_topic_penalty": 0.85,
    "price_divergence_penalty": 0.50,
}


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


def load_reference_sources(config_dir: Path = DEFAULT_CONFIG_DIR) -> list[dict[str, str]]:
    path = config_dir / "reference_sources.json"
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    output: list[dict[str, str]] = []
    for item in raw:
        if not isinstance(item, dict):
            continue
        output.append(
            {
                "category": str(item.get("category", "")),
                "name": str(item.get("name", "")),
                "url": str(item.get("url", "")),
                "usage": str(item.get("usage", "")),
                "mode": str(item.get("mode", "")),
            }
        )
    return output


def load_model_weights(config_dir: Path = DEFAULT_CONFIG_DIR) -> dict[str, float]:
    path = config_dir / "model_weights.json"
    if not path.exists():
        return dict(DEFAULT_MODEL_WEIGHTS)
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    weights = dict(DEFAULT_MODEL_WEIGHTS)
    for key, default in DEFAULT_MODEL_WEIGHTS.items():
        value = raw.get(key, default)
        if isinstance(value, (int, float)):
            weights[key] = float(value)
    return weights


def write_model_weights(config_dir: Path, weights: dict[str, float]) -> Path:
    config_dir.mkdir(parents=True, exist_ok=True)
    path = config_dir / "model_weights.json"
    normalized = {key: round(float(weights.get(key, value)), 4) for key, value in DEFAULT_MODEL_WEIGHTS.items()}
    path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def _split_multi(value: str) -> tuple[str, ...]:
    return tuple(item.strip() for item in value.split("|") if item.strip())
