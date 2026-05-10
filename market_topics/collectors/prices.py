from __future__ import annotations

import urllib.parse
from datetime import date, datetime, timedelta, timezone
from typing import Any

from ..models import Company, PricePerformance
from ..analysis.validation import direction_sign
from .fundamentals import FINMIND_URL
from .http import HttpError, get_json


YAHOO_CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
MAX_RECENT_RETURN_ABS = 80.0


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

    def collect_forward_returns(
        self,
        company: Company,
        direction: str,
        signal_date: date | None = None,
    ) -> dict[str, Any]:
        signal = signal_date or self.report_date
        if direction_sign(direction) == 0:
            return {
                "outcome_status": "neutral",
                "source": "N/A",
                "base_date": "N/A",
                "target_date_3d": "N/A",
                "target_date_5d": "N/A",
                "forward_return_3d": None,
                "forward_return_5d": None,
            }
        if company.market.upper() == "US":
            rows = self._collect_yahoo_rows(company.ticker, company.ticker)
            source = "Yahoo Finance chart"
        elif company.market.upper() == "TW":
            rows = self._collect_yahoo_rows(f"{company.ticker}.TW", company.ticker)
            source = "Yahoo Finance chart"
            if not rows:
                rows = self._collect_yahoo_rows(f"{company.ticker}.TWO", company.ticker)
        else:
            rows = []
            source = "N/A"
        return _build_forward_returns(rows, signal, source)

    def _collect_us(self, company: Company, direction: str) -> PricePerformance:
        rows = self._collect_yahoo_rows(company.ticker, company.ticker)
        rows = _rows_until(rows, self.report_date)
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
        performance = _build_performance(rows, direction, "FinMind TaiwanStockPrice")
        history_rows = _rows_until(self._collect_yahoo_rows(f"{company.ticker}.TW", company.ticker), self.report_date)
        if history_rows:
            _merge_price_history(performance, history_rows, "Yahoo Finance chart")
        return performance

    def _collect_yahoo_rows(self, symbol: str, ticker: str) -> list[tuple[str, float]]:
        params = urllib.parse.urlencode({"range": "max", "interval": "1d"})
        url = f"{YAHOO_CHART_URL.format(symbol=symbol)}?{params}"
        try:
            payload = get_json(url, headers={"User-Agent": "Mozilla/5.0"})
        except HttpError as exc:
            self.data_gaps.append(f"Yahoo Finance 歷史價格抓取失敗：{ticker}，原因：{exc}")
            return []
        return _parse_yahoo_chart(payload)


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


def _rows_until(rows: list[tuple[str, float]], end_date: date) -> list[tuple[str, float]]:
    end_text = end_date.isoformat()
    return [(day, close) for day, close in rows if day <= end_text]


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
        current_price=_format_price(clean_rows[-1][1]),
        all_time_high=_format_price(_max_close(clean_rows)[1]),
        drawdown_from_high=_format_drawdown(clean_rows[-1][1], _max_close(clean_rows)[1]),
        all_time_high_date=_max_close(clean_rows)[0],
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
    value = (current / base - 1) * 100
    if abs(value) > MAX_RECENT_RETURN_ABS:
        return None
    return value


def _build_forward_returns(rows: list[tuple[str, float]], signal_date: date, source: str) -> dict[str, Any]:
    clean_rows = sorted((day, close) for day, close in rows if close > 0)
    if not clean_rows:
        return {
            "outcome_status": "missing_price",
            "source": source,
            "base_date": "N/A",
            "target_date_3d": "N/A",
            "target_date_5d": "N/A",
            "forward_return_3d": None,
            "forward_return_5d": None,
        }
    signal_text = signal_date.isoformat()
    base_index = next((index for index, (day, _) in enumerate(clean_rows) if day >= signal_text), None)
    if base_index is None:
        return {
            "outcome_status": "pending",
            "source": source,
            "base_date": "N/A",
            "target_date_3d": "N/A",
            "target_date_5d": "N/A",
            "forward_return_3d": None,
            "forward_return_5d": None,
        }
    base_date, base_close = clean_rows[base_index]
    return_3d, target_3d = _forward_return(clean_rows, base_index, base_close, 3)
    return_5d, target_5d = _forward_return(clean_rows, base_index, base_close, 5)
    status = "valid" if return_5d is not None else "pending"
    return {
        "outcome_status": status,
        "source": source,
        "base_date": base_date,
        "target_date_3d": target_3d or "N/A",
        "target_date_5d": target_5d or "N/A",
        "forward_return_3d": None if return_3d is None else round(return_3d, 4),
        "forward_return_5d": None if return_5d is None else round(return_5d, 4),
    }


def _forward_return(
    rows: list[tuple[str, float]],
    base_index: int,
    base_close: float,
    trading_days: int,
) -> tuple[float | None, str | None]:
    target_index = base_index + trading_days
    if target_index >= len(rows) or base_close == 0:
        return None, None
    target_date, target_close = rows[target_index]
    value = (target_close / base_close - 1) * 100
    if abs(value) > MAX_RECENT_RETURN_ABS:
        return None, target_date
    return value, target_date


def _format_pct(value: float | None) -> str:
    if value is None:
        return "N/A"
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"


def _format_price(value: float | None) -> str:
    if value is None:
        return "N/A"
    if abs(value) >= 1000:
        return f"{value:,.2f}"
    return f"{value:.2f}"


def _format_drawdown(current: float | None, high: float | None) -> str:
    if current is None or high is None or high <= 0:
        return "N/A"
    drawdown = (current / high - 1) * 100
    return f"{drawdown:.2f}%"


def _max_close(rows: list[tuple[str, float]]) -> tuple[str, float]:
    return max(rows, key=lambda item: item[1])


def _merge_price_history(performance: PricePerformance, rows: list[tuple[str, float]], source: str) -> None:
    clean_rows = [(day, close) for day, close in rows if close > 0]
    if not clean_rows:
        return
    current_day, current_close = clean_rows[-1]
    high_day, high_close = _max_close(clean_rows)
    performance.current_price = _format_price(current_close)
    performance.all_time_high = _format_price(high_close)
    performance.drawdown_from_high = _format_drawdown(current_close, high_close)
    performance.all_time_high_date = high_day
    if performance.as_of_date == "N/A":
        performance.as_of_date = current_day
    if source not in performance.source:
        performance.source = f"{performance.source}<br>{source}" if performance.source != "N/A" else source


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
