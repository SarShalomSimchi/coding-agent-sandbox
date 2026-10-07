import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from company_tools import normalize_company_name


class NormalizeCompanyNameTest(unittest.TestCase):
    def test_plain_string(self):
        self.assertEqual(normalize_company_name("Example"), "example")

    def test_trims_leading_and_trailing_whitespace(self):
        self.assertEqual(normalize_company_name("  Acme Corp  "), "acme corp")

    def test_collapses_repeated_whitespace(self):
        self.assertEqual(
            normalize_company_name("Acme\t\tCorp\n\nHoldings   Inc"),
            "acme corp holdings inc",
        )

    def test_mixed_case(self):
        self.assertEqual(normalize_company_name("ACME Corp"), "acme corp")

    def test_whitespace_only_input(self):
        self.assertEqual(normalize_company_name("   \t\n  "), "")

    def test_empty_input(self):
        self.assertEqual(normalize_company_name(""), "")


if __name__ == "__main__":
    unittest.main()
