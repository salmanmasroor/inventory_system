from models.supplier import Supplier

from .base_repository import BaseRepository


class SupplierRepository(BaseRepository):
    def add(self, name, contact=""):
        self.execute(
            "INSERT INTO suppliers (name, contact) VALUES (?, ?)",
            (name, contact or None),
        )
        return True

    def find_all(self):
        rows = self.fetchall("SELECT id, name, contact FROM suppliers ORDER BY id")
        return [Supplier(row[0], row[1], row[2] or "") for row in rows]

    def find_by_id(self, supplier_id):
        row = self.fetchone(
            "SELECT id, name, contact FROM suppliers WHERE id = ?",
            (supplier_id,),
        )
        if row is None:
            return None
        return Supplier(row[0], row[1], row[2] or "")

    def update(self, supplier_id, name=None, contact=None):
        rowcount = 0
        if name is not None:
            rowcount += self.execute(
                "UPDATE suppliers SET name = ? WHERE id = ?",
                (name, supplier_id),
            )
        if contact is not None:
            rowcount += self.execute(
                "UPDATE suppliers SET contact = ? WHERE id = ?",
                (contact, supplier_id),
            )
        return rowcount > 0

    def delete(self, supplier_id):
        return self.execute("DELETE FROM suppliers WHERE id = ?", (supplier_id,)) > 0
