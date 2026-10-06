import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from keyword_tools import normalize_keyword, normalize_keywords


class NormalizeKeywordTest(unittest.TestCase):
    def test_trims_lowercases_and_collapses_spaces(self):
        self.assertEqual(normalize_keyword("  Senior   Backend  "), "senior backend")

    def test_empty_input(self):
        self.assertEqual(normalize_keyword("   "), "")


class NormalizeKeywordsTest(unittest.TestCase):
    def test_normalize_keywords_example(self):
        raw = ["  Python ", "JAVA", "python", " ", "  Java  "]
        expected = ["python", "java"]
        self.assertEqual(normalize_keywords(raw), expected)

    def test_does_not_mutate_input_list(self):
        raw = ["  Python ", "JAVA", "python"]
        raw_copy = list(raw)
        normalize_keywords(raw)
        self.assertEqual(raw, raw_copy)

    def test_discards_empty_and_whitespace_only_strings(self):
        raw = ["", "   ", "\t", "\n", "valid"]
        self.assertEqual(normalize_keywords(raw), ["valid"])

    def test_preserves_first_occurrence_order(self):
        raw = [" C++ ", " Python ", "c++", "Java", "python", " C++ "]
        self.assertEqual(normalize_keywords(raw), ["c++", "python", "java"])


if __name__ == "__main__":
    unittest.main()
