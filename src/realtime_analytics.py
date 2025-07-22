"""
Real-time analytics and dashboard for user progress.
"""
import threading
import time

from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class RealTimeAnalyticsDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Analytics Dashboard")
        layout = QVBoxLayout(self)
        self.status_label = QLabel("Live Progress Updates")
        layout.addWidget(self.status_label)
        self.live_label = QLabel("")
        layout.addWidget(self.live_label)
        self._running = True
        self._thread = threading.Thread(target=self._update_live_data)
        self._thread.start()

    def _update_live_data(self):
        while self._running:
            # Simulate live data update
            self.live_label.setText(f"Questions answered: {int(time.time()) % 100}")
            time.sleep(1)

    def closeEvent(self, event):
        self._running = False
        self._thread.join()
        event.accept()
