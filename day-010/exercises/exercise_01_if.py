'''age = int(input("What is your age: "))

if age < 13:
    print("Child")
elif age > 13 and age < 20:
    print("Teenager")
else:
    print("Adult")'''

# Program checks exam results 

score = int(input("What's your score: "))

if score < 0 or score > 100:
    print("invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 50 :
    print("Pass")
else:
    print("Fail")