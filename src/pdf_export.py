"""
Export Q&A and progress to PDF.
"""
import json
import os

from fpdf import FPDF


class PDFExporter:
    def __init__(self, output_file='output.pdf'):
        self.output_file = output_file
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def export_questions(self, questions_file):
        with open(questions_file, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(0, 10, 'Interview Questions', ln=True)
        self.pdf.set_font('Arial', '', 12)
        for level, qlist in questions.items():
            self.pdf.cell(0, 10, f'Level: {level}', ln=True)
            for q in qlist:
                self.pdf.multi_cell(0, 10, f"Q: {q['question']}\nA: {q['answer']}\nCode: {q.get('code', '')}")
        self.pdf.output(self.output_file)

    def export_progress(self, progress_file):
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress = json.load(f)
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(0, 10, 'User Progress', ln=True)
        self.pdf.set_font('Arial', '', 12)
        for level, questions in progress.items():
            self.pdf.cell(0, 10, f'Level: {level}', ln=True)
            for q in questions:
                self.pdf.cell(0, 10, f'Answered: {q}', ln=True)
        self.pdf.output(self.output_file)
