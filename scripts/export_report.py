"""
Script to export user progress and questions to CSV files.
"""
import os

from src.export import export_progress_to_csv, export_questions_to_csv


def main():
    progress_file = os.path.join(os.path.dirname(__file__), '../data/user_progress.json')
    questions_file = os.path.join(os.path.dirname(__file__), '../data/questions.json')
    export_progress_to_csv(progress_file, 'user_progress.csv')
    export_questions_to_csv(questions_file, 'questions.csv')
    print('Export complete: user_progress.csv, questions.csv')

if __name__ == "__main__":
    main()
