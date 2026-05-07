from __future__ import annotations

import os
import urllib.parse
from datetime import date, timedelta
from typing import Any

from ..models import Company, CompanyMetrics
from .http import HttpError, get_json


ALPHA_URL = "https://www.alphavantage.co/query"
FINMIND_URL = "https://api.finmindtrade.com/api/v4/data"
SEC_COMPANYFACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
TWSE_PER_URL = "https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL"


class FundamentalsCollector:
    def __init__(self, data_gaps: list[str], report_date: date | None = None) -> None:
        self.data_gaps = data_gaps
        self.report_date = report_date or date.today()
        self.alpha_key = os.getenv("ALPHAVANTAGE_API_KEY", "").strip()
        self.finmind_token = os.getenv("FINMIND_TOKEN", "").strip()
        self.sec_user_agent = os.getenv("SEC_USER_AGENT", "").strip()
        self._twse_per_cache: dict[str, dict[str, Any]] | None = None

    def collect_for_company(self, company: Company) -> CompanyMetrics:
        if company.market.upper() == "US":
            return self._collect_us(company)
        if company.market.upper() == "TW":
            return self._collect_tw(company)
        return CompanyMetrics(notes=[f"未知市場：{company.market}"])

    def _collect_us(self, company: Company) -> CompanyMetrics:
        metrics = CompanyMetrics(currency="USD")
        if self.alpha_key:
            self._merge_alpha(company, metrics)
        else:
            metrics.notes.append("未設定 ALPHAVANTAGE_API_KEY，跳過 Alpha Vantage 估值補充。")

        if company.cik and self.sec_user_agent:
            self._merge_sec(company, metrics)
        elif company.cik:
            metrics.notes.append("未設定 SEC_USER_AGENT，跳過 SEC EDGAR XBRL。")
        else:
            metrics.notes.append("company_universe.csv 未提供 CIK，無法抓取 SEC EDGAR XBRL。")
        return metrics

    def _collect_tw(self, company: Company) -> CompanyMetrics:
        metrics = CompanyMetrics(currency="TWD")
        self._merge_twse_per(company, metrics)
        self._merge_finmind_revenue(company, metrics)
        self._merge_finmind_eps(company, metrics)
        return metrics

    def _merge_alpha(self, company: Company, metrics: CompanyMetrics) -> None:
        overview_url = _url(ALPHA_URL, function="OVERVIEW", symbol=company.ticker, apikey=self.alpha_key)
        try:
            overview = get_json(overview_url)
        except HttpError as exc:
            self.data_gaps.append(f"Alpha Vantage 抓取失敗：{company.ticker}，原因：{exc}")
            return
        if "Note" in overview or "Information" in overview:
            self.data_gaps.append(f"Alpha Vantage 限流或回覆資訊：{company.ticker}")
            return

        eps = _clean_number(overview.get("EPS"))
        pe = _clean_number(overview.get("PERatio"))
        revenue = _clean_number(overview.get("RevenueTTM"))
        latest_quarter = str(overview.get("LatestQuarter", "")).strip()
        if eps:
            metrics.eps = eps
        if pe:
            metrics.pe = pe
        if revenue:
            metrics.revenue = _format_large_number(revenue)
        if latest_quarter:
            metrics.as_of_date = latest_quarter
        metrics.sources.append("Alpha Vantage OVERVIEW")

    def _merge_sec(self, company: Company, metrics: CompanyMetrics) -> None:
        cik = company.cik.zfill(10)
        url = SEC_COMPANYFACTS_URL.format(cik=cik)
        headers = {"User-Agent": self.sec_user_agent}
        try:
            payload = get_json(url, headers=headers)
        except HttpError as exc:
            self.data_gaps.append(f"SEC EDGAR 抓取失敗：{company.ticker}，原因：{exc}")
            return

        facts = payload.get("facts", {}).get("us-gaap", {})
        eps_fact = _latest_fact(facts, ["EarningsPerShareDiluted", "EarningsPerShareBasic"], "USD/shares")
        revenue_fact = _latest_fact(
            facts,
            ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"],
            "USD",
        )
        if eps_fact and metrics.eps == "N/A":
            metrics.eps = str(eps_fact["val"])
        if revenue_fact and metrics.revenue == "N/A":
            metrics.revenue = _format_large_number(str(revenue_fact["val"]))
        latest_end = max(
            [str(item.get("end", "")) for item in [eps_fact, revenue_fact] if item],
            default="",
        )
        if latest_end and metrics.as_of_date == "N/A":
            metrics.as_of_date = latest_end
        metrics.sources.append("SEC EDGAR XBRL companyfacts")

    def _merge_twse_per(self, company: Company, metrics: CompanyMetrics) -> None:
        if self._twse_per_cache is None:
            try:
                rows = get_json(TWSE_PER_URL)
                self._twse_per_cache = {str(row.get("Code", "")).strip(): row for row in rows}
            except HttpError as exc:
                self._twse_per_cache = {}
                self.data_gaps.append(f"TWSE PER/PBR 抓取失敗：{exc}")

        row = self._twse_per_cache.get(company.ticker, {}) if self._twse_per_cache else {}
        pe = _clean_number(row.get("PEratio") or row.get("PE Ratio") or row.get("本益比"))
        if pe:
            metrics.pe = pe
            metrics.sources.append("TWSE OpenAPI BWIBBU_ALL")

    def _merge_finmind_revenue(self, company: Company, metrics: CompanyMetrics) -> None:
        start_date = (self.report_date - timedelta(days=500)).isoformat()
        params = {
            "dataset": "TaiwanStockMonthRevenue",
            "data_id": company.ticker,
            "start_date": start_date,
        }
        if self.finmind_token:
            params["token"] = self.finmind_token
        url = f"{FINMIND_URL}?{urllib.parse.urlencode(params)}"
        try:
            payload = get_json(url)
        except HttpError as exc:
            self.data_gaps.append(f"FinMind 月營收抓取失敗：{company.ticker}，原因：{exc}")
            return

        rows = payload.get("data", [])
        if not rows:
            metrics.notes.append("FinMind 無月營收資料或免費額度受限。")
            return
        latest = sorted(rows, key=_revenue_sort_key)[-1]
        revenue = _clean_number(latest.get("revenue"))
        revenue_yoy = _calculate_revenue_yoy(latest, rows)
        if revenue:
            metrics.revenue = _format_large_number(revenue)
        if revenue_yoy is not None:
            metrics.revenue_yoy = f"{revenue_yoy:.2f}%"
        metrics.as_of_date = str(latest.get("date", metrics.as_of_date))
        metrics.sources.append("FinMind TaiwanStockMonthRevenue")

    def _merge_finmind_eps(self, company: Company, metrics: CompanyMetrics) -> None:
        start_date = (self.report_date - timedelta(days=900)).isoformat()
        params = {
            "dataset": "TaiwanStockFinancialStatements",
            "data_id": company.ticker,
            "start_date": start_date,
        }
        if self.finmind_token:
            params["token"] = self.finmind_token
        url = f"{FINMIND_URL}?{urllib.parse.urlencode(params)}"
        try:
            payload = get_json(url)
        except HttpError as exc:
            self.data_gaps.append(f"FinMind 綜合損益表抓取失敗：{company.ticker}，原因：{exc}")
            return

        rows = payload.get("data", [])
        eps_rows = [
            row
            for row in rows
            if str(row.get("type", "")).upper() == "EPS" and _clean_number(row.get("value"))
        ]
        if not eps_rows:
            metrics.notes.append("FinMind 綜合損益表沒有 EPS 資料。")
            return

        latest_eps_rows = sorted(eps_rows, key=lambda row: str(row.get("date", "")))[-4:]
        eps_values = [float(str(row["value"]).replace(",", "")) for row in latest_eps_rows]
        eps_ttm = sum(eps_values)
        metrics.eps = f"{eps_ttm:.2f}"
        latest_date = str(latest_eps_rows[-1].get("date", ""))
        if latest_date and metrics.as_of_date == "N/A":
            metrics.as_of_date = latest_date
        elif latest_date and metrics.as_of_date != "N/A":
            metrics.as_of_date = max(metrics.as_of_date, latest_date)
        metrics.sources.append("FinMind TaiwanStockFinancialStatements EPS TTM")


def _url(base: str, **params: str) -> str:
    return f"{base}?{urllib.parse.urlencode(params)}"


def _clean_number(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace(",", "").strip()
    if not text or text.lower() in {"none", "null", "nan", "-"}:
        return ""
    return text


def _format_large_number(value: str) -> str:
    try:
        number = float(value)
    except ValueError:
        return value
    if abs(number) >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f}B"
    if abs(number) >= 1_000_000:
        return f"{number / 1_000_000:.2f}M"
    return f"{number:,.0f}"


def _revenue_sort_key(row: dict[str, Any]) -> tuple[int, int, str]:
    try:
        year = int(row.get("revenue_year", 0))
        month = int(row.get("revenue_month", 0))
    except (TypeError, ValueError):
        year = 0
        month = 0
    return (year, month, str(row.get("date", "")))


def _calculate_revenue_yoy(latest: dict[str, Any], rows: list[dict[str, Any]]) -> float | None:
    try:
        latest_year = int(latest.get("revenue_year"))
        latest_month = int(latest.get("revenue_month"))
        latest_revenue = float(str(latest.get("revenue")).replace(",", ""))
    except (TypeError, ValueError):
        return None

    previous: dict[str, Any] | None = None
    for row in rows:
        try:
            if int(row.get("revenue_year")) == latest_year - 1 and int(row.get("revenue_month")) == latest_month:
                previous = row
                break
        except (TypeError, ValueError):
            continue
    if previous is None:
        return None
    try:
        previous_revenue = float(str(previous.get("revenue")).replace(",", ""))
    except (TypeError, ValueError):
        return None
    if previous_revenue == 0:
        return None
    return (latest_revenue - previous_revenue) / previous_revenue * 100


def _latest_fact(facts: dict[str, Any], concepts: list[str], unit: str) -> dict[str, Any] | None:
    candidates: list[dict[str, Any]] = []
    for concept in concepts:
        units = facts.get(concept, {}).get("units", {})
        candidates.extend(units.get(unit, []))
    if not candidates:
        return None
    filed = [item for item in candidates if item.get("val") is not None and item.get("end")]
    if not filed:
        return None
    return sorted(filed, key=lambda item: (str(item.get("end", "")), str(item.get("filed", ""))))[-1]
