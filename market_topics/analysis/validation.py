from __future__ import annotations

import math
from typing import Any

from ..models import CompanyRelation, Topic


def adjusted_directional_confidence(direction: str, confidence: float, price_validation: str = "N/A") -> str:
    adjusted = market_adjusted_confidence(confidence, price_validation)
    if direction == "正向":
        return f"+{adjusted:.2f}"
    if direction == "負向":
        return f"-{adjusted:.2f}"
    return "0.00"


def market_adjusted_confidence(confidence: float, price_validation: str) -> float:
    if price_validation == "同向":
        return confidence
    if price_validation == "背離":
        return confidence * 0.50
    if price_validation == "未明確":
        return confidence * 0.75
    return confidence


def raw_signed_confidence(relation: CompanyRelation) -> float | None:
    sign = direction_sign(relation.impact_direction)
    if sign == 0:
        return None
    return sign * relation.confidence


def direction_sign(direction: str) -> int:
    if direction == "正向":
        return 1
    if direction == "負向":
        return -1
    return 0


def parse_percent(value: str) -> float | None:
    if not value or value == "N/A":
        return None
    text = str(value).replace("%", "").replace(",", "").strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def relation_directional_return(relation: CompanyRelation, period: str = "3d") -> float | None:
    sign = direction_sign(relation.impact_direction)
    if sign == 0:
        return None
    price = relation.price_performance
    raw = parse_percent(price.return_5d if period == "5d" else price.return_3d)
    if raw is None:
        return None
    return sign * raw


def topic_market_validation(topic: Topic) -> dict[str, Any]:
    rows = [relation for relation in topic.related_companies if direction_sign(relation.impact_direction) != 0]
    valid_rows = [relation for relation in rows if relation_directional_return(relation, "3d") is not None]
    aligned = sum(1 for relation in valid_rows if relation.price_performance.validation == "同向")
    diverged = sum(1 for relation in valid_rows if relation.price_performance.validation == "背離")
    unclear = sum(1 for relation in valid_rows if relation.price_performance.validation == "未明確")
    avg_3d = _mean([relation_directional_return(relation, "3d") for relation in valid_rows])
    avg_5d = _mean([relation_directional_return(relation, "5d") for relation in valid_rows])
    aligned_ratio = aligned / len(valid_rows) if valid_rows else None
    score = _confirmation_score(aligned_ratio, avg_3d)
    return {
        "topic": topic.name,
        "company_count": len(topic.related_companies),
        "validated_count": len(valid_rows),
        "aligned_count": aligned,
        "diverged_count": diverged,
        "unclear_count": unclear,
        "aligned_ratio": _round_or_none(aligned_ratio),
        "avg_directional_return_3d": _round_or_none(avg_3d),
        "avg_directional_return_5d": _round_or_none(avg_5d),
        "market_confirmation_score": _round_or_none(score),
    }


def daily_market_validation(topics: list[Topic]) -> dict[str, Any]:
    pairs_3d: list[tuple[float, float]] = []
    pairs_5d: list[tuple[float, float]] = []
    aligned = 0
    diverged = 0
    unclear = 0
    valid = 0

    for topic in topics:
        for relation in topic.related_companies:
            confidence = raw_signed_confidence(relation)
            if confidence is None:
                continue
            return_3d = parse_percent(relation.price_performance.return_3d)
            return_5d = parse_percent(relation.price_performance.return_5d)
            if return_3d is not None:
                pairs_3d.append((confidence, return_3d))
                valid += 1
                if relation.price_performance.validation == "同向":
                    aligned += 1
                elif relation.price_performance.validation == "背離":
                    diverged += 1
                elif relation.price_performance.validation == "未明確":
                    unclear += 1
            if return_5d is not None:
                pairs_5d.append((confidence, return_5d))

    topics_validation = [topic_market_validation(topic) for topic in topics]
    return {
        "sample_count_3d": len(pairs_3d),
        "sample_count_5d": len(pairs_5d),
        "correlation_3d": _round_or_none(_pearson(pairs_3d)),
        "correlation_5d": _round_or_none(_pearson(pairs_5d)),
        "aligned_count": aligned,
        "diverged_count": diverged,
        "unclear_count": unclear,
        "validated_count": valid,
        "aligned_ratio": _round_or_none(aligned / valid if valid else None),
        "topics": topics_validation,
    }


def format_optional_number(value: float | None, digits: int = 2) -> str:
    if value is None:
        return "N/A"
    return f"{value:.{digits}f}"


def format_optional_percent(value: float | None) -> str:
    if value is None:
        return "N/A"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def _confirmation_score(aligned_ratio: float | None, avg_directional_return: float | None) -> float | None:
    if aligned_ratio is None and avg_directional_return is None:
        return None
    ratio_component = 50.0 if aligned_ratio is None else aligned_ratio * 70.0
    return_component = 0.0 if avg_directional_return is None else max(-10.0, min(10.0, avg_directional_return)) * 3.0
    return max(0.0, min(100.0, ratio_component + return_component))


def _mean(values: list[float | None]) -> float | None:
    clean = [value for value in values if value is not None]
    if not clean:
        return None
    return sum(clean) / len(clean)


def _pearson(pairs: list[tuple[float, float]]) -> float | None:
    if len(pairs) < 3:
        return None
    xs = [item[0] for item in pairs]
    ys = [item[1] for item in pairs]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    numerator = sum((x - mean_x) * (y - mean_y) for x, y in pairs)
    denominator_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    denominator_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if denominator_x == 0 or denominator_y == 0:
        return None
    return numerator / (denominator_x * denominator_y)


def _round_or_none(value: float | None) -> float | None:
    if value is None:
        return None
    return round(value, 4)
