"""
Multi-language support: language selector for interview questions.
"""
from PyQt5.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget


class LanguageSelector(QWidget):
    def __init__(self, languages=None):
        super().__init__()
        self.setWindowTitle("Language Selector")
        layout = QVBoxLayout(self)
        self.label = QLabel("Select Interview Language:")
        layout.addWidget(self.label)
        self.combo = QComboBox()
        self.languages = languages or ["Python", "Java", "C++"]
        self.combo.addItems(self.languages)
        layout.addWidget(self.combo)

    def get_selected_language(self):
        return self.combo.currentText()
