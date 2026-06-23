class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"{self.name} | Rs.{self.price} | Qty:{self.quantity}"


class User:
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}\nEmail: {self.email}"


if __name__ == "__main__":
    p = Product("asdas",12,23)
    print(p)