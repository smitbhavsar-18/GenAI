#Task 1: Create a product collection using list and tuple data structures.
products =["watch", "shoes", "bag", "jewelry", "sunglasses","shirt"]

sample_product = ("watch","1000","electronics")

print(products[-2])

products.append("belt")
products.append("hat")
print(products)

sample_product=list(sample_product)
sample_product[1] = "1500"
sample_product = tuple(sample_product)

print(sample_product)

#Task2 : Categories (sets)

categories_set = {"electronics", "fashion", "home decor", "beauty", "sports"}

categories_set.add("toys")
categories_set.add("sports")

print(categories_set)

print("shirt" in categories_set)

#Task 3: Product Pricing (dictionary)

price_dict = {
    "watch": 1000,  
    "shoes": 500,
    "bag": 300,
    "jewelry": 2000,
    "sunglasses": 150,
    "shirt": 100
}

price_dict["belt"] = 50
price_dict["bag"] = 350
if "jewelry" in price_dict:
    del price_dict["jewelry"]
print(price_dict)

sum = 0
maxi = float('-inf')
mini = float('inf')

for key, value in price_dict.items():
    sum = sum + value
    maxi = max(maxi, value)
    mini = min(mini, value)
    
average = sum / len(price_dict)
print("Average price of products:", average)

print("Maximum price of products:", maxi)
print("Minimum price of products:", mini)

#Task 4: Combined Operations
products = [("Laptop", "Electronics"), ("Coffee", "Grocery"), ("Phone", "Electronics"), ("Bread", "Grocery"), ("Milk", "Grocery")]
price_dict = {"Laptop": 1000, "Coffee": 10, "Phone": 500, "Bread": 2, "Milk": 3}

catalog = [(name, price_dict[name], cat) for name, cat in products]

category_to_products = {}
for name, price, cat in catalog:
    if cat not in category_to_products:
        category_to_products[cat] = []
    category_to_products[cat].append(name)

max_category = max(category_to_products, key=lambda k: len(category_to_products[k]))

print(f"Category with most products: {max_category}")
print(f"Products: {category_to_products[max_category]}")
