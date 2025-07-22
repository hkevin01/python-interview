"""
Main entry point for the Python Interview Assistant GUI.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

from src.gui import InterviewApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == "--analytics":
        from src.analytics import AnalyticsDashboard
        window = AnalyticsDashboard()
        window.show()
        sys.exit(app.exec_())
    try:
        window = InterviewApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        QMessageBox.critical(None, "Startup Error", str(e))
        sys.exit(1)
