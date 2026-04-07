import random

TASKS = [
    {
        "id": "1",
        "message": "I was charged twice for my subscription.",
        "category": "billing",
        "priority": "high",
        "solution_keywords": ["refund", "charged twice"]
    },
    {
        "id": "2",
        "message": "The app crashes when I open it.",
        "category": "technical",
        "priority": "medium",
        "solution_keywords": ["update", "reinstall"]
    },
    {
        "id": "3",
        "message": "I want to cancel my account.",
        "category": "account",
        "priority": "low",
        "solution_keywords": ["cancel", "account"]
    }
]

def get_random_task():
    return random.choice(TASKS)
