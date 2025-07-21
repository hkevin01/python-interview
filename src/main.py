"""
Main entry point for the Python Interview Assistant GUI.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMessageBox

from gui import InterviewApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        window = InterviewApp()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        QMessageBox.critical(None, "Startup Error", str(e))
        sys.exit(1)
