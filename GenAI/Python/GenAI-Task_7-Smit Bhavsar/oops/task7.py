# task 7: Mini Project: Simple Inventory System
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"product name : {self.name} | product price : {self.price} | product category : {self.category}")
        
    def __add__(self, product):
        return Product(self.name + " & " + product.name , self.price + product.price, self.category + " & " +  product.category)
    
class Inventory:
    
    def __init__(self, products):
        self.products = products
    def add_product(self, product):
        self.products.append(product)
    
    def remove(self, name):
        self.products.remove(name)
        
    def get_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.price     
        return total_value
    
    def show_all_products(self):
        for product in self.products:
            product.get_info()
            
class Store:
    def __init__(self, store_name, inventory):
        self.store_name = store_name
        self.inventory = inventory
    
    def add_new_product(self,name,price,category):
        return Product(name, price, category)     
    
    def show_summary(self):
        total_value = self.inventory.get_total_value()
        total_item = len(self.inventory.products) 
        print(f"Total Iteams : {total_item} | Total_value : {total_value}")  
        
laptop_inventory = Inventory([])
store = Store("Laptop Store",laptop_inventory)

lenovo = store.add_new_product("Lenovo IdeaPad", 50000, "Windwos Laptop")   
macbook = store.add_new_product("Macbook Pro", 150000, "Macos Laptop")   
dell = store.add_new_product("dell 15", 40000, "Windwos Laptop")

laptop_inventory.add_product(lenovo)
laptop_inventory.add_product(macbook)
laptop_inventory.add_product(dell)

laptop_inventory.show_all_products()

store.show_summary()

combined_product = lenovo + macbook
print("Combined price of Product : " , combined_product.price)

laptop_inventory.remove(dell)
laptop_inventory.show_all_products()

store.show_summary()

