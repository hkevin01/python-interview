"""
Community question submission and review logic.
"""
import json
import os


def submit_question(level, question, answer, code=None):
    """
    Submit a new question for review and inclusion.
    """
    pending_file = os.path.join(os.path.dirname(__file__), '../data/pending_questions.json')
    entry = {'level': level, 'question': question, 'answer': answer}
    if code:
        entry['code'] = code
    if not os.path.exists(pending_file):
        with open(pending_file, 'w', encoding='utf-8') as f:
            json.dump([], f)
    with open(pending_file, 'r', encoding='utf-8') as f:
        pending = json.load(f)
    pending.append(entry)
    with open(pending_file, 'w', encoding='utf-8') as f:
        json.dump(pending, f, indent=2)
    return True

def review_pending_questions():
    """
    Return all pending questions for review.
    """
    pending_file = os.path.join(os.path.dirname(__file__), '../data/pending_questions.json')
    if not os.path.exists(pending_file):
        return []
    with open(pending_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def approve_question(index):
    """
    Approve a pending question and move it to the main dataset.
    """
    base_dir = os.path.dirname(__file__)
    pending_file = os.path.join(base_dir, '../data/pending_questions.json')
    questions_file = os.path.join(base_dir, '../data/questions.json')
    if not os.path.exists(pending_file):
        return False
    with open(pending_file, 'r', encoding='utf-8') as f:
        pending = json.load(f)
    if index < 0 or index >= len(pending):
        return False
    entry = pending.pop(index)
    # Add to main dataset
    with open(questions_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    level = entry.get('level', 'beginner')
    if level not in data:
        data[level] = []
    data[level].append(entry)
    with open(questions_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    # Update pending file
    with open(pending_file, 'w', encoding='utf-8') as f:
        json.dump(pending, f, indent=2)
    return True
