# Challenge 1 - Iterate through a list

usernames = ["admin", "john", "sarah", "mike", "david"]

for username in usernames:
    print(f"User account: {username}")

# Challenge 2 - Count uppercase letters

text = "PyThOn SeCuRiTy"
count = 0

for char in text:
    if char.isupper():
        count += 1

print(f"Total uppercase characters: {count}")

# Challenge 3 - Analyze security events

security_events = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Login successful",
    "Login failed"
]

count = 0

for key in security_events:
    if "failed" in key:
        count += 1
        print(f"Failed login: {count}")

print(f"Total failed attempts: {count}")
