security_events = [
    "Login successful",
    "Login failed",
    "Login failed",
    "Password changed",
    "Login successful",
    "Login failed"
]

success_count = 0
failed_count = 0
password_count = 0

for event in security_events:
    if "successful" in event:
        success_count += 1
   
    elif "failed" in event:    
        failed_count += 1
        
    else:
        if "Password" in event:
            password_count +=1

print(f"Succesful logins: {success_count}")
print(f"Failed logins: {failed_count}")
print(f"Password changes: {password_count}")

if failed_count >= 3:
    print("WARNING: High number of failed login attempts!")