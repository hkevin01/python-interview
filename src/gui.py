"""
PyQt GUI layout and navigation for Python Interview Assistant.
"""
import json
import os

from PyQt5.QtGui import QColor, QFont, QTextCharFormat, QTextCursor
from PyQt5.QtWidgets import (QLabel, QLineEdit, QMainWindow, QPushButton,
                             QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

from search import search_questions
from src.cpp_questions import questions as cpp_questions
from src.java_questions import questions as java_questions
from src.language_selector import LanguageSelector
from src.logging_utils import log_error
from src.settings import SettingsPanel


class InterviewApp(QMainWindow):
    """
    Main application window for the Python Interview Assistant GUI.
    """

    def __init__(self):
        """
        Initialize the main window, layout, navigation, and sections.
        """
        super().__init__()
        self.setWindowTitle("Python Interview Assistant")
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search questions...")
        layout.addWidget(self.search_bar)
        self.search_bar.textChanged.connect(self.update_search_results)
        self.stacked = QStackedWidget()
        layout.addWidget(self.stacked)
        self.init_navigation(layout)
        self.questions = self.load_questions()
        self.init_sections()
        self.search_results_widget = QWidget()
        self.search_results_layout = QVBoxLayout(self.search_results_widget)
        self.stacked.addWidget(self.search_results_widget)

    def load_questions(self, language='Python'):
        """
        Load interview questions from the data file or language module.
        """
        if language == 'Python':
            path = os.path.join(os.path.dirname(__file__), '../data/questions.json')
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif language == 'Java':
            return {'java': java_questions}
        elif language == 'C++':
            return {'cpp': cpp_questions}
        else:
            return {}

    def highlight_python_code(self, text_edit, code):
        """
        Apply basic Python syntax highlighting to the given QTextEdit.
        """
        text_edit.setPlainText(code)
        cursor = text_edit.textCursor()
        fmt_keyword = QTextCharFormat()
        fmt_keyword.setForeground(QColor('blue'))
        fmt_keyword.setFontWeight(QFont.Bold)
        fmt_string = QTextCharFormat()
        fmt_string.setForeground(QColor('darkGreen'))
        fmt_comment = QTextCharFormat()
        fmt_comment.setForeground(QColor('darkGray'))
        keywords = [
            'def', 'class', 'import', 'from', 'return', 'if', 'else', 'elif',
            'for', 'while', 'try', 'except', 'with', 'as', 'pass', 'break',
            'continue', 'in', 'is', 'not', 'and', 'or', 'lambda', 'yield',
            'global', 'nonlocal', 'assert', 'del', 'raise', 'True', 'False',
            'None'
        ]
        cursor.movePosition(QTextCursor.Start)
        code_lines = code.split('\n')
        for line in code_lines:
            # Highlight comments
            if '#' in line:
                idx = line.index('#')
                cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor,
                    idx)
                cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
                    len(line) - idx)
                cursor.mergeCharFormat(fmt_comment)
                cursor.movePosition(QTextCursor.EndOfLine)
            # Highlight strings
            pos = 0
            while pos < len(line):
                if line[pos] in ['"', "'"]:
                    quote = line[pos]
                    start = pos
                    pos += 1
                    while pos < len(line) and line[pos] != quote:
                        pos += 1
                    end = pos
                    cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor,
                        start)
                    cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
                        end - start + 1)
                    cursor.mergeCharFormat(fmt_string)
                    cursor.movePosition(QTextCursor.EndOfLine)
                pos += 1
            # Highlight keywords
            for kw in keywords:
                idx = line.find(kw)
                if idx != -1:
                    cursor.movePosition(QTextCursor.Right, QTextCursor.MoveAnchor,
                        idx)
                    cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor,
                        len(kw))
                    cursor.mergeCharFormat(fmt_keyword)
                    cursor.movePosition(QTextCursor.EndOfLine)
        cursor.movePosition(QTextCursor.Start)

    def update_search_results(self, text):
        """
        Update the search results widget with filtered questions and answers.
        """
        try:
            # Clear previous results
            for i in reversed(range(self.search_results_layout.count())):
                item = self.search_results_layout.itemAt(i)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        widget.setParent(None)
            if text.strip():
                results = search_questions(text)
                for r in results:
                    q_label = QLabel(
                        f"[{r['level'].capitalize()}] Q: {r['question']}")
                    self.search_results_layout.addWidget(q_label)
                    a_text = QTextEdit(r['answer'])
                    a_text.setReadOnly(True)
                    a_text.hide()
                    self.search_results_layout.addWidget(a_text)
                    a_btn = QPushButton("Show Answer")
                    self.search_results_layout.addWidget(a_btn)
                    a_btn.clicked.connect(lambda checked, t=a_text:
                        t.setVisible(True))
                    # Show code sample
                    if 'code' in r:
                        code_btn = QPushButton("Show Code Example")
                        self.search_results_layout.addWidget(code_btn)
                        code_text = QTextEdit()
                        code_text.setReadOnly(True)
                        code_text.hide()
                        self.highlight_python_code(code_text, r['code'])
                        self.search_results_layout.addWidget(code_text)
                        code_btn.clicked.connect(lambda checked, t=code_text:
                            t.setVisible(True))
                self.stacked.setCurrentWidget(self.search_results_widget)
            else:
                self.stacked.setCurrentIndex(0)
        except Exception as e:
            log_error(f"Search error: {e}")

    def init_navigation(self, layout):
        """
        Initialize navigation buttons for difficulty sections and language selector.
        """
        self.nav_label = QLabel("Select Section:")
        layout.addWidget(self.nav_label)
        self.language_selector = LanguageSelector()
        layout.addWidget(self.language_selector)
        self.btn_beginner = QPushButton("Beginner")
        self.btn_intermediate = QPushButton("Intermediate")
        self.btn_advanced = QPushButton("Advanced")
        layout.addWidget(self.btn_beginner)
        layout.addWidget(self.btn_intermediate)
        layout.addWidget(self.btn_advanced)
        self.btn_beginner.clicked.connect(
            lambda: self.stacked.setCurrentIndex(0)
        )
        self.btn_intermediate.clicked.connect(
            lambda: self.stacked.setCurrentIndex(1)
        )
        self.btn_advanced.clicked.connect(
            lambda: self.stacked.setCurrentIndex(2)
        )
        self.language_selector.combo.currentTextChanged.connect(self.change_language)
        self.settings_btn = QPushButton("Settings")
        layout.addWidget(self.settings_btn)
        self.settings_btn.clicked.connect(self.open_settings)

    def open_settings(self):
        self.settings_panel = SettingsPanel()
        self.settings_panel.show()

    def change_language(self, language):
        """
        Change the language of the interview questions displayed.
        """
        try:
            self.questions = self.load_questions(language)
            self.stacked.clear()
            self.init_sections()
        except Exception as e:
            log_error(f"Language change error: {e}")

    def init_sections(self):
        """
        Add section widgets for each difficulty level.
        """
        self.stacked.addWidget(self.section_widget("beginner"))
        self.stacked.addWidget(self.section_widget("intermediate"))
        self.stacked.addWidget(self.section_widget("advanced"))

    def section_widget(self, level):
        """
        Create a widget for a given difficulty level with questions and answers.
        """
        widget = QWidget()
        layout = QVBoxLayout(widget)
        questions = self.questions.get(level, [])
        for q in questions:
            q_label = QLabel(f"Q: {q['question']}")
            layout.addWidget(q_label)
            a_btn = QPushButton("Show Answer")
            layout.addWidget(a_btn)
            a_text = QTextEdit(q['answer'])
            a_text.setReadOnly(True)
            a_text.hide()
            layout.addWidget(a_text)
            a_btn.clicked.connect(lambda checked, t=a_text:
                t.setVisible(True))
            # Show code sample
            if 'code' in q:
                code_btn = QPushButton("Show Code Example")
                layout.addWidget(code_btn)
                code_text = QTextEdit()
                code_text.setReadOnly(True)
                code_text.hide()
                self.highlight_python_code(code_text, q['code'])
                layout.addWidget(code_text)
                code_btn.clicked.connect(lambda checked, t=code_text:
                    t.setVisible(True))
        return widget
