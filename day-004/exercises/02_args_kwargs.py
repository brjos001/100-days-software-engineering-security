'''
# Exercise 1
def show_args(*args):
    print(args)

#show_args(1, 2, 3)

show_args("Alice", 25, True, "admin")'''

'''
# Exercise 2
def show_args(*args):
    for value in args:
        print(value)

show_args("Alice", 25, True)'''

'''
# Exercise 3
def calculate_sum(*numbers):
    total = 0
    
    for value in numbers:
        total = total + value

    print(total)

calculate_sum(1, 2, 3)'''

'''
# Basic simple example
def show_info(**kwargs):
    print(kwargs)

show_info(name="Alice", age=25, role="admin")'''

'''
Exercise 1
def describe_user(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)
        print(kwargs)


describe_user(
    name="Alice",
    age=25,
    admin=True
)'''

'''def inspect_user(*args, **kwargs):
    print("ARGS:", args)
    print("KWARGS:", kwargs)

inspect_user("Alice", 25, True, role="admin", active=True)'''
'''
# Exercise 2

def create_user(*args, **kwargs):
    user = {
        "name": args[0],
        "age" : args[1],
    }

    return user


user = create_user("Joseph", 28, role="admin", user=True)

print(user)'''

'''
# Exercise 3

def greet():
    return "Hello"

def execute(function):
    return function()

result = execute(greet)

print(result)'''

def add():
    print("Adding user")

def list_users():
    print("Listing users")

commands = {
    "add": add,
    "list": list_users
}

commands["add"]()
commands["list"]()

def run_command(command):
    return commands[command]

run_command("add")

