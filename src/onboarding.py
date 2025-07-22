"""
Onboarding and tutorial screens for new users.
"""
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from src.logging_utils import log_action, log_error


class OnboardingScreen(QWidget):
    def __init__(self):
        try:
            super().__init__()
            self.setWindowTitle("Welcome to Python Interview Assistant!")
            layout = QVBoxLayout(self)
            self.intro_label = QLabel("Get started with a quick tour of the app features.")
            layout.addWidget(self.intro_label)
            self.tutorial_label = QLabel("- Browse questions by difficulty and language.\n- Reveal answers and code samples.\n- Track your progress and feedback.\n- Customize your experience in Settings.")
            layout.addWidget(self.tutorial_label)
            self.start_btn = QPushButton("Start Using App")
            layout.addWidget(self.start_btn)
            self.start_btn.clicked.connect(self.close_onboarding)
            log_action("Onboarding screen shown.")
        except Exception as e:
            log_error(f"Onboarding error: {e}")

    def close_onboarding(self):
        log_action("Onboarding closed.")
        self.close()
