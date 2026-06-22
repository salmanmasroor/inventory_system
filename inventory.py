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
    
    def update_product(self,product_id,type,value):

        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE products SET {type} = ? WHERE id = ?",(value,product_id))
        conn.commit()
        conn.close()

    def select_option(self,id):
        if id == 1:
            value = "name"
        if id == 2:
            value = "price"
        if id == 3:
            value = "quantity"
        return value