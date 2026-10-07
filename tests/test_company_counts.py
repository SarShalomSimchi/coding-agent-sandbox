import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from company_counts import group_job_counts_by_company


class GroupJobCountsByCompanyTest(unittest.TestCase):
    def test_empty_input_returns_empty_dict(self):
        self.assertEqual(group_job_counts_by_company([]), {})

    def test_one_company(self):
        jobs = [{"company": "Acme", "title": "Backend Engineer"}]
        self.assertEqual(group_job_counts_by_company(jobs), {"Acme": 1})

    def test_repeated_company(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer"},
            {"company": "Acme", "title": "Platform Engineer"},
            {"company": "Acme", "title": "Data Engineer"},
        ]
        self.assertEqual(group_job_counts_by_company(jobs), {"Acme": 3})

    def test_multiple_companies(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer"},
            {"company": "Beta", "title": "Platform Engineer"},
            {"company": "Acme", "title": "Data Engineer"},
        ]
        self.assertEqual(group_job_counts_by_company(jobs), {"Acme": 2, "Beta": 1})

    def test_preserves_first_seen_key_order(self):
        jobs = [
            {"company": "Beta", "title": "A"},
            {"company": "Acme", "title": "B"},
            {"company": "Gamma", "title": "C"},
            {"company": "Beta", "title": "D"},
        ]
        self.assertEqual(
            list(group_job_counts_by_company(jobs).keys()),
            ["Beta", "Acme", "Gamma"],
        )

    def test_input_remains_unchanged(self):
        jobs = [
            {"company": "Acme", "title": "Backend Engineer"},
            {"company": "Beta", "title": "Platform Engineer"},
        ]
        snapshot = copy.deepcopy(jobs)
        group_job_counts_by_company(jobs)
        self.assertEqual(jobs, snapshot)


if __name__ == "__main__":
    unittest.main()
