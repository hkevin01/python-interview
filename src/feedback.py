"""
Feedback and rating system for questions and answers.
"""
import json
import os


class FeedbackManager:
    def __init__(self, feedback_file=None):
        self.feedback_file = feedback_file or os.path.join(os.path.dirname(__file__), '../data/feedback.json')
        if not os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def submit_feedback(self, question, rating, comment):
        with open(self.feedback_file, 'r', encoding='utf-8') as f:
            feedback = json.load(f)
        entry = {'question': question, 'rating': rating, 'comment': comment}
        feedback.append(entry)
        with open(self.feedback_file, 'w', encoding='utf-8') as f:
            json.dump(feedback, f, indent=2)
        return True

    def get_feedback(self):
        with open(self.feedback_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def analyze_feedback(self):
        feedback = self.get_feedback()
        if not feedback:
            return {'average_rating': None, 'total': 0}
        avg = sum(f['rating'] for f in feedback) / len(feedback)
        return {'average_rating': avg, 'total': len(feedback)}
