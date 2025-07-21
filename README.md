# Python Interview Assistant

[![Build Status](https://github.com/kevin/python-interview/actions/workflows/build.yml/badge.svg)](https://github.com/kevin/python-interview/actions/workflows/build.yml)
[![Test Status](https://github.com/kevin/python-interview/actions/workflows/test.yml/badge.svg)](https://github.com/kevin/python-interview/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview
A PyQt-based GUI application featuring common Python interview questions and answers, from beginner to advanced (including PyTorch and scikit-learn). It also teaches project structure and best practices for Python, Java, and C++.

## Features
- Browse questions by difficulty (Beginner, Intermediate, Advanced)
- Reveal answers and explanations
- Search and filter questions
- Example code snippets
- Add new questions via script or editing JSON

## Installation
```bash
# Clone the repository
$ git clone https://github.com/kevin/python-interview.git
$ cd python-interview

# Create and activate a virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt
```

## Usage
```bash
$ python src/main.py
```

See [docs/USAGE.md](docs/USAGE.md) for more details.

## Contribution
See [docs/CODING_STANDARDS.md](docs/CODING_STANDARDS.md) and [docs/WORKFLOW.md](docs/WORKFLOW.md).

## License
MIT
