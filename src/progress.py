"""
User progress tracking for Python Interview Assistant.
"""
import json
import os

from src.logging_utils import log_error

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')

def load_progress():
    try:
        if not os.path.exists(PROGRESS_FILE):
            return {}
        with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        log_error(f"Load progress error: {e}")
        return {}

def save_progress(progress):
    try:
        with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
            json.dump(progress, f, indent=2)
    except Exception as e:
        log_error(f"Save progress error: {e}")

def mark_answered(level, question):
    try:
        progress = load_progress()
        if level not in progress:
            progress[level] = []
        if question not in progress[level]:
            progress[level].append(question)
        save_progress(progress)
    except Exception as e:
        log_error(f"Mark answered error: {e}")

def get_completion_status():
    try:
        progress = load_progress()
        return progress
    except Exception as e:
        log_error(f"Get completion status error: {e}")
        return {}
