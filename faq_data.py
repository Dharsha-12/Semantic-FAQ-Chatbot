"""A small FAQ dataset for the terminal chatbot."""

# Each item has a stable ID, the question that will be embedded, and its answer.
# The question is stored as the searchable document; the answer is returned later.
FAQS = [
    {
        "id": "faq-001",
        "question": "What is a variable in Python?",
        "answer": "A variable is a name that refers to a value, such as `count = 3`.",
    },
    {
        "id": "faq-002",
        "question": "How do I create a list in Python?",
        "answer": "Use square brackets, for example `colors = ['red', 'blue']`.",
    },
    {
        "id": "faq-003",
        "question": "What is a Python dictionary?",
        "answer": "A dictionary stores key-value pairs, for example `{'name': 'Ada'}`.",
    },
    {
        "id": "faq-004",
        "question": "How do I define a function in Python?",
        "answer": "Use `def`, followed by the function name and parentheses, such as `def greet():`.",
    },
    {
        "id": "faq-005",
        "question": "What is a loop used for?",
        "answer": "A loop repeats a block of code, often once for each item in a collection.",
    },
    {
        "id": "faq-006",
        "question": "What is the difference between a list and a tuple?",
        "answer": "A list can be changed after it is created; a tuple is generally used for a fixed sequence.",
    },
    {
        "id": "faq-007",
        "question": "How can I install a Python package?",
        "answer": "Use pip in your terminal, for example `python -m pip install package-name`.",
    },
    {
        "id": "faq-008",
        "question": "What does an if statement do?",
        "answer": "An if statement runs code only when its condition is true.",
    },
    {
        "id": "faq-009",
        "question": "What is a Python module?",
        "answer": "A module is a Python file containing code that can be imported and reused.",
    },
    {
        "id": "faq-010",
        "question": "How do I handle errors in Python?",
        "answer": "Use `try` and `except` to catch and handle specific exceptions.",
    },
    {
        "id": "faq-011",
        "question": "What does the return statement do?",
        "answer": "The return statement sends a value from a function back to the code that called it.",
    },
    {
        "id": "faq-012",
        "question": "What is a virtual environment?",
        "answer": "A virtual environment keeps a project's installed Python packages separate from other projects.",
    },
]
