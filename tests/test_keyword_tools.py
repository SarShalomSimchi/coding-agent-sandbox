import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from keyword_tools import normalize_keyword


class NormalizeKeywordTest(unittest.TestCase):
    def test_trims_lowercases_and_collapses_spaces(self):
        self.assertEqual(normalize_keyword("  Senior   Backend  "), "senior backend")

    def test_empty_input(self):
        self.assertEqual(normalize_keyword("   "), "")


if __name__ == "__main__":
    unittest.main()
