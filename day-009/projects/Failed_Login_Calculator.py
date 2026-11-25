'''username = "admin"
total_attempts = 12
successful_attempts = 8

failed_login = total_attempts - successful_attempts

# My first attempt
# print(username, "Failed login attempts", failed_login)

# Small improvement
print(f"Username: {username}")
print(f"Failed login attempts: {failed_login}")'''

# Next cahllenge User input

username = input("Enter username: ")

total_attempts = int(input("Enter total login attempts: "))

successful_attempts = int(input("Enter successful attempts: "))


if successful_attempts > total_attempts:
    print("Error: Succesful attempts cannot exceed total attempts")
else:
    success_rate = (successful_attempts/total_attempts) * 100
    print(f"Username: {username}")
    print(f"Success Rate: {success_rate}%")
