import sqlite3
import tempfile
import unittest
from pathlib import Path

from models.product import Product
from repositories.category_repository import CategoryRepository
from repositories.product_repository import ProductRepository
from repositories.supplier_repository import SupplierRepository
from repositories.user_repository import UserRepository


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.temp_dir.name) / "test.db"
        self._create_schema()

    def tearDown(self):
        self.temp_dir.cleanup()

    def _create_schema(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT NOT NULL,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                category_id INTEGER,
                supplier_id INTEGER
            )
        """)
        cursor.execute("""
            CREATE TABLE categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                contact TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def test_product_repository_crud(self):
        repo = ProductRepository(db_path=self.db_path)
        product = Product("Widget", "SKU001", 10, 9.99, None, None)
        repo.add(product)

        rows = repo.find_all()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][1], "Widget")

        repo.update_field(1, "quantity", 5)
        updated = repo.find_by_id(1)
        self.assertEqual(updated[0][3], 5)

        low_stock = repo.find_low_stock(10)
        self.assertEqual(len(low_stock), 1)

        repo.delete(1)
        self.assertEqual(len(repo.find_all()), 0)

    def test_category_repository_add_and_delete(self):
        repo = CategoryRepository(db_path=self.db_path)
        self.assertTrue(repo.add("Electronics"))
        self.assertFalse(repo.add("Electronics"))

        categories = repo.find_all()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Electronics")

        self.assertTrue(repo.delete(categories[0].id))

    def test_supplier_repository(self):
        repo = SupplierRepository(db_path=self.db_path)
        repo.add("Acme Corp", "555-0100")

        suppliers = repo.find_all()
        self.assertEqual(len(suppliers), 1)
        self.assertEqual(suppliers[0].name, "Acme Corp")

        supplier = repo.find_by_id(suppliers[0].id)
        self.assertIsNotNone(supplier)
        self.assertEqual(supplier.contact, "555-0100")

    def test_user_repository(self):
        repo = UserRepository(db_path=self.db_path)
        repo.create("John", "Doe", "john@example.com", "hashed")

        self.assertTrue(repo.email_exists("john@example.com"))
        self.assertFalse(repo.email_exists("missing@example.com"))

        rows = repo.authenticate("john@example.com", "hashed")
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
