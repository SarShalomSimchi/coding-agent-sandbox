import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from score_summary import score_summary


class ScoreSummaryTest(unittest.TestCase):
    def test_empty_input_returns_none_fields(self):
        self.assertEqual(
            score_summary([]),
            {
                "count": 0,
                "min_score": None,
                "max_score": None,
                "average_score": None,
            },
        )

    def test_single_job(self):
        self.assertEqual(
            score_summary([{"title": "A", "score": 42}]),
            {
                "count": 1,
                "min_score": 42,
                "max_score": 42,
                "average_score": 42.0,
            },
        )

    def test_multiple_positive_scores(self):
        jobs = [
            {"title": "A", "score": 10},
            {"title": "B", "score": 20},
            {"title": "C", "score": 30},
        ]
        self.assertEqual(
            score_summary(jobs),
            {
                "count": 3,
                "min_score": 10,
                "max_score": 30,
                "average_score": 20.0,
            },
        )

    def test_negative_and_positive_scores(self):
        jobs = [
            {"title": "A", "score": -5},
            {"title": "B", "score": 0},
            {"title": "C", "score": 5},
        ]
        self.assertEqual(
            score_summary(jobs),
            {
                "count": 3,
                "min_score": -5,
                "max_score": 5,
                "average_score": 0.0,
            },
        )

    def test_input_is_not_mutated(self):
        jobs = [
            {"title": "A", "score": 10},
            {"title": "B", "score": 20},
        ]
        original = copy.deepcopy(jobs)
        score_summary(jobs)
        self.assertEqual(jobs, original)


if __name__ == "__main__":
    unittest.main()
