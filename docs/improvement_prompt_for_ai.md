# Comprehensive Prompt to Improve Python Interview Assistant

Use this prompt with an AI assistant or developer to significantly enhance your Python interview application:

---

## 1. Enhanced Questions Database
- 150+ questions: beginner (50), intermediate (60), advanced (40)
- Real interview questions from Google, Microsoft, Amazon, etc.
- Code-heavy/practical coding challenges
- Modern Python topics: asyncio, type hints, dataclasses, f-strings, walrus operator
- Framework-specific: Django, Flask, FastAPI, pandas, numpy, PyTorch, scikit-learn
- System design for senior roles
- Each question includes:
  - Clear question text
  - Detailed answer with explanation
  - Code examples (with syntax highlighting)
  - Alternative solutions
  - Time/space complexity analysis
  - Common mistakes to avoid
  - Follow-up questions

## 2. Code Syntax Highlighting
- Use Pygments for Python syntax highlighting
- Custom widget for colored code blocks
- Support dark/light themes
- Line numbers for long code
- Copy-to-clipboard for code blocks

## 3. Enhanced GUI Features
- Modern UI: better typography, spacing
- Code viewer widget with highlighting
- Progress tracking by topic
- Bookmark system with categories
- Search with filters (difficulty, topic, keywords)
- Quiz mode with timer/scoring
- Study path recommendations
- Dark/Light theme toggle
- Export to PDF/HTML

## 4. Sample Question Format
```json
{
  "id": 1,
  "question": "Question text here",
  "answer": "Detailed answer with explanation",
  "code_example": "# Python code here\nprint('Hello World')",
  "alternative_solutions": ["solution1", "solution2"],
  "complexity": {"time": "O(n)", "space": "O(1)"},
  "category": "data_structures",
  "subcategory": "lists",
  "difficulty": "beginner",
  "companies": ["Google", "Amazon"],
  "follow_up": "What if we needed to...",
  "common_mistakes": ["mistake1", "mistake2"],
  "related_topics": ["topic1", "topic2"]
}
```

## 5. Advanced Features to Add
- Adaptive learning
- Spaced repetition
- Mock interview mode
- Performance analytics
- Collaborative features
- Voice integration
- Code execution
- Video explanations

## 6. Specific Topics to Cover
- Core Python: variables, data types, control structures, functions, classes, modules, exceptions, file I/O, decorators, generators, context managers, metaclasses
- Data Structures & Algorithms: lists, dicts, sets, tuples, stacks, queues, trees, graphs, sorting, searching, DP, recursion
- OOP: classes, inheritance, polymorphism, encapsulation, abstract classes, multiple inheritance, MRO
- Advanced Python: asyncio, threading, multiprocessing, memory management, GC, GIL, descriptors, slots, weakref
- Popular Libraries: pandas, numpy, matplotlib, seaborn, jupyter, scikit-learn, PyTorch, TensorFlow, keras, Django, Flask, FastAPI, requests, pytest, unittest, mock, SQLAlchemy, celery, redis
- System Design: DB design, API design, caching, scalability, microservices, deployment

## 7. Code Highlighting Implementation
```python
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PyQt5.QtCore import QRegExp, Qt
import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import get_formatter_by_name

class CodeHighlighter(QSyntaxHighlighter):
    # Implementation for syntax highlighting
    pass

class CodeViewer(QTextEdit):
    # Custom widget for displaying code with highlighting
    pass
```

## 8. Sample Enhanced Questions
**Beginner Example**:
```json
{
  "question": "What is the difference between `==` and `is` operators in Python?",
  "answer": "The `==` operator compares values for equality, while `is` compares object identity (memory location).",
  "code_example": "a = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n\nprint(a == b)  # True - same values\nprint(a is b)  # False - different objects\nprint(a is c)  # True - same object",
  "explanation": "This distinction is crucial for understanding Python's object model..."
}
```
**Advanced Example**:
```json
{
  "question": "Implement a decorator that limits function execution time",
  "answer": "Use threading and signals to create a timeout decorator",
  "code_example": "import functools\nimport signal\n\ndef timeout(seconds):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            # Implementation here\n            pass\n        return wrapper\n    return decorator"
}
```

## 9. Additional Features
- Export study notes in markdown
- Integration with coding platforms
- Custom question creation
- Study group features
- Achievement system
- Offline mode
- Multiple languages support

## Implementation Priority
1. Enhanced questions database
2. Code syntax highlighting
3. Better UI/UX
4. Advanced features

Please provide:
- Complete implementation code for syntax highlighting
- 20 high-quality questions for each difficulty level
- Updated GUI components
- Database schema improvements
- Performance optimizations for large question sets

Focus on making this a professional-grade interview preparation tool that stands out from existing solutions.
