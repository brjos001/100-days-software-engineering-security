# Challegne 1 AND operator: Login checker

user = input("What's your username: ")
password = input("What's your password: ")

if user == "admin" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Challenge 2 OR operator; Discount elgibilty

student = input("Are you a student?: ")
age = input("What's your age?: ")

if student == "yes" or age >= 65:
    print("Discount eligible")
else:
    print("Discount ineligible")

# Challenge 3 NOT operator: Account status

account_active = False

if not account_active:
    print("Your account is active")
else:
    print("Your account is  inactive")

# Challenge 4 Combing logical operator: Secure access checker

role = "admin"
account_active = input("Is your account active")

if role == "admin" or (role == "employee" and account_active):
    print("Access Granted")
else:
    print("Acces Denied")