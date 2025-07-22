"""
PDF viewer widget for displaying exported Q&A and progress.
"""
import os

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class PDFViewer(QWidget):
    def __init__(self, pdf_file=None):
        super().__init__()
        self.setWindowTitle("PDF Viewer")
        layout = QVBoxLayout(self)
        self.label = QLabel("View your exported PDF below:")
        layout.addWidget(self.label)
        self.viewer = QWebEngineView()
        layout.addWidget(self.viewer)
        if pdf_file and os.path.exists(pdf_file):
            self.viewer.load(f"file://{os.path.abspath(pdf_file)}")
