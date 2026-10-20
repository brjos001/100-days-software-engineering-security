
### `Journal.md`

```markdown
# Day 6 Journal — Modules

## What I Learned

Today I started learning how Python programs can be separated into multiple files.

I learned that a Python file can act as a **module**, and other Python files can import code from it.

For example:

```python
import calculator

# Day 6 Journal — Modules

## What I Learned

Today I started learning how Python programs can be separated into multiple files using **modules**.

I learned that a Python file can act as a module, allowing other Python files to import and reuse its functions, variables, and classes. This helps keep code organized, reduces repetition, and makes projects easier to maintain.

Instead of writing an entire program in one large file, I can separate related functionality into different files and import it whenever needed.

## 1. Creating a Module

I created a Python file named `calculator.py` containing two functions:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

The `add()` function takes two arguments and returns their sum.

The `subtract()` function takes two arguments and returns the result of subtracting the second number from the first.

These functions are stored in the `calculator.py` module so that other Python files can reuse them.

## 2. Importing a Module

After creating the module, I can create another Python file named `main.py` in the same directory.

```python
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.subtract(10, 5)

print(result1)
print(result2)
```

### Output

```text
15
5
```

Using `import calculator` allows me to access the functions defined inside `calculator.py`.

I use `calculator.add()` and `calculator.subtract()` to call the functions through the module name.

This makes it easier to identify where a function comes from, especially when a project contains multiple modules.

## 3. Importing Specific Functions

Python also allows me to import a specific function instead of importing the entire module.

```python
from calculator import add

result = add(7, 3)

print(result)
```

### Output

```text
10
```

The statement `from calculator import add` imports only the `add()` function into the current namespace.

Because I imported the function directly, I can call `add()` without writing `calculator.add()`.

## 4. Importing Multiple Functions

I can import more than one function from the same module.

```python
from calculator import add, subtract

print(add(20, 8))
print(subtract(20, 8))
```

### Output

```text
28
12
```

This approach is useful when I only need a few specific functions from a module.

## 5. Using an Alias

Python allows me to give a module a shorter name using the `as` keyword.

```python
import calculator as calc

print(calc.add(4, 6))
print(calc.subtract(10, 3))
```

### Output

```text
10
7
```

An alias can make code shorter and easier to read. It is particularly useful when working with modules that have long names.

## 6. Why Modules Are Important

Modules provide several benefits when developing Python applications:

* **Code reusability:** I can use the same functions in multiple files without rewriting them.
* **Organization:** I can separate related functionality into individual files.
* **Maintainability:** Updating one module can improve every part of the program that uses it.
* **Readability:** Smaller files make code easier to understand and debug.
* **Collaboration:** Different developers can work on separate modules within the same project.

## 7. Key Concepts Learned

* A module is a Python file that contains reusable code.
* The `import` statement allows me to access code from another module.
* The `from ... import ...` syntax imports specific functions or other names.
* The `as` keyword creates an alias.
* Functions inside a module can be reused across multiple Python files.
* Modules help prepare a project for a more structured package organization.

## Reflection

Today I learned how to organize Python programs by separating functions into modules and importing them into other files.

I now understand that I do not need to write all my code in a single Python file. Instead, I can create reusable modules and combine them to build larger applications.

This is an important step toward writing cleaner, more maintainable Python code and understanding how real-world Python projects are structured.

## Next Steps

* [ ] Practice creating additional Python modules.
* [ ] Import functions and variables from other files.
* [ ] Experiment with module aliases.
* [ ] Learn how Python packages organize multiple modules.
* [ ] Continue working through the Day 6 Packages and Developer Toolkit exercises.

