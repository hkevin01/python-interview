# Usage Guide

## Running the Application
1. Activate your Python virtual environment:
   ```bash
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the GUI:
   ```bash
   python src/main.py
   ```

## Features
- Browse Python interview questions by difficulty (Beginner, Intermediate, Advanced)
- Reveal answers and explanations
- Search and filter questions using the search bar
- Example code snippets for each question

## Adding Questions
- Edit `data/questions.json` to add new questions and answers
- Use the format:
  ```json
  {
    "question": "Your question here",
    "answer": "Your answer here"
  }
  ```

## Troubleshooting
- Ensure PyQt5 is installed in your environment
- If you encounter errors, check your Python version and dependencies
