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

    def test_later_higher_score_replaces_earlier_duplicate(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer", "score": 70},
            {"company": "Beta", "title": "Platform Engineer", "score": 80},
            {"company": " acme ", "title": " backend engineer ", "score": 95},
        ]
        expected = [
            {"company": " acme ", "title": " backend engineer ", "score": 95},
            {"company": "Beta", "title": "Platform Engineer", "score": 80},
        ]
        self.assertEqual(deduplicate_jobs(jobs), expected)

    def test_equal_score_keeps_first_occurrence(self):
        job1 = {"company": "Acme", "title": "Backend Engineer", "score": 90}
        job2 = {"company": " acme ", "title": " backend engineer ", "score": 90}
        jobs = [job1, job2]
        result = deduplicate_jobs(jobs)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], job1)

    def test_duplicate_group_keeps_original_group_position(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer", "score": 50},
            {"company": "Beta", "title": "Platform Engineer", "score": 80},
            {"company": "Gamma", "title": "DevOps", "score": 90},
            {"company": "ACME", "title": "backend engineer", "score": 95},
            {"company": "BETA", "title": "platform engineer", "score": 60},
        ]
        result = deduplicate_jobs(jobs)
        # First appearance sequence of keys: Acme, Beta, Gamma
        self.assertEqual(result[0]["company"], "ACME")
        self.assertEqual(result[0]["score"], 95)
        self.assertEqual(result[1]["company"], "Beta")
        self.assertEqual(result[1]["score"], 80)
        self.assertEqual(result[2]["company"], "Gamma")
        self.assertEqual(result[2]["score"], 90)

    def test_does_not_mutate_input_list_or_dictionaries(self):
        job1 = {"company": "Acme", "title": "Backend Engineer", "score": 70}
        job2 = {"company": "Beta", "title": "Platform Engineer", "score": 80}
        job3 = {"company": " acme ", "title": " backend engineer ", "score": 95}
        jobs = [job1, job2, job3]

        jobs_copy = [dict(j) for j in jobs]
        jobs_list_copy = list(jobs)

        deduplicate_jobs(jobs)

        self.assertEqual(jobs, jobs_list_copy)
        self.assertEqual(jobs, jobs_copy)


if __name__ == "__main__":
    unittest.main()
