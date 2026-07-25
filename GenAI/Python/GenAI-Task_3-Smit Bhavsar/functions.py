# Task-1 : Price After Discount

def apply_discount(price,discount_percent=5):
    if(discount_percent > 60):
        return ("Discount percent must be between less then 60.")
    final_price = price * (1 - discount_percent/100)
    return final_price

print(apply_discount(1000, 10))  
print(apply_discount(500))

# Task 2- factorial using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
print(factorial(0))
print(factorial(-3))

# Task 3- Lamda function - GST calculation

gst = lambda price : price * 0.18 + price
print(gst(100))

gst_with_discount = lambda price, discount, gst: (price - (price * discount / 100)) * (1 + gst / 100)
print(gst_with_discount(1000, 10, 18))

#Task 4- Using map functions

prices = [100, 250, 400, 1200, 50]
print(list(map(lambda x: x * 0.18 + x, prices)))

print(list(map(lambda x: (x - (x * 10 / 100)) * (1 + 18 / 100), prices)))

#Task 5: Using filter()

prices = [100, 250, 400, 1200, 50, 2000, 850]

# 1. Prices greater than 500
expensive_prices = list(filter(lambda x: x > 500, prices))

# 2. Prices less than or equal to 500
affordable_prices = list(filter(lambda x: x <= 500, prices))

print(f"Expensive: {expensive_prices}")
print(f"Affordable: {affordable_prices}")

#Task 6: Combined Utility Function

def process_prices(prices):
    # Apply 10% discount
    discounted_prices = list(map(lambda x: x * 0.9, prices))
    
    # Filter discounted prices above 300
    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))
    
    return discounted_prices, filtered_prices

# Test the function
d_list, f_list = process_prices([100, 500, 900, 50, 750])
print(f"Discounted: {d_list}")
print(f"Filtered (>300): {f_list}")

#task 7 - Mini Problem: Menu Using Functions

def add_price(prices_list, price):
    prices_list.append(price)

def get_average_price(prices_list):
    return sum(prices_list) / len(prices_list) if prices_list else 0

def get_max_price(prices_list):
    return max(prices_list) if prices_list else 0

# Menu Loop
my_prices = []
while True:
    print("\n1 -> Add price | 2 -> Show average | 3 -> Show highest | q -> Quit")
    choice = input("Select an option: ").lower()

    if choice == '1':
        p = float(input("Enter price: "))
        add_price(my_prices, p)
    elif choice == '2':
        print(f"Average: {get_average_price(my_prices)}")
    elif choice == '3':
        print(f"Highest: {get_max_price(my_prices)}")
    elif choice == 'q':
        break
    else:
        print("Invalid choice.")
