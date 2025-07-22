import json


def make_questions(level, start_id, prefix):
    return [
        {
            "id": start_id + i,
            "question": f"{prefix} Question {i+1}: What is Python concept {i+1}?",
            "answer": f"{prefix} Answer {i+1}: This is the answer for Python concept {i+1}.",
            "category": prefix.lower(),
            "explanation": f"{prefix} Explanation {i+1}: Explanation for Python concept {i+1}."
        }
        for i in range(100)
    ]

data = {
    "beginner": make_questions("beginner", 1, "Beginner"),
    "intermediate": make_questions("intermediate", 101, "Intermediate"),
    "advanced": make_questions("advanced", 201, "Advanced")
}

with open("data/questions.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Generated 100 questions for each level in data/questions.json")
