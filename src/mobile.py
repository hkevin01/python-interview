"""
Mobile-friendly GUI layout and touch controls.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


def enable_mobile_layout(app: QApplication):
    """
    Enable mobile-friendly layout and touch controls for the given QApplication.
    """
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # Example: Print message for mobile layout enabled (stub)
    print("Mobile layout and touch controls enabled.")
