Python Toolkit

A Python learning project focused on building practical tools, handling errors, and writing reliable code.

📌 Day 9 — Exception Handling

Today's focus is making the toolkit resilient to unexpected input and errors.

Features
Handle invalid commands.
Handle missing files.
Validate numeric input.
Catch Python exceptions.
Create custom exceptions.
Keep the application running after errors.
Concepts Learned
Concept	Description
try	Attempts potentially risky code
except	Handles exceptions
else	Runs when no exception occurs
finally	Executes during cleanup
raise	Deliberately triggers exceptions
Exception hierarchy	Organizes exception types
📁 Project Structure
text
python-toolkit/
│
├── README.md
├── Journal.md
├── roadmap.md
├── toolkit.py
├── roadmap.md
├── journal.md
└── readme.md

Note: The lowercase Markdown files above are example files used by the toolkit. On case-sensitive systems, filenames with different capitalization are separate files.
⚙️ Requirements
Python 3.10+
pip
markdown-it-py (for Markdown parsing exercises)

Install the dependency:

bash
pip install markdown-it-py

▶️ Run the Toolkit
bash
python toolkit.py

🧪 Error Testing
Test	Expected Behavior
Invalid command	Display an error
Missing file	Display a file-not-found message
Invalid number	Catch ValueError
Negative number	Raise custom ValueError
Division by zero	Catch ZeroDivisionError
🎯 Project Goal

Build a reliable Python toolkit that handles unexpected situations without crashing.

📚 Learning Progress
Day 9 — Exception Handling
Day 10 — Upcoming Python concepts

Learning Python one project at a time.
