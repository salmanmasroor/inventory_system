import sqlite3
from model import Product
from logger import get_logger

log = get_logger()
class Inventory:

    def connect(self):
        return sqlite3.connect("inventory.db")
    
    def _query(self,query,*args):
        conn = self.connect()
        cursor= conn.cursor()

        cursor.execute(query,*args)
        conn.commit()

        conn.close()
    
    def _fetch(self,query):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        conn.close()
        return rows
    
    def dashboard_menu(username="Admin"):
        print("=" * 45)
        print("               DASHBOARD")
        print("=" * 45)
        print()

        print(f"Logged in as : {username}")
        print()

        print(f"{'Products':<18}: 253")
        print(f"{'Categories':<18}: 12")
        print(f"{'Suppliers':<18}: 18")
        print(f"{'Customers':<18}: 156")
        print()

        print(f"{'Stock Value':<18}: $85,200")
        print(f"{'Low Stock':<18}: 9")
        #print(f"{\n"Today's Sales\":<18}: $1,240")
        print()

        print("=" * 45)

        options = [
            "Products",
            "Categories",
            "Suppliers",
            "Customers",
            "Purchases",
            "Sales",
            "Reports",
            "AI Assistant",
            "Settings",
            "Exit"
        ]

        for i, option in enumerate(options[:-1], 1):
            print(f"{i}. {option}")

        print("0. Exit")
        print("-" * 45)

        try:
            return int(input("Choose: "))
        except ValueError:
            return -1
        
    def add_product(self,product):
        self._query("INSERT INTO products (name,price, quantity) VALUES (?, ?, ?)",(product.name,product.price,product.quantity))
        log.info("Product added successfully")
    
    def view_products(self):
        return self._fetch("SELECT * FROM products")
        
    def update_product(self,product_id,type,value):
        self._query(f"UPDATE products SET {type} = ? WHERE id = ?",(value,product_id))
        log.info(f"Product {type} Updated successfully")

    def select_option(self,id):
        if id == 1:
            value = "name"
        elif id == 2:
            value = "price"
        elif id == 3:
            value = "quantity"
        return value
    
    def delete_product(self, product_id):
        self._query("DELETE FROM products WHERE id = ?", (product_id,))
        log.info("Product %s deleted", product_id)
    
    def search_product(self,product_id):
        conn = self.connect()
        cursor = conn.cursor()
        if isinstance(product_id,int):
               cursor.execute("SELECT * FROM products WHERE id = ?",(product_id,))
               rows = cursor.fetchall()
               return rows
        elif isinstance(product_id,str):
            cursor.execute("SELECT * FROM products WHERE name = ? OR name = ?" ,(product_id,product_id.title()))
            rows = cursor.fetchall()
            return rows
        
    def low_stock_products(self):
        self._fetch("SELECT * FROM products WHERE quantity < 5")


if __name__ == "__main__":
    pass
