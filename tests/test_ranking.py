import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ranking import top_jobs


class TopJobsBaselineTest(unittest.TestCase):
    def test_zero_limit_returns_empty(self):
        jobs = [{"title": "A", "score": 10}]
        self.assertEqual(top_jobs(jobs, 0), [])

    def test_negative_limit_returns_empty(self):
        jobs = [{"title": "A", "score": 10}]
        self.assertEqual(top_jobs(jobs, -5), [])

    def test_limit_larger_than_input_returns_all_jobs(self):
        jobs = [
            {"title": "A", "score": 10},
            {"title": "B", "score": 20},
        ]
        self.assertEqual(len(top_jobs(jobs, 10)), 2)


class TopJobsRankingRegressionTest(unittest.TestCase):
    def test_returns_jobs_in_descending_score_order(self):
        jobs = [
            {"title": "A", "score": 40},
            {"title": "B", "score": 90},
            {"title": "C", "score": 70},
        ]
        self.assertEqual(
            [job["title"] for job in top_jobs(jobs, 3)],
            ["B", "C", "A"],
        )

    def test_returns_at_most_limit_items(self):
        jobs = [
            {"title": "A", "score": 40},
            {"title": "B", "score": 90},
            {"title": "C", "score": 70},
        ]
        result = top_jobs(jobs, 2)
        self.assertEqual([job["title"] for job in result], ["B", "C"])

    def test_equal_scores_preserve_original_input_order(self):
        jobs = [
            {"title": "A", "score": 50},
            {"title": "B", "score": 50},
            {"title": "C", "score": 50},
        ]
        self.assertEqual(
            [job["title"] for job in top_jobs(jobs, 3)],
            ["A", "B", "C"],
        )

    def test_does_not_mutate_input_list_or_jobs(self):
        jobs = [
            {"title": "A", "score": 40},
            {"title": "B", "score": 90},
            {"title": "C", "score": 70},
        ]
        snapshot = [dict(job) for job in jobs]
        top_jobs(jobs, 2)
        self.assertEqual(jobs, snapshot)
        self.assertEqual([job["title"] for job in jobs], ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
