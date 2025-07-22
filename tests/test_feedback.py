"""
Unit test for FeedbackManager.
"""
import json
import os
import unittest

from src.feedback import FeedbackManager


class TestFeedbackManager(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_feedback.json'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump([], f)
        self.manager = FeedbackManager(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_submit_and_get_feedback(self):
        self.manager.submit_feedback('Q1', 5, 'Great question!')
        feedback = self.manager.get_feedback()
        self.assertEqual(len(feedback), 1)
        self.assertEqual(feedback[0]['rating'], 5)
        self.assertEqual(feedback[0]['comment'], 'Great question!')

    def test_analyze_feedback(self):
        self.manager.submit_feedback('Q1', 4, 'Good')
        self.manager.submit_feedback('Q2', 2, 'Needs work')
        analysis = self.manager.analyze_feedback()
        self.assertEqual(analysis['total'], 2)
        self.assertAlmostEqual(analysis['average_rating'], 3.0)

if __name__ == "__main__":
    unittest.main()
