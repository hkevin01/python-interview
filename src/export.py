"""
Export and report generation for Q&A history and user progress.
"""
import json
import os


def export_progress_to_csv(progress_file, output_file):
    with open(progress_file, 'r', encoding='utf-8') as f:
        progress = json.load(f)
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write('level,question\n')
        for level, questions in progress.items():
            for q in questions:
                out.write(f'{level},{q}\n')

def export_questions_to_csv(questions_file, output_file):
    with open(questions_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    with open(output_file, 'w', encoding='utf-8') as out:
        out.write('level,question,answer,code\n')
        for level, qlist in questions.items():
            for q in qlist:
                code = q.get('code', '').replace('\n', ' ')
                out.write(f'{level},{q['question']},{q['answer']},{code}\n')
