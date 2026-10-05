# Day 4 — Functions

## Topics

- Function definitions
- Arguments
- Return values
- Local variables
- Global variables
- LEGB scope
- `*args`
- `**kwargs`
- Function objects
- Functions stored in dictionaries
- Function dispatch

## What I Learned

Today I focused on understanding functions, arguments, return values, and scope.

### `*args`

`*args` allows a function to accept an arbitrary number of positional arguments.

```python
def show_args(*args):
    print(args)

show_args("Alice", 25, True)

