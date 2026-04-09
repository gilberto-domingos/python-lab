from product import Product

class Stock:
     def __init__(self):
         self.products = []

     def add_product(self, product):
         self.products.append(product)

     def remove_product(self, product):
         if product not in self.products:
             raise ValueError("Product not found")
         self.products.remove(product)

     def search_product(self, name):
         for product in self.products:
             if product.name == name:
                 return product
         return None