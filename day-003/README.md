# Python Learning

A practical Python learning repository focused on understanding how Python works rather than memorizing syntax.

The goal is to learn how to read code, predict behavior, understand program state, and reason about how Python executes.

## Progress

### Day 1 — Python Foundations

Learned the basics of Python syntax, variables, data types, expressions, and operators.

### Day 2 — Objects, Names & References

Learned that Python names refer to objects.

Example:

x = 42
y = x

Both names refer to the same integer object.

For mutable objects:

x = []
y = x

x.append("hello")

Both `x` and `y` now refer to the same modified list.

Key concepts:

- Objects
- Names
- References
- Identity
- Equality
- Mutability
- Immutability
- Mutation
- Rebinding
- `id()`
- `is`
- `==`

### Day 3 — Conditionals, System Status & Boolean Operations

Learned how Python makes decisions using conditionals and Boolean logic.

Example:

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

Practiced:

- `if`
- `else`
- `elif`
- `and`
- `or`
- `not`
- Compound conditions
- System-status checks
- Access-control logic

Example:

if username_correct and password_correct and not account_locked:
    print("Access Granted")

## Learning Approach

The goal is not just to memorize syntax.

For each exercise, I practice:

1. Understanding the code.
2. Predicting what will happen.
3. Running the code.
4. Comparing the result with my prediction.
5. Explaining why the result happened.

## Repository Structure

README.md
ROADMAP.md
JOURNAL.md

day-03/
    conditionals_and_boolean_operations.py
