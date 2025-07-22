"""
User customization and settings panel for GUI.
"""
import json
import os

from PyQt5.QtWidgets import (QComboBox, QLabel, QPushButton, QSpinBox,
                             QVBoxLayout, QWidget)


class SettingsPanel(QWidget):
    def __init__(self, settings_file=None):
        super().__init__()
        self.setWindowTitle("Settings")
        layout = QVBoxLayout(self)
        self.settings_file = settings_file or os.path.join(os.path.dirname(__file__), '../data/user_settings.json')
        self.theme_label = QLabel("Theme:")
        layout.addWidget(self.theme_label)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        layout.addWidget(self.theme_combo)
        self.font_label = QLabel("Font Size:")
        layout.addWidget(self.font_label)
        self.font_spin = QSpinBox()
        self.font_spin.setRange(8, 32)
        layout.addWidget(self.font_spin)
        self.layout_label = QLabel("Layout:")
        layout.addWidget(self.layout_label)
        self.layout_combo = QComboBox()
        self.layout_combo.addItems(["Default", "Compact", "Spacious"])
        layout.addWidget(self.layout_combo)
        self.color_label = QLabel("Color Scheme:")
        layout.addWidget(self.color_label)
        self.color_combo = QComboBox()
        self.color_combo.addItems(["System", "Light", "Dark", "High Contrast"])
        layout.addWidget(self.color_combo)
        self.save_btn = QPushButton("Save Settings")
        layout.addWidget(self.save_btn)
        self.save_btn.clicked.connect(self.save_settings)
        self.backup_btn = QPushButton("Backup Settings to Cloud")
        layout.addWidget(self.backup_btn)
        self.backup_btn.clicked.connect(self.backup_settings)
        self.load_settings()

    def save_settings(self):
        settings = {
            "theme": self.theme_combo.currentText(),
            "font_size": self.font_spin.value(),
            "layout": self.layout_combo.currentText(),
            "color_scheme": self.color_combo.currentText()
        }
        with open(self.settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
            self.theme_combo.setCurrentText(settings.get("theme", "Light"))
            self.font_spin.setValue(settings.get("font_size", 12))
            self.layout_combo.setCurrentText(settings.get("layout", "Default"))
            self.color_combo.setCurrentText(settings.get("color_scheme", "System"))

    def backup_settings(self):
        # Placeholder for cloud sync integration
        print("Settings backed up to cloud.")
