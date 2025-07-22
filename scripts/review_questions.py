"""
Script to review and approve community-submitted questions.
"""
import json
import os

from src.community import approve_question, review_pending_questions


def main():
    pending = review_pending_questions()
    if not pending:
        print('No pending questions.')
        return
    for i, q in enumerate(pending, 1):
        print(f"[{i}] Level: {q['level']}\nQ: {q['question']}\nA: {q['answer']}\nCode: {q.get('code', '')}\n")
    
    prompt = (
        'Enter the number of the question to approve '
        '(or blank to skip): '
    )
    idx = input(prompt)
    if idx.strip():
        try:
            idx_int = int(idx) - 1
            if approve_question(idx_int):
                print('Question approved and moved to main dataset.')
            else:
                print('Invalid index or error approving question.')
        except ValueError:
            print('Invalid input. Please enter a number.')


if __name__ == "__main__":
    main()
