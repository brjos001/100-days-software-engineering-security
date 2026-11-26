# Challenge 1 - Number comparison
number1 = 25
number2 = 40

if number1 == number2:
    print("Equal")
elif number1 > number2:
    print("number1 is greater")
elif number1 < number2:
    print("number1 is smaller")
elif number1 != number2:
    print("numbers are different")

# Challenge 2 - Age eligibility checker
age = int(input("What's your age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Challenge 3 - Shopping discount checker

total = int(input("What's your shopping total: "))

if total <= 50:
    print("No discount")
elif total <= 99:
    print("10 percent discount")
elif total <= 199:
    print("15 percent discount")
elif total >= 200:
    print("20 percent discount")
else:
    print("Error")
