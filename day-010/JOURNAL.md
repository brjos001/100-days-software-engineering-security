Day 3 — Conditions and Loops

Status: Completed
Focus: Python Control Flow, Loops and Collections

1. Learning Objectives
Understand if, elif, and else.
Understand comparison operators.
Understand logical operators.
Learn nested conditions.
Understand for and while loops.
Learn how to iterate through collections.
Apply conditions and loops to practical security scenarios.
2. Key Concepts Learned
2.1 Conditional Statements

Conditional statements allow Python to make decisions based on whether a condition is True or False.

python
age = 20

if age >= 18:
    print("You are an adult")
elif age < 18:
    print("You are a minor")
else:
    print("Invalid age")


Key concepts:

if checks the first condition.
elif checks another condition.
else executes when previous conditions are false.
2.2 Comparison Operators

Comparison operators compare two values.

Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to

Example:

python
balance = 500

if balance >= 200:
    print("Sufficient funds")

2.3 Logical Operators

Logical operators combine or reverse conditions.

Operator	Meaning
and	Both conditions must be true
or	At least one condition must be true
not	Reverses the condition

Example:

python
username_correct = True
password_correct = True

if username_correct and password_correct:
    print("Login successful")
else:
    print("Login failed")

2.4 Nested Conditions

A nested condition is an if statement inside another if statement.

python
account_active = True
balance = 500
withdrawal_amount = 200

if account_active:
    print("Account verified")

    if balance >= withdrawal_amount:
        print("Sufficient funds")

        if withdrawal_amount > 0:
            print("Withdrawal approved")
        else:
            print("Invalid withdrawal amount")
    else:
        print("Insufficient funds")
else:
    print("Account is inactive")


What I learned:

Inner conditions are checked only when Python reaches them.
Indentation determines which conditions belong inside others.
Nested conditions help break complex decisions into smaller steps.
2.5 For Loops

A for loop repeats instructions for each item in a sequence.

python
for i in range(1, 11):
    print(i)


Using a list:

python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


What I learned:

range() generates a sequence of numbers.
The ending number in range() is excluded.
A for loop automatically moves to the next item.
Loops can be combined with conditions.
2.6 While Loops

A while loop repeats instructions as long as a condition remains true.

python
count = 1

while count <= 10:
    print(count)
    count += 1


What I learned:

Initialize the counter before the loop.
The while condition controls repetition.
count += 1 increments the counter.
Forgetting to update the counter can create an infinite loop.
2.7 Break Statement

The break statement immediately exits a loop.

python
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == "python123":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect password")


Important distinction:

if and else control decisions.
break terminates the loop.
Python continues executing statements after the loop.
2.8 Iterating Through Collections

Iteration means going through collection items one at a time.

Lists:

python
users = ["admin", "john", "sarah"]

for user in users:
    print(user)


Strings:

python
text = "Python"

for character in text:
    print(character)


Tuples:

python
security_events = ("Login", "Logout", "Failed Login")

for event in security_events:
    print(event)


Dictionaries:

python
user = {
    "username": "admin",
    "role": "administrator",
    "active": True
}

for key, value in user.items():
    print(key, value)


Useful string methods:

Method	Purpose
.isupper()	Checks uppercase characters
.islower()	Checks lowercase characters
.isdigit()	Checks digits
.isalpha()	Checks alphabetic characters
.isalnum()	Checks letters and numbers

The in operator checks whether an item exists inside a collection or string.

python
if "failed" in "Login failed":
    print("Failed login detected")

3. Exercises Completed
Exercise 01: If statements
Exercise 02: Comparison operators
Exercise 03: Logical operators
Exercise 04: Nested conditions
Exercise 05: For loops
Exercise 06: While loops
Exercise 07: Iterating collections
4. Practical Projects
Project 1: Security Login Checker

File: projects/security_login_checker.py

Requirements:

Accept password input.
Allow a maximum of three attempts.
Check whether the password is correct.
Display an error for incorrect passwords.
Stop asking when the correct password is entered.
Display an account lockout message after three failed attempts.

Concepts applied:

Variables
While loops
If and else
Comparison operators
Break statements
Counters

Security note: This was a learning simulation using a dummy password, not production authentication. Real passwords should never be stored or logged in plaintext.

Project 2: Security Event Analyzer

File: projects/security_event_analyzer.py

python
security_events = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Password changed",
    "Login successful",
    "Login failed"
]

success_count = 0
failed_count = 0
password_count = 0

for event in security_events:
    if "successful" in event:
        success_count += 1

    elif "failed" in event:
        failed_count += 1

    elif "Password" in event:
        password_count += 1

print(f"Successful logins: {success_count}")
print(f"Failed logins: {failed_count}")
print(f"Password changes: {password_count}")

if failed_count >= 3:
    print("WARNING: High number of failed login attempts!")


Expected output:

text
Successful logins: 2
Failed logins: 3
Password changes: 1
WARNING: High number of failed login attempts!


Concepts applied:

Lists
For loops
If and elif
String matching
Counters
Comparison operators
5. What I Learned

Today I learned how to make Python programs make decisions and repeat instructions.

My biggest takeaways:

Nested conditions allow me to check multiple requirements.
Comparison operators help me evaluate values.
Logical operators allow me to combine conditions.
For loops iterate through sequences automatically.
While loops repeat as long as a condition is true.
Break stops a loop immediately.
Collections allow me to work with multiple pieces of data.
Indentation controls the structure and execution of Python code.

I also learned how to combine these concepts to build simple security-related programs.

6. What I Found Difficult
Understanding nested conditions and indentation.
Understanding the difference between for and while loops.
Understanding why break is needed.
Understanding why code outside a loop executes after the loop finishes.
Understanding how counters work.
Choosing the correct string method or operator when analysing collections.
7. What I Need to Practice
Writing nested conditions without assistance.
Using break correctly.
Building loops with counters.
Iterating through lists and dictionaries.
Combining loops with logical operators.
Writing cleaner and more reusable Python code.
8. GitHub Commit
bash
git add .
git commit -m "Complete Day 3 Python conditions and loops"
git push

9. Day 3 Completion Status
Conditional statements
Comparison operators
Logical operators
Nested conditions
For loops
While loops
Iterating through collections
Security Login Checker
Security Event Analyzer

Day 3: COMPLETED

10. Next Learning Day

Day 4 — Functions in Python

Planned topics:

Understanding functions.
Defining functions using def.
Parameters and arguments.
Returning values with return.
Local and global scope.
Reusable functions.
Building practical security functions.

Goal: Learn to organize Python code into reusable functions and build more structured programs.