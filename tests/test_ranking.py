import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ranking import top_jobs


class TopJobsBaselineTest(unittest.TestCase):
    def test_zero_limit_returns_empty(self):
        jobs = [{"title": "A", "score": 10}]
        self.assertEqual(top_jobs(jobs, 0), [])

    def test_limit_larger_than_input_returns_all_jobs(self):
        jobs = [
            {"title": "A", "score": 10},
            {"title": "B", "score": 20},
        ]
        self.assertEqual(len(top_jobs(jobs, 10)), 2)


if __name__ == "__main__":
    unittest.main()
