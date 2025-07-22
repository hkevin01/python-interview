"""
Advanced analytics: user strengths/weaknesses heatmap visualization.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class HeatmapAnalytics(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.setWindowTitle("User Strengths/Weaknesses Heatmap")
        layout = QVBoxLayout(self)
        self.label = QLabel("Heatmap of your performance by topic:")
        layout.addWidget(self.label)
        self.figure = plt.Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.data = data or np.random.rand(5, 5)
        self.plot_heatmap()

    def plot_heatmap(self):
        ax = self.figure.add_subplot(111)
        ax.clear()
        cax = ax.imshow(self.data, cmap='coolwarm', interpolation='nearest')
        self.figure.colorbar(cax)
        ax.set_title('Performance Heatmap')
        self.canvas.draw()
