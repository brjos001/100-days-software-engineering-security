from users import create_user
from utils import format_user

user_name = input("What is your name: ")
user_age = input("What is your age: ")

user = create_user(user_name, user_age)

message = format_user(user)

print(message)