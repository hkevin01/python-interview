"""
Main entry point for the Python Interview Assistant GUI.
"""
import os
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

# Ensure src is in sys.path for direct execution
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
src_path = os.path.join(project_root, 'src')
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from gui import InterviewApp

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
