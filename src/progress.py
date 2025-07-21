"""
User progress tracking for Python Interview Assistant.
"""
import json
import os

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {}
    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_progress(progress):
    with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
        json.dump(progress, f, indent=2)

def mark_answered(level, question):
    progress = load_progress()
    if level not in progress:
        progress[level] = []
    if question not in progress[level]:
        progress[level].append(question)
    save_progress(progress)

def get_completion_status():
    progress = load_progress()
    return progress
