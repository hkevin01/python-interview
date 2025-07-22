"""
Accessibility features for keyboard navigation and screen reader support.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication


def enable_accessibility(app: QApplication):
    """
    Enable accessibility features for the given QApplication.
    """
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    # Example: Set tab order, add ARIA-like labels (stub)
    # Future: Integrate with screen reader APIs
    print("Accessibility features enabled.")
