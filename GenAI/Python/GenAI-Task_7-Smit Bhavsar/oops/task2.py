#Task 2: Constructor & Encapsulation

class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.__price} | product category : {self.category}")
        
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price > 0:
            self.__price = price
    

watch = Product("Titan Watch", 2000, "Electric")
watch.get_info()
print("Price of watch :",watch.get_price())
watch.set_price(2500)
print("Price of watch :",watch.get_price())