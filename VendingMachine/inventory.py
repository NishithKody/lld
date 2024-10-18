
from product import Product

class Inventory:
    def __init__(self) -> None:
        self.products = {}
    
    def add_product(self, product:Product, quantity):
        self.products[product] = quantity
    
    def increase_quantity(self, product:Product, value):
        self.products[product] += value
    
    def get_product_quantity(self, product:Product):
        if(product in self.products):
            return self.products[product]
        else:
            return 0
    
    def is_avail(self, product:Product):
        if(product in self.products and self.products[product]>0):
            return True
        else:
            return False