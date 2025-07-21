"""
Unit tests for search and filter functionality.
"""
import unittest

from src.search import search_questions


class TestSearchQuestions(unittest.TestCase):
    def test_search_by_keyword(self):
        results = search_questions("variable")
        self.assertTrue(any("variable" in r["question"].lower() for r in results))

    def test_search_by_level(self):
        results = search_questions("function", level="beginner")
        self.assertTrue(all(r["level"] == "beginner" for r in results))

    def test_search_no_results(self):
        results = search_questions("nonexistentkeyword")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
