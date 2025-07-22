"""
Unit tests for AnalyticsDashboard.
"""
import os
import unittest

from src.analytics import AnalyticsDashboard


class TestAnalyticsDashboard(unittest.TestCase):
    def test_dashboard_creation(self):
        # Should create dashboard without error (matplotlib may be missing)
        try:
            dashboard = AnalyticsDashboard()
            self.assertIsNotNone(dashboard)
        except Exception as e:
            self.fail(f"AnalyticsDashboard creation failed: {e}")

if __name__ == "__main__":
    unittest.main()
