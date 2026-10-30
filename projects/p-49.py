products = [
    ("P101", 100, 10),
    ("P102", 250, 5),
    ("P103", 150, 0),
    ("P104", 200, 8),
    ("P101", 100, 10)
]

total_value = 0

print("PRODUCT CATALOGUE REPORT")

for product in products:
    product_id, price, stock = product

    print("\nProduct ID:", product_id)
    print("Price:", price)
    print("Stock:", stock)

    if price <= 0 or stock < 0:
        print("Invalid Product Record")

    else:
        value = price * stock
        total_value += value

        print("Inventory Value:", value)

        if stock < 5:
            print("Replenishment Required")

print("\nDuplicate Product IDs:")

for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i][0] == products[j][0]:
            print("Duplicate:", products[i][0])

print("\nTotal Inventory Value:", total_value)