class Product:
    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.descricao = description
        self.quantity = quantity

    def add_stock(self, quantity):
        self.quantity += quantity

    def remove_stock(self, quantity):
        if quantity > self.quantity:
            raise ValueError("Quantity unavailable")
        self.quantity -= quantity

    def apply_discount(self, discount):
        if discount < 0 or discount > 1:
            raise ValueError("Invalid discount")
        self.price = self.price * (1 - discount)

    def get_price_final(self):
        return self.price