import sqlite3
from product import Product

class Inventory:

    def connect(self):
        return sqlite3.connect("inventory.db")
    
    def add_product(self,product):
        conn = self.connect()
        cursor= conn.cursor()

        cursor.execute("""
        INSERT INTO products (name,price, quantity) VALUES (?, ?, ?)
        """,(product.name,product.price,product.quantity))

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
    