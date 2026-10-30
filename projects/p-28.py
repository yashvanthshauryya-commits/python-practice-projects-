ids = [101, 102, 103, 101, 104, 102]
amounts = [500, 1200, 800, 500, 2000, 1200]

print("Transaction Report")

for i in range(len(ids)):
    print(ids[i], amounts[i])

print("\nDuplicate Transactions:")

for i in range(len(ids)):
    for j in range(i + 1, len(ids)):
        if ids[i] == ids[j]:
            print("Duplicate ID:", ids[i])

print("\nHigh Value Transactions:")

for i in range(len(amounts)):
    if amounts[i] > 1000:
        print(ids[i], amounts[i])