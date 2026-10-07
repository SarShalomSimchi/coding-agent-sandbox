import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from job_filters import filter_jobs_by_min_score


class FilterJobsByMinScoreTest(unittest.TestCase):
    def test_empty_input_returns_empty_list(self):
        self.assertEqual(filter_jobs_by_min_score([], 50), [])

    def test_all_jobs_below_threshold_returns_empty_list(self):
        jobs = [
            {"title": "A", "score": 10},
            {"title": "B", "score": 20},
        ]
        self.assertEqual(filter_jobs_by_min_score(jobs, 50), [])

    def test_all_jobs_at_or_above_threshold_are_kept(self):
        jobs = [
            {"title": "A", "score": 60},
            {"title": "B", "score": 90},
        ]
        self.assertEqual(filter_jobs_by_min_score(jobs, 50), jobs)

    def test_boundary_equality_is_inclusive(self):
        jobs = [{"title": "A", "score": 50}]
        self.assertEqual(filter_jobs_by_min_score(jobs, 50), jobs)

    def test_preserves_original_input_order(self):
        jobs = [
            {"title": "Low", "score": 30},
            {"title": "High", "score": 90},
            {"title": "Mid", "score": 70},
        ]
        result = filter_jobs_by_min_score(jobs, 50)
        self.assertEqual([job["title"] for job in result], ["High", "Mid"])

    def test_does_not_mutate_input(self):
        jobs = [
            {"title": "Low", "score": 30},
            {"title": "High", "score": 90},
        ]
        snapshot = [dict(job) for job in jobs]
        result = filter_jobs_by_min_score(jobs, 50)
        self.assertEqual(jobs, snapshot)
        self.assertIsNot(result, jobs)
        self.assertIs(result[0], jobs[1])


if __name__ == "__main__":
    unittest.main()
