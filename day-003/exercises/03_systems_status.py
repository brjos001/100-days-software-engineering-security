server_online = True
cpu_usage = 45


if server_online and cpu_usage < 80:
    print("Server is healthy")
else:
    print("Server needs attention")


server_online = True
disk_space = 50

if server_online or disk_space < 10:
    print("Server needs attention")
else:
    print("Server is healthy")

age = 20
has_id = True
is_employee = False

if (age >= 18 and has_id) or is_employee:
    print("Access Granted")
else:
    print("Access Denied")

username_correct = True
password_correct = True
account_locked = False
is_admin = True

if (username_correct and password_correct and not account_locked) or is_admin:
    print("Access Granted")
else:
    print("Access Denied") 