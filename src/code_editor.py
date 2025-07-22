"""
Code editor widget for user practice and code attempts.
"""
from PyQt5.QtWidgets import (QLabel, QPushButton, QTextEdit, QVBoxLayout,
                             QWidget)

from src.logging_utils import log_action, log_error


class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Practice Code Editor")
        layout = QVBoxLayout(self)
        self.label = QLabel("Write and test your code below:")
        layout.addWidget(self.label)
        self.editor = QTextEdit()
        layout.addWidget(self.editor)
        self.run_btn = QPushButton("Run Code")
        layout.addWidget(self.run_btn)
        self.output_label = QLabel("")
        layout.addWidget(self.output_label)
        self.run_btn.clicked.connect(self.run_code)

    def run_code(self):
        code = self.editor.toPlainText()
        try:
            exec_globals = {}
            exec(code, exec_globals)
            self.output_label.setText("Code executed successfully.")
            log_action("User ran code in editor.")
        except Exception as e:
            self.output_label.setText(f"Error: {e}")
            log_error(f"Code editor error: {e}")

    def show_feedback(self, feedback):
        """
        Display AI code review feedback in the editor output label.
        """
        msg = ""
        if feedback.get("errors"):
            msg += "Errors:\n" + "\n".join(feedback["errors"]) + "\n"
        if feedback.get("suggestions"):
            msg += "Suggestions:\n" + "\n".join(feedback["suggestions"]) + "\n"
        if feedback.get("improvements"):
            improvements = "\n".join(feedback["improvements"])
            msg += f"Improvements:\n{improvements}\n"
        self.output_label.setText(msg or "No feedback.")
