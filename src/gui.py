"""
PyQt GUI layout and navigation for Python Interview Assistant.
"""
import json
import os
import sys
import traceback

from PyQt5.QtGui import (QColor, QFont, QKeySequence, QTextCharFormat,
                         QTextCursor)
from PyQt5.QtWidgets import (QLabel, QLineEdit, QMainWindow, QMessageBox,
                             QPushButton, QShortcut, QStackedWidget, QTextEdit,
                             QVBoxLayout, QWidget)

from cloud_sync import CloudSync
from cpp_questions import questions as cpp_questions
from error_monitor import ErrorMonitor
from java_questions import questions as java_questions
from language_selector import LanguageSelector
from logging_utils import log_error
from realtime_analytics import RealTimeAnalyticsDashboard
from search import search_questions
from settings import SettingsPanel


# Error handling decorator
def safe_button_handler(func):
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
            traceback.print_exc()
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")
    return wrapper


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
        self.settings_panel = None
        self.analytics_window = None
        self.error_monitor = None
        self.cloud_sync = None
        self.questions = self.load_questions()
        self.debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'
        self.init_navigation(layout)
        self.init_sections()
        self.search_results_widget = QWidget()
        self.search_results_layout = QVBoxLayout(self.search_results_widget)
        self.stacked.addWidget(self.search_results_widget)
        self.setup_error_handling()
        self.setup_shortcuts()

    def setup_error_handling(self):
        sys.excepthook = self.handle_exception

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        error_msg = ''.join(traceback.format_exception(
            exc_type, exc_value, exc_traceback))
        print(f"Uncaught exception: {error_msg}")
        QMessageBox.critical(
            self, "Critical Error",
            f"A critical error occurred:\n{exc_value}")

    def setup_shortcuts(self):
        QShortcut(QKeySequence("Ctrl+Right"), self, self.next_question)
        QShortcut(QKeySequence("Ctrl+Left"), self, self.previous_question)
        QShortcut(QKeySequence("Space"), self, self.show_answer)
        QShortcut(QKeySequence("Ctrl+B"), self, self.bookmark_question)
        QShortcut(QKeySequence("Ctrl+S"), self, self.open_cloud_sync)
        QShortcut(QKeySequence("F1"), self, self.show_help)

    def show_help(self):
        help_text = """
        Keyboard Shortcuts:
        Ctrl+Right - Next Question
        Ctrl+Left - Previous Question
        Space - Show/Hide Answer
        Ctrl+B - Bookmark Question
        Ctrl+S - Sync to Cloud
        F1 - Show this help
        """
        QMessageBox.information(self, "Help", help_text)

    def debug_print(self, message):
        if self.debug_mode:
            print(f"DEBUG: {message}")

    def show_debug_info(self):
        if not self.debug_mode:
            return
        debug_info = (
            f"Current Question Index: {getattr(self, 'current_question_index', 'None')}\n"
            f"Current Difficulty: {getattr(self, 'current_difficulty', 'None')}\n"
            f"Questions Loaded: {len(self.questions) if hasattr(self, 'questions') else 0}\n"
            f"User Progress Loaded: {bool(getattr(self, 'user_progress', None))}\n"
        )
        QMessageBox.information(self, "Debug Info", debug_info)

    def load_questions(self, language='Python'):
        """
        Load interview questions from the data file or language module.
        """
        if language == 'Python':
            base = os.path.dirname(__file__)
            path = os.path.join(base, '../data/questions.json')
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
        self.btn_beginner.clicked.connect(self.safe_load_beginner)
        self.btn_intermediate.clicked.connect(
            lambda: self.stacked.setCurrentIndex(1)
        )
        self.btn_advanced.clicked.connect(
            lambda: self.stacked.setCurrentIndex(2)
        )
        self.language_selector.combo.currentTextChanged.connect(
            self.change_language)
        self.settings_btn = QPushButton("Settings")
        layout.addWidget(self.settings_btn)
        self.settings_btn.clicked.connect(self.open_settings)
        self.analytics_btn = QPushButton("Real-Time Analytics")
        layout.addWidget(self.analytics_btn)
        self.analytics_btn.clicked.connect(self.open_analytics)
        self.error_btn = QPushButton("Error Monitor")
        layout.addWidget(self.error_btn)
        self.error_btn.clicked.connect(self.open_error_monitor)
        self.cloud_btn = QPushButton("Cloud Sync")
        layout.addWidget(self.cloud_btn)
        self.cloud_btn.clicked.connect(self.open_cloud_sync)

    def safe_load_beginner(self):
        """Safely load beginner questions using QTimer to avoid threading issues."""
        from PyQt5.QtCore import QTimer
        QTimer.singleShot(0, self.load_beginner_questions)

    def load_beginner_questions(self):
        try:
            self.current_difficulty = 'beginner'
            self.current_question_index = 0
            self.ensure_questions_loaded()
            self.show_current_question()
            self.stacked.setCurrentIndex(0)
        except Exception as e:
            print(f"Error loading beginner questions: {e}")

    def ensure_questions_loaded(self):
        if not hasattr(self, 'questions') or not self.questions:
            self.questions = self.get_default_questions()

    def show_current_question(self):
        try:
            current_questions = self.questions.get(self.current_difficulty, [])
            if current_questions and self.current_question_index < len(current_questions):
                question = current_questions[self.current_question_index]
                # If you have a question display widget, update it here
                # For demonstration, just print
                print(f"Current question: {question.get('question', '')}")
            else:
                print(f"No {self.current_difficulty} questions available")
        except Exception as e:
            print(f"Error showing current question: {e}")

    def get_default_questions(self):
        return {
            "beginner": [
                {
                    "id": 1,
                    "question": "What is Python?",
                    "answer": "Python is a high-level, interpreted programming language."
                }
            ],
            "intermediate": [],
            "advanced": []
        }

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

    def open_analytics(self):
        """
        Open the real-time analytics dashboard with error handling.
        """
        try:
            self.analytics_window = RealTimeAnalyticsDashboard()
            self.analytics_window.show()
        except (RuntimeError, ImportError) as e:
            log_error(f"Analytics dashboard error: {e}")
            QMessageBox.critical(self, "Analytics Error", str(e))

    def open_error_monitor(self):
        self.error_monitor = ErrorMonitor()
        # For demonstration, show errors in a message box
        errors = self.error_monitor.get_errors()
        msg = '\n'.join(errors) if errors else 'No errors reported.'
        QMessageBox.information(self, "Error Monitor", msg)

    @safe_button_handler
    def open_cloud_sync(self):
        try:
            data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
            os.makedirs(data_dir, exist_ok=True)
            progress_file = os.path.join(data_dir, 'user_progress.json')
            if not os.path.exists(progress_file):
                self.create_default_progress_file(progress_file)
            self.cloud_sync = CloudSync(progress_file)
            self.cloud_sync.sync_to_cloud()
            msg = "Progress synced to cloud."
            QMessageBox.information(self, "Cloud Sync", msg)
        except Exception as e:
            print(f"Error in cloud sync: {e}")
            msg = f"Unable to sync to cloud: {str(e)}"
            QMessageBox.warning(self, "Cloud Sync Error", msg)

    def create_default_progress_file(self, file_path):
        default_data = {
            "completed_questions": [],
            "bookmarked_questions": [],
            "user_stats": {
                "total_answered": 0,
                "correct_answers": 0,
                "sessions": 0,
                "last_session": None
            },
            "preferences": {
                "theme": "default",
                "auto_save": True,
                "show_hints": True
            }
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=4)

    @safe_button_handler
    def show_answer(self):
        # Placeholder for answer display logic
        pass

    @safe_button_handler
    def next_question(self):
        pass

    @safe_button_handler
    def previous_question(self):
        pass

    @safe_button_handler
    def bookmark_question(self):
        pass

    @safe_button_handler
    def filter_by_difficulty(self):
        pass

    @safe_button_handler
    def search_questions(self):
        pass

    def load_default_questions(self):
        self.questions = {
            "beginner": [
                {
                    "id": 1,
                    "question": "What is Python?",
                    "answer": "Python is a high-level, interpreted programming language."
                }
            ],
            "intermediate": [],
            "advanced": []
        }
