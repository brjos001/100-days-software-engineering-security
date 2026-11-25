
# Day 2 — Variables and Data Types

**Subject:** Python Fundamentals  
**Focus:** Variables, data types, type conversion, input and output.

---

## 1. Learning Objectives

- Understand strings, integers, floats and booleans.
- Learn variable assignment.
- Understand type conversion.
- Practice input and output.
- Perform calculations using variables.
- Build a basic security information calculator.

## 2. Concepts Learned

### Variables

Variables store information in Python.

```python
username = "admin"
login_attempts = 5
security_score = 85
```

The `=` operator assigns a value to a variable.

### Python Data Types

| Data type | Description | Example |
|---|---|---|
| `str` | Text | `"admin"` |
| `int` | Whole numbers | `25` |
| `float` | Decimal numbers | `95.5` |
| `bool` | True or False | `True` |

### Checking Data Types

Python provides the `type()` function.

```python
username = "admin"
attempts = 5
score = 95.5
firewall_enabled = True

print(type(username))
print(type(attempts))
print(type(score))
print(type(firewall_enabled))
```

### Type Conversion

Type conversion changes a value from one data type to another.

```python
age = "25"
age = int(age)

print(age)
print(type(age))
```

Important conversion functions:

- `int()` — converts to integer.
- `float()` — converts to float.
- `str()` — converts to string.
- `bool()` — converts to Boolean.

### Input and Output

- `input()` collects information from users.
- `print()` displays information.
- `input()` normally returns a string.

Example:

```python
username = input("Enter username: ")
attempts = int(input("Enter login attempts: "))

print(username)
print(attempts)
```

### Mathematical Operators

| Operator | Purpose |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Modulus (remainder) |
| `**` | Exponentiation |

### Augmented Assignment

```python
risk_score = 10
risk_score += 20

print(risk_score)
```

Other operators include `-=`, `*=`, and `/=`.

### Conditional Statement Introduction

Learned the basics of:

- `if`
- `elif`
- `else`

Python checks conditions from top to bottom and executes the first matching block.

---

## 3. Practical Exercises

Completed exercises involving:

1. Creating and assigning variables.
2. Identifying Python data types.
3. Converting strings into integers.
4. Collecting user input.
5. Calculating failed login attempts.
6. Calculating login success rates.
7. Validating login attempt values.

## 4. Main Practical Project

### Basic Security Information Calculator

**Objective:** Build a Python program that collects login information and calculates login statistics.

Features:

- Collect username.
- Collect total login attempts.
- Collect successful login attempts.
- Calculate failed login attempts.
- Calculate login success percentage.
- Validate user input.
- Display a security report.

### Final Project Code

```python
username = input("Enter username: ")

total_attempts = int(input("Enter total login attempts: "))

successful_attempts = int(input("Enter successful attempts: "))

if total_attempts <= 0:
    print("Error: Total attempts must be greater than zero.")

elif successful_attempts < 0:
    print("Error: Successful attempts cannot be negative.")

elif successful_attempts > total_attempts:
    print("Error: Successful attempts cannot exceed total attempts.")

else:
    failed_attempts = total_attempts - successful_attempts

    success_rate = (successful_attempts / total_attempts) * 100

    print("\n=== LOGIN SECURITY REPORT ===")
    print(f"Username: {username}")
    print(f"Total attempts: {total_attempts}")
    print(f"Successful attempts: {successful_attempts}")
    print(f"Failed attempts: {failed_attempts}")
    print(f"Success rate: {success_rate:.2f}%")
```

## 5. Important Lessons

- Variables allow programs to store and manipulate information.
- Data types determine the kind of values variables hold.
- Type conversion allows calculations using user input.
- Input and output make programs interactive.
- Conditional statements help programs make decisions.
- Input validation helps prevent invalid calculations.

## 6. Challenges Encountered

- Understanding the difference between integers and floats.
- Remembering to convert input strings into integers.
- Understanding variable reassignment.
- Preventing division by zero.
- Validating login attempt values.

## 7. Day 2 Assessment

**Status:** Completed

Successfully built a basic security information calculator and demonstrated an understanding of variables, data types, calculations, input/output and introductory conditional logic.

## 8. Next Learning Objectives — Day 3

**Topic: Conditional Statements**

- Understand `if`, `elif` and `else`.
- Learn comparison operators.
- Learn logical operators (`and`, `or`, `not`).
- Understand nested conditions.
- Build a basic security login checker.

---

**Learning Progress:** Python Fundamentals — Day 2 Complete.
