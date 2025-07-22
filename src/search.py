"""
Search and filter functionality for interview questions.
"""
import json
import os

from logging_utils import log_error


def load_questions():
    path = os.path.join(os.path.dirname(__file__), '../data/questions.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def search_questions(query, level=None):
    try:
        questions = load_questions()
        results = []
        levels = [level] if level else questions.keys()
        for lvl in levels:
            for q in questions[lvl]:
                if query.lower() in q['question'].lower() or query.lower() in q['answer'].lower():
                    result = {
                        'level': lvl,
                        'question': q['question'],
                        'answer': q['answer']
                    }
                    if 'code' in q:
                        result['code'] = q['code']
                    results.append(result)
        return results
    except Exception as e:
        log_error(f"Search function error: {e}")
        return []
