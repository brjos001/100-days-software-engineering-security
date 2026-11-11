Python Learning Journal
Day 9 — Exception Handling

Date: 2026-11-11

📚 What I Learned

Today I learned how Python handles errors and exceptions.

Topics
try
except
else
finally
raise
Python exception hierarchy
🧠 Key Lessons
try

Used to execute code that might produce an error.

except

Catches an exception and allows the program to respond.

else

Executes when the try block succeeds.

finally

Executes whether an exception occurs or not.

raise

Allows me to deliberately trigger an exception.

Exception Hierarchy

Some common exceptions:

Exception	Meaning
ValueError	Invalid value
TypeError	Incorrect type
FileNotFoundError	Missing file
ZeroDivisionError	Division by zero
KeyError	Missing dictionary key
IndexError	Invalid list index
🛠️ What I Built

I created a crash-resistant Python toolkit.

It can:

Read Markdown files.
Handle missing files.
Reject invalid commands.
Validate numeric input.
Handle negative numbers.
Continue running after handled errors.
💥 Deliberate Break Tests
Test	Result
Enter invalid command	Error handled
Remove journal.md	Missing file handled
Enter hello as a number	ValueError handled
Enter -10	Custom error handled
Enter 10	Calculation succeeds
Malformed Markdown	Parser behavior investigated
🔍 What I Found Interesting

Not every error is a Python exception.

For example, malformed Markdown can be accepted by a Markdown parser without raising an exception.

This means I may need additional validation rules to detect formatting problems.

💡 Biggest Lesson

Errors are expected.

Good software should handle unexpected input gracefully instead of terminating unexpectedly.

🚧 What I Want to Improve
Add error logging.
Create custom exception classes.
Validate filenames.
Add division functionality.
Improve Markdown validation.
Test more unexpected input.
✅ Day 9 Checklist
Learned try.
Learned except.
Learned else.
Learned finally.
Learned raise.
Studied exception hierarchy.
Built exception handling into my toolkit.
Tested invalid input.
Add error logging.
Complete bonus challenge.

Day 9 Status: In Progress / Ready for final testing
