import sqlite3
from database import DB_PATH

class CategoryService:
    def __init__(self):
        self.db_path = DB_PATH
    

    def add_category(self, name):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
                conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def view_categories(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM categories ORDER BY id")
            return cursor.fetchall()

    def update_category(self, category_id, new_name):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE categories SET name = ? WHERE id = ?", (new_name, category_id))
            conn.commit()

    def delete_category(self, category_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
            conn.commit()
            return cursor.rowcount > 0