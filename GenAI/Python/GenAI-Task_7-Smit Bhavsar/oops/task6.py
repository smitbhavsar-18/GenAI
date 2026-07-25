#Task 6 : Magic Method & Operator Overloading

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
    def __str__(self):
        return f"Product details : product name : {self.name} | product price : {self.price} | product category : {self.category}"
    
    def __add__(self, product):
        return Product(self.name + " & " + product.name , self.price + product.price, self.category + " & " +  product.category)
    

watch = Product("Titan Watch", 2000, "Electric")
print(watch)

shirt = Product("US Polo Shirt", 2000, "Clothing")
print(shirt)

combined_product = watch + shirt
print(combined_product)