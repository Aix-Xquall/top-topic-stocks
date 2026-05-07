from __future__ import annotations

import unittest

from market_topics.collectors.prices import _build_performance


class PricePerformanceTest(unittest.TestCase):
    def test_positive_direction_is_confirmed_by_positive_return(self) -> None:
        performance = _build_performance(
            [
                ("2026-05-01", 100.0),
                ("2026-05-04", 102.0),
                ("2026-05-05", 104.0),
                ("2026-05-06", 106.0),
                ("2026-05-07", 108.0),
                ("2026-05-08", 110.0),
            ],
            "正向",
            "test",
        )

        self.assertEqual(performance.return_3d, "+5.77%")
        self.assertEqual(performance.return_5d, "+10.00%")
        self.assertEqual(performance.validation, "同向")

    def test_negative_direction_diverges_from_positive_return(self) -> None:
        performance = _build_performance(
            [
                ("2026-05-01", 100.0),
                ("2026-05-04", 102.0),
                ("2026-05-05", 104.0),
                ("2026-05-06", 106.0),
            ],
            "負向",
            "test",
        )

        self.assertEqual(performance.validation, "背離")


if __name__ == "__main__":
    unittest.main()

