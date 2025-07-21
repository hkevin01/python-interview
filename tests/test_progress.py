"""
Unit tests for user progress tracking.
"""
import os
import unittest

from src.progress import (get_completion_status, load_progress, mark_answered,
                          save_progress)


class TestProgress(unittest.TestCase):
    def setUp(self):
        # Ensure a clean progress file
        progress_file = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')
        if os.path.exists(progress_file):
            os.remove(progress_file)

    def test_mark_answered(self):
        mark_answered('beginner', 'What is a variable in Python?')
        progress = load_progress()
        self.assertIn('beginner', progress)
        self.assertIn('What is a variable in Python?', progress['beginner'])

    def test_get_completion_status(self):
        mark_answered('intermediate', 'Explain list comprehensions in Python.')
        status = get_completion_status()
        self.assertIn('intermediate', status)
        self.assertIn('Explain list comprehensions in Python.', status['intermediate'])

if __name__ == "__main__":
    unittest.main()
