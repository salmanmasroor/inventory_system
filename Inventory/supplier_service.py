import sqlite3
from database import DB_PATH
from models.supplier import Supplier


class SupplierService:
    def __init__(self):
        self.db_path = DB_PATH

    def add_supplier(self, name, contact=""):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO suppliers (name, contact) VALUES (?, ?)",
                (name, contact or None),
            )
            conn.commit()
        return True

    def list_suppliers(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, contact FROM suppliers ORDER BY id")
            return [Supplier(row[0], row[1], row[2] or "") for row in cursor.fetchall()]

    def get_supplier(self, supplier_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, contact FROM suppliers WHERE id = ?",
                (supplier_id,),
            )
            row = cursor.fetchone()
            if row is None:
                return None
            return Supplier(row[0], row[1], row[2] or "")

    def update_supplier(self, supplier_id, name=None, contact=None):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if name is not None:
                cursor.execute(
                    "UPDATE suppliers SET name = ? WHERE id = ?",
                    (name, supplier_id),
                )
            if contact is not None:
                cursor.execute(
                    "UPDATE suppliers SET contact = ? WHERE id = ?",
                    (contact, supplier_id),
                )
            conn.commit()
            return cursor.rowcount > 0

    def delete_supplier(self, supplier_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM suppliers WHERE id = ?", (supplier_id,))
            conn.commit()
            return cursor.rowcount > 0
