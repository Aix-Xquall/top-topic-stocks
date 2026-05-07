from __future__ import annotations

import unittest

from market_topics.collectors.fundamentals import _calculate_revenue_yoy, _revenue_sort_key


class TaiwanMetricsTest(unittest.TestCase):
    def test_calculates_month_revenue_yoy_from_same_revenue_month(self) -> None:
        rows = [
            {"date": "2025-04-01", "revenue_year": 2025, "revenue_month": 3, "revenue": 100},
            {"date": "2026-04-01", "revenue_year": 2026, "revenue_month": 3, "revenue": 125},
        ]
        latest = sorted(rows, key=_revenue_sort_key)[-1]

        self.assertEqual(_calculate_revenue_yoy(latest, rows), 25.0)

    def test_revenue_yoy_is_none_without_prior_year_comparison(self) -> None:
        rows = [
            {"date": "2026-04-01", "revenue_year": 2026, "revenue_month": 3, "revenue": 125},
        ]

        self.assertIsNone(_calculate_revenue_yoy(rows[0], rows))


if __name__ == "__main__":
    unittest.main()

