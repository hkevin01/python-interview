"""
Script to add a new interview question to data/questions.json.
"""
import json
import os
import sys


def add_question(level, question, answer):
    path = os.path.join(os.path.dirname(__file__), '../data/questions.json')
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if level not in data:
        data[level] = []
    data[level].append({'question': question, 'answer': answer})
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python add_question.py <level> <question> <answer>")
        sys.exit(1)
    add_question(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Question added.")
