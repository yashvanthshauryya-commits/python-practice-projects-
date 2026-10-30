days = int(input("Enter number of days: "))
start = int(input("Starting weekday (0=Mon, 6=Sun): "))

if days < 28 or days > 31 or start < 0 or start > 6:
    print("Invalid input")

else:
    print("MON TUE WED THU FRI SAT SUN")

    for i in range(start):
        print("    ", end="")

    for day in range(1, days + 1):
        print("%3d " % day, end="")

        if (start + day) % 7 == 0:
            print()

    print()