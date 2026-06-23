import sqlite3
from model import Product
from logger import get_logger

log = get_logger()
class Inventory:

    def connect(self):
        return sqlite3.connect("inventory.db")
    
    def add_product(self,product):
        conn = self.connect()
        cursor= conn.cursor()

        cursor.execute("""
        INSERT INTO products (name,price, quantity) VALUES (?, ?, ?)
        """,(product.name,product.price,product.quantity))

        log.info("Product added successfully")

        conn.commit()
        conn.close()
    
    def view_products(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()

        conn.close()
        return rows
    
    def delete_product(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()
    
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
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE quantity < 5")
        rows = cursor.fetchall()
        return rows 

if __name__ == "__main__":
    inv = Inventory()
    data = (inv.search_product("Shoes"))

    for a in data:
        id , name, price, quantity = a
        print(id , name ,price, quantity)
