class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name} | Rs.{self.price} | Qty:{self.quantity}"

if __name__ == "__main__":
    p = Product("asdas",12,23)
    print(p)