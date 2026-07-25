# Task 1: Write Sales Records to a File
sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", "w") as file:
    for sale in sales:
        file.write(f"{sale}\n")

with open("sales_data.txt", "r") as file:
    print("--- Task 1: File Contents ---")
    print(file.read())

# Task 2: Read File in Different Ways

with open("sales_data.txt", "r") as file:
    print("--- Task 2.1: .read() ---")
    print(file.read())

with open("sales_data.txt", "r") as file:
    print("--- Task 2.2: .readline() ---")
    print(file.readline().strip())

with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    sales_list = [int(line.strip()) for line in lines]
    print("--- Task 2.3: List of Integers ---")
    print(sales_list)

# Task 3: Append New Sales
new_sales = [5000, 2500, 1700]

with open("sales_data.txt", "a") as file:
    for sale in new_sales:
        file.write(f"{sale}\n")

with open("sales_data.txt", "r") as file:
    content = file.readlines()
    print("--- Task 3: Updated File ---")
    for line in content:
        print(line.strip())

    print(f"\nTotal number of lines: {len(content)}")

# Task 4: Summary Report
try:
    with open("sales_data.txt", "r") as file:
        sales = [int(line.strip()) for line in file if line.strip()]

    if sales:
        total = sum(sales)
        highest = max(sales)
        lowest = min(sales)
        average = total / len(sales)

        print(f"Total Sales: {total}")
        print(f"Highest Sale: {highest}")
        print(f"Lowest Sale: {lowest}")
        print(f"Average Sale: {average}")
except FileNotFoundError:
    print("Error: sales_data.txt not found.")

# Task 5: Create Product Info File
product = {}

for i in range(3):
    name = input(f"Enter name for product {i+1}: ")
    price = input(f"Enter price for product {i+1}: ")
    product[name] = price

with open("products.txt", "a") as file:
    for name, price in product.items():
        file.write(f"{name} | {price}\n")

print("\n--- Product List ---")
with open("products.txt", "r") as file:
    for line in file:
        print(line.strip())

# Task 6: Read File Safely
import os

filename = input("Enter the filename to open: ")

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print("File not found. Please check the filename.")

# Task 7: Discount Report
prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_pct = float(input("Enter discount percentage (e.g., 10 for 10%): "))
discounted_total = 0

with open("discount_report.txt", "w") as file:
    for product, price in prices.items():
        discounted_p = price * (1 - discount_pct / 100)
        discounted_total += discounted_p
        file.write(f"{product} | {price} | {discounted_p}\n")

    avg_discounted = discounted_total / len(prices)
    file.write(f"\nTotal Items: {len(prices)}")
    file.write(f"\nAverage Discounted Price: {avg_discounted}")

print("\n--- Discount Report ---")
with open("discount_report.txt", "r") as file:
    print(file.read())