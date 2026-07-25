# Task 1: Discount Rules
try:
    # 1. Read integer input and 3. Handle non-numeric case
    order_amount = int(input("Enter order amount: "))

    # 2. Apply discount rules
    if order_amount >= 2000:
        discount_percent = 0.15
    elif 1500 <= order_amount < 2000:
        discount_percent = 0.10
    elif 1000 <= order_amount < 1500:
        discount_percent = 0.07
    else:
        discount_percent = 0.00

    # Calculations
    subtotal = order_amount * (1 - discount_percent)
    tax = subtotal * 0.05  # Extra: 5% tax
    final_total = subtotal + tax

    print(f"Subtotal: {subtotal:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Final Amount: {final_total:.2f}")

except ValueError:
    print("Error: Please enter a valid numeric integer.")   

    
#Task 2: Process Multiple Orders

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discounted_count = 0

print(f"{'Amount':<10} | {'Discount%':<10} | {'Final Amount':<12}")
print("-" * 38)

for amount in orders:
    # Determine discount
    if amount >= 2000:
        d_perc = 15
    elif 1500 <= amount < 2000:
        d_perc = 10
    elif 1000 <= amount < 1500:
        d_perc = 7
    else:
        d_perc = 0
    
    # Calculate final amount for this order
    final = amount * (1 - d_perc/100)
    total_revenue += final
    
    # Extra: Count discounted orders
    if d_perc > 0:
        discounted_count += 1
        
    print(f"{amount:<10} | {d_perc:>8}% | {final:>12.2f}")

print("-" * 38)
print(f"Total Revenue: {total_revenue:.2f}")
print(f"Orders with discounts: {discounted_count}")

#Task 3: User Menu

orders = []

while True:
    print("\nMenu options:")
    print("1 — Add order amount")
    print("2 — Show all orders and totals")
    print("q — Quit")
    
    choice = input("Choose an action: ")

    if choice == 'q':
        break
    
    if choice == '1':
        amount = float(input("Enter order amount: "))
        orders.append(amount)
    elif choice == '2':
        # Assuming a simple 10% discount for this example
        total = sum(orders)
        discounted_total = total * 0.90
        print(f"Orders: {orders}")
        print(f"Total after 10% discount: {discounted_total}")
    else:
        print("Invalid input. Please try again.")
        continue

# Task 5: Loop Control with Conditions

daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0

for sale in daily:
    if sale == -1:
        print("Corrupted data found. Stopping process.")
        break
    
    if sale == 0:
        continue  # Skip days with no sales
    
    total_sales += sale
    print(f"Added {sale}. Running total: {total_sales}")

print(f"Final total sales: {total_sales}")

    
    
