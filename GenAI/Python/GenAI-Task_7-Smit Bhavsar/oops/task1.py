#Task 1: Basic class

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
    def apply_discount(self,percent):
        return self.price*percent/100
    

watch = Product("Titan Watch", 2000, "Electric")
watch.get_info()

shirt = Product("US Polo Shirt", 2000, "Clothing")
shirt.get_info()