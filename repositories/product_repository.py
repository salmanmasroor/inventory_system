from models.product import Product

from .base_repository import BaseRepository

PRODUCT_SELECT = (
    "SELECT id, name, price, quantity, sku, category_id, supplier_id FROM products"
)


class ProductRepository(BaseRepository):
    def add(self, product):
        self.execute(
            "INSERT INTO products (name, price, quantity, sku, category_id, supplier_id) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                product.name,
                product.price,
                product.quantity,
                product.sku,
                product.category_id,
                product.supplier_id,
            ),
        )

    def find_all(self):
        return self.fetchall(PRODUCT_SELECT)

    def find_by_id(self, product_id):
        return self.fetchall(f"{PRODUCT_SELECT} WHERE id = ?", (product_id,))

    def update_field(self, product_id, field, value):
        self.execute(
            f"UPDATE products SET {field} = ? WHERE id = ?",
            (value, product_id),
        )

    def delete(self, product_id):
        self.execute("DELETE FROM products WHERE id = ?", (product_id,))

    def search_by_id(self, product_id):
        return self.fetchall(f"{PRODUCT_SELECT} WHERE id = ?", (product_id,))

    def search_by_name(self, name):
        return self.fetchall(
            f"{PRODUCT_SELECT} WHERE name = ? OR name = ?",
            (name, name.title()),
        )

    def find_low_stock(self, threshold):
        return self.fetchall(
            f"{PRODUCT_SELECT} WHERE quantity < ?",
            (threshold,),
        )

    @staticmethod
    def field_for_option(option_id):
        fields = {1: "name", 2: "price", 3: "quantity", 4: "sku"}
        return fields.get(option_id)

    @staticmethod
    def to_product(row):
        return Product(
            name=row[1],
            sku=row[4] if len(row) > 4 else None,
            quantity=row[3],
            price=row[2],
            category_id=row[5] if len(row) > 5 else None,
            supplier_id=row[6] if len(row) > 6 else None,
        )
