import sqlite3
from models.product import Product
from logger import get_logger
from database import DB_PATH


log = get_logger()


class Inventory:

    def connect(self):
        return sqlite3.connect(DB_PATH)
    
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

    def add_product(self,product):
        self._query("INSERT INTO products (name,price, quantity,sku,category_id) VALUES (?, ?, ?, ?, ?)",(product.name,product.price,product.quantity,product.sku,product.category_id))
        log.info("Product added successfully")
    
    def view_products(self,id=None):
        if id is not None:
            return self._fetch(f"SELECT * FROM products WHERE id = {id}")
        else:
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
        elif id == 4:
            value = "sku"
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
    inventory = Inventory()
    inventory.product()