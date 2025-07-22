"""
Unit test for RealTimeAnalyticsDashboard.
"""
import unittest

from src.realtime_analytics import RealTimeAnalyticsDashboard


class TestRealTimeAnalyticsDashboard(unittest.TestCase):
    def test_dashboard_creation(self):
        dashboard = RealTimeAnalyticsDashboard()
        self.assertIsNotNone(dashboard)

if __name__ == "__main__":
    unittest.main()
