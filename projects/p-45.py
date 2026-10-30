appliances = ["Fan", "Light", "TV", "AC"]

usage = []

for i in range(4):
    row = []
    print("\nEnter", appliances[i], "usage for 7 days")

    for j in range(7):
        units = float(input("Enter units: "))
        row.append(units)

    usage.append(row)

print("\nWeekly Electricity Report")

for i in range(4):
    total = 0

    for j in range(7):
        total += usage[i][j]

    print(appliances[i], "Total:", total)

print("\nDaily Consumption:")

for j in range(7):
    total = 0

    for i in range(4):
        total += usage[i][j]

    print("Day", j + 1, ":", total, "units")

    if total > 20:
        print("Warning: High consumption!")