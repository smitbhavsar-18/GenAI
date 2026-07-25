#Task 2: INheritance

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
    
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years
        
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category} | warranty years : {self.warranty_years}")
        
watch = ElectronicProduct("Titan Watch", 2000, "watch", 2)
watch.get_info()
