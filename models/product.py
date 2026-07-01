class Product:
    def __init__(self, name, sku, quantity, price, category_id, supplier_id=None):
        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price
        self.category_id = category_id
        self.supplier_id = supplier_id

    def __str__(self):
        return f"{self.name} | Rs.{self.price} | Qty:{self.quantity}"

