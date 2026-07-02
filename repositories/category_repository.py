import sqlite3

from models.category import Category

from .base_repository import BaseRepository


class CategoryRepository(BaseRepository):
    def add(self, name):
        try:
            self.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            return True
        except sqlite3.IntegrityError:
            return False

    def find_all(self):
        rows = self.fetchall("SELECT id, name FROM categories ORDER BY id")
        return [Category(row[0], row[1]) for row in rows]

    def update(self, category_id, new_name):
        self.execute(
            "UPDATE categories SET name = ? WHERE id = ?",
            (new_name, category_id),
        )

    def delete(self, category_id):
        return self.execute("DELETE FROM categories WHERE id = ?", (category_id,)) > 0
