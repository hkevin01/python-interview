"""
Unit tests for InterviewApp GUI.
"""
import sys
import unittest

from PyQt5.QtWidgets import QApplication

from src.gui import InterviewApp


class TestInterviewApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def test_window_title(self):
        window = InterviewApp()
        self.assertEqual(window.windowTitle(), "Python Interview Assistant")

    def test_questions_loaded(self):
        window = InterviewApp()
        self.assertGreaterEqual(len(window.questions["beginner"]), 1)
        self.assertGreaterEqual(len(window.questions["intermediate"]), 1)
        self.assertGreaterEqual(len(window.questions["advanced"]), 1)

    def test_section_widgets(self):
        window = InterviewApp()
        for i, level in enumerate(["beginner", "intermediate", "advanced"]):
            section = window.stacked.widget(i)
            self.assertIsNotNone(section)


if __name__ == "__main__":
    unittest.main()
