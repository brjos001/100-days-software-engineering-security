# Python Learning Journal

## Day 3 — Conditionals, System Status & Boolean Operations

### What I Learned

Today I learned how Python uses conditionals and Boolean operations to make decisions.

I practiced:

- `if`
- `else`
- `elif`
- `and`
- `or`
- `not`
- Compound Boolean expressions
- System-status logic
- Access-control logic

---

## Conditionals

### `if` / `else`

An `if` statement checks a condition.

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Since `age` is 15, the condition is `False`, so the `else` block runs.

### `elif`

`elif` allows multiple conditions to be checked.

```python
score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

Python checks the conditions from top to bottom and executes the first condition that is `True`.

---

## System Status

I practiced using `and` to require multiple conditions to be true.

```python
server_online = True
cpu_usage = 45

if server_online and cpu_usage < 80:
    print("Server is healthy")
else:
    print("Server needs attention")
```

Both conditions must be `True`.

```text
True and True
True
```

---

## Boolean Operators

### `and`

Both conditions must be `True`.

```text
True and True
True

True and False
False

False and True
False

False and False
False
```

### `or`

At least one condition must be `True`.

```text
True or True
True

True or False
True

False or True
True

False or False
False
```

### `not`

`not` reverses a Boolean value.

```text
not True
False

not False
True
```

---

## System Status with `or`

I practiced using `or` to determine whether a server needs attention.

```python
server_online = True
disk_space = 8

if not server_online or disk_space < 10:
    print("Server needs attention")
else:
    print("Server is healthy")
```

The server needs attention when either:

- The server is offline.
- Disk space is below 10.

---

## Combining Boolean Operators

I practiced combining `and`, `or`, and `not`.

```python
username_correct = True
password_correct = True
account_locked = False
is_admin = True

if (username_correct and password_correct and not account_locked) or is_admin:
    print("Access Granted")
else:
    print("Access Denied")
```

The logic is:

```text
(username correct AND password correct AND account NOT locked)
OR
admin
```

---

## Mistake I Made

I initially misunderstood `account_locked`.

I thought:

```python
account_locked = True
```

would allow normal access.

I realized that `True` means the account is locked.

Normal access requires:

```python
not account_locked
```

For example:

```python
account_locked = False

if not account_locked:
    print("Account is unlocked")
```

---

## Boolean Evaluation

I practiced breaking complex Boolean expressions into smaller parts.

```text
(True and True and not True) or False
```

First:

```text
not True
False
```

Then:

```text
True and True and False
False
```

Finally:

```text
False or False
False
```

---

## Day 3 Takeaways

```text
if       → make a decision
elif     → check another condition
else     → handle everything else

and      → all conditions must be true
or       → at least one condition must be true
not      → reverses True and False
```

The main skill I developed today was learning to predict the result of a condition before running the code.

I am learning to think through:

```text
State
↓
Condition
↓
True / False
↓
Branch
↓
Action
```