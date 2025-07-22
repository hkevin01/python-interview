"""
Analytics dashboard for user progress and strengths/weaknesses visualization.
"""
import json
import os

try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_qt5agg import \
        FigureCanvasQTAgg as FigureCanvas
    from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
except ImportError:
    QWidget = QVBoxLayout = QLabel = plt = FigureCanvas = None

class AnalyticsDashboard(QWidget):
    def __init__(self, progress_file=None):
        super().__init__()
        self.setWindowTitle("Analytics Dashboard")
        layout = QVBoxLayout(self)
        self.progress_file = progress_file or os.path.join(os.path.dirname(__file__), '../data/user_progress.json')
        self.status_label = QLabel("User Progress Overview")
        layout.addWidget(self.status_label)
        if plt and FigureCanvas:
            self.figure = plt.Figure()
            self.canvas = FigureCanvas(self.figure)
            layout.addWidget(self.canvas)
            self.plot_progress()
        else:
            layout.addWidget(QLabel("matplotlib not available"))

    def plot_progress(self):
        with open(self.progress_file, 'r', encoding='utf-8') as f:
            progress = json.load(f)
        levels = list(progress.keys())
        counts = [len(progress[lvl]) for lvl in levels]
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.bar(levels, counts, color=['#4caf50', '#2196f3', '#f44336'])
        ax.set_ylabel('Questions Answered')
        ax.set_title('Progress by Difficulty')
        self.canvas.draw()
