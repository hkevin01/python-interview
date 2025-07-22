"""
Unit test for ErrorMonitor.
"""
import unittest

from src.error_monitor import ErrorMonitor


class TestErrorMonitor(unittest.TestCase):
    def test_error_reporting(self):
        monitor = ErrorMonitor()
        monitor.report_error("Test error")
        self.assertIn("Test error", monitor.get_errors())
        analysis = monitor.analyze_errors()
        self.assertEqual(analysis["total"], 1)
        self.assertEqual(analysis["unique"], 1)

if __name__ == "__main__":
    unittest.main()
