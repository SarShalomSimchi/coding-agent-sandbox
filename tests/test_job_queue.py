import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from job_queue import deduplicate_jobs


class DeduplicateJobsBaselineTest(unittest.TestCase):
    def test_keeps_distinct_jobs(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer", "score": 70},
            {"company": "Beta", "title": "Platform Engineer", "score": 80},
        ]
        self.assertEqual(deduplicate_jobs(jobs), jobs)

    def test_normalizes_company_and_title_for_duplicates(self):
        jobs = [
            {"company": " Acme ", "title": "Backend Engineer", "score": 70},
            {"company": "acme", "title": " backend engineer ", "score": 70},
        ]
        self.assertEqual(deduplicate_jobs(jobs), [jobs[0]])


if __name__ == "__main__":
    unittest.main()
