class Product:
    def __init__(self,name,sku,quantity,price,category_id):
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.category_id = category_id

    def __str__(self):
        return f"{self.name} | Rs.{self.price} | Qty:{self.quantity}"

