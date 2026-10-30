password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    else:
        special += 1

if len(password) < 8:
    print("Password must contain 8 characters")

if upper == 0:
    print("Add one uppercase letter")

if lower == 0:
    print("Add one lowercase letter")

if digit == 0:
    print("Add one number")

if special == 0:
    print("Add one special character")

if "123" in password or "password" in password.lower():
    print("Contains a prohibited pattern")

elif len(password) >= 8 and upper > 0 and lower > 0 and digit > 0 and special > 0:
    print("Password is valid")