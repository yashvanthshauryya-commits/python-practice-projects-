email = input("Enter student email: ")
student_id = input("Enter student ID: ")

# Email validation
if ("@" in email and
    email.count("@") == 1 and
    "." in email and
    email.index(".") > email.index("@") + 1 and
    email[-1] != "." and
    " " not in email):

    print("Valid Email")
else:
    print("Invalid Email")

# Student ID format: CSE-26-101
parts = student_id.split("-")

if len(parts) == 3:
    if (len(parts[0]) >= 2 and
        len(parts[1]) == 2 and
        len(parts[2]) == 3 and
        parts[0].isalpha() and
        parts[1].isdigit() and
        parts[2].isdigit()):

        print("Valid Student ID")
    else:
        print("Invalid Student ID")
else:
    print("Invalid Student ID")