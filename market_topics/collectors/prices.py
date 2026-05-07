from __future__ import annotations

import json
import urllib.parse
from datetime import date, datetime, time, timedelta, timezone
from typing import Any

from ..models import Company, PricePerformance
from .fundamentals import FINMIND_URL
from .http import HttpError, get_json


YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"


class PricePerformanceCollector:
    def __init__(self, data_gaps: list[str], report_date: date) -> None:
        self.data_gaps = data_gaps
        self.report_date = report_date
        self._cache: dict[tuple[str, str, str], PricePerformance] = {}

    def collect_for_company(self, company: Company, direction: str) -> PricePerformance:
        key = (company.market.upper(), company.ticker, direction)
        if key in self._cache:
            return self._cache[key]

        if company.market.upper() == "US":
            performance = self._collect_us(company, direction)
        elif company.market.upper() == "TW":
            performance = self._collect_tw(company, direction)
        else:
            performance = PricePerformance(notes=[f"未知市場：{company.market}"])

        self._cache[key] = performance
        return performance

    def _collect_us(self, company: Company, direction: str) -> PricePerformance:
        start = self.report_date - timedelta(days=14)
        end = self.report_date + timedelta(days=2)
        period1 = _epoch_seconds(start)
        period2 = _epoch_seconds(end)
        params = urllib.parse.urlencode({"period1": period1, "period2": period2, "interval": "1d"})
        url = f"{YAHOO_CHART_URL.format(symbol=company.ticker)}?{params}"
        try:
            payload = get_json(url, headers={"User-Agent": "Mozilla/5.0"})
        except HttpError as exc:
            self.data_gaps.append(f"Yahoo Finance 日線抓取失敗：{company.ticker}，原因：{exc}")
            return PricePerformance(notes=[str(exc)])

        rows = _parse_yahoo_chart(payload)
        return _build_performance(rows, direction, "Yahoo Finance chart")

    def _collect_tw(self, company: Company, direction: str) -> PricePerformance:
        start = (self.report_date - timedelta(days=14)).isoformat()
        end = (self.report_date + timedelta(days=2)).isoformat()
        params = {
            "dataset": "TaiwanStockPrice",
            "data_id": company.ticker,
            "start_date": start,
            "end_date": end,
        }
        url = f"{FINMIND_URL}?{urllib.parse.urlencode(params)}"
        try:
            payload = get_json(url)
        except HttpError as exc:
            self.data_gaps.append(f"FinMind 股價抓取失敗：{company.ticker}，原因：{exc}")
            return PricePerformance(notes=[str(exc)])

        rows = [
            (str(row.get("date", "")), float(row["close"]))
            for row in payload.get("data", [])
            if row.get("date") and row.get("close") is not None
        ]
        return _build_performance(rows, direction, "FinMind TaiwanStockPrice")


def _epoch_seconds(value: date) -> int:
    return int(datetime.combine(value, time.min, tzinfo=timezone.utc).timestamp())


def _parse_yahoo_chart(payload: dict[str, Any]) -> list[tuple[str, float]]:
    result = payload.get("chart", {}).get("result", [])
    if not result:
        return []
    item = result[0]
    timestamps = item.get("timestamp", [])
    closes = item.get("indicators", {}).get("quote", [{}])[0].get("close", [])
    rows: list[tuple[str, float]] = []
    for timestamp, close in zip(timestamps, closes):
        if close is None:
            continue
        rows.append((datetime.fromtimestamp(timestamp, tz=timezone.utc).date().isoformat(), float(close)))
    return rows


def _build_performance(rows: list[tuple[str, float]], direction: str, source: str) -> PricePerformance:
    clean_rows = [(day, close) for day, close in rows if close > 0]
    if len(clean_rows) < 2:
        return PricePerformance(source=source, notes=["可用收盤價不足。"])

    return_3d = _period_return(clean_rows, 3)
    return_5d = _period_return(clean_rows, 5)
    validation_basis = return_3d if return_3d is not None else return_5d
    validation = _validate_direction(direction, validation_basis)
    return PricePerformance(
        return_3d=_format_pct(return_3d),
        return_5d=_format_pct(return_5d),
        as_of_date=clean_rows[-1][0],
        validation=validation,
        source=source,
    )


def _period_return(rows: list[tuple[str, float]], trading_days: int) -> float | None:
    if len(rows) <= trading_days:
        return None
    current = rows[-1][1]
    base = rows[-(trading_days + 1)][1]
    if base == 0:
        return None
    return (current / base - 1) * 100


def _format_pct(value: float | None) -> str:
    if value is None:
        return "N/A"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def _validate_direction(direction: str, recent_return: float | None) -> str:
    if direction == "中性":
        return "不適用"
    if recent_return is None:
        return "N/A"
    if abs(recent_return) < 1.0:
        return "未明確"
    if direction == "正向":
        return "同向" if recent_return > 0 else "背離"
    if direction == "負向":
        return "同向" if recent_return < 0 else "背離"
    return "N/A"

