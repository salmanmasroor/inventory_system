class Product:
    def __init__(self,name,sku,quantity,price):
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} | Rs.{self.price} | Qty:{self.quantity}"

