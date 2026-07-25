#Task 1: Safe Divison Utility

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

try:
    result = int(numerator) / int(denominator)
except ValueError:
    print("Error: Please enter valid integers for numerator and denominator.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"The result of {numerator} divided by {denominator} is: {result}")
finally:
    print("Operation completed.")    

#Task 2 : Bill Calculator

prices = [120, 350,  'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        # tring to convert in int if not integer then raise typeerror
        price = int(price)
        if price > 0:
            total += int(price)
        elif price < 0:
            # to handle negative value error
            raise ValueError("Negative price not allowed.")
    except TypeError:
        print("Price value is not number")
    except ValueError as e:
        print(f"Error: {e}")
    print(f"Current total: {total}")
    
    
#Task 3: Age validator

def check_age(age):
    # raise value error if age is less then 1 and greater then 120 otherwise return just age value
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120.")
    else:
        return (f"Valid age: {age}")

age = int(input("Enter your age: "))   
 
# if not any value error   then return age value otherwise print raised value error from method
try:
    print(check_age(age))
except ValueError as e:
    print(f"Error: {e}")
    
    
#Task 4: File Reader

filename = input("Enter the filename to read: ")

#try if file exists the read first 3 line of fileand print it otherwise print file not found from except part
try:
    with open(filename, 'r') as file:
        for i in range(4):
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("File operation attempted.")
    
#Task 5: Safe Shopping Cart

# take input from user while char is not q if price is valid float then add it to cart otherwise raise value error for negative price
cart = []
while True:
    char = input("Enter item price (or 'q' to quit): ")
    if char == 'q':
        break
    try:
        price = float(char)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        cart.append(price)
    except ValueError as e:
        print(f"Error: {e}")

print(f"Total items: {len(cart)} & Total bill: {sum(cart)}")