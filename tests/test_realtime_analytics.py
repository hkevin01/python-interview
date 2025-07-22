"""
Unit test for RealTimeAnalyticsDashboard.
"""
import unittest

from src.realtime_analytics import RealTimeAnalyticsDashboard


class TestRealTimeAnalyticsDashboard(unittest.TestCase):
    def test_dashboard_creation(self):
        try:
            dashboard = RealTimeAnalyticsDashboard()
            self.assertIsNotNone(dashboard)
        except (RuntimeError, ImportError) as e:
            import logging
            logging.error("Dashboard creation failed: %s", e)
            self.fail(f"Dashboard creation failed: {e}")


if __name__ == "__main__":
    unittest.main()
