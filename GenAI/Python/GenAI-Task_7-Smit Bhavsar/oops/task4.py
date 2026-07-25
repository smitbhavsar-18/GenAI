#Task 4: Polymorphism

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
class laptop(Product):
    def get_info(self):
        print(f"This is Laptop Info : product name : {self.name} | product price : {self.price} | product category : {self.category}")
         
class Mobile(Product):
    def get_info(self):
        print(f"This is Mobile Info : product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
lenovo = laptop("Lenovo IdeaPad", 50000, "Windwos Laptop")
apple = Mobile("iphone 15", 70000, "IOS Mobile")
macbook = laptop('Macbook Pro', 150000, "MacOS Laptop")
samsung = Mobile("samsung s25", 80000, "Android Mobile")

products = [lenovo, apple, macbook, samsung]

for product in products:
    product.get_info()