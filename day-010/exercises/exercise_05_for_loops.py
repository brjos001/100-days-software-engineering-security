# Challenge 1 - Print numbers

for i in range(11):
    print(i)

# Challenge 

for i in range(21):
    if  i % 2 == 0:
        print(i, "is even")

# Challenge 3 Security application

failed_attempts = [1, 2, 3, 4, 5]

for failed_attempt in failed_attempts:
    if failed_attempt >= 3:
        print("Warning: Multiple login attemtps detected")
    else:
        print("Login attempt recorded")

# Challenge 4 Multiplication table

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")