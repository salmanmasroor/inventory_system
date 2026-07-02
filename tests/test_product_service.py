import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from models.product import Product
from repositories.product_repository import ProductRepository
from services.product_service import ProductService


class ProductServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.db_path = Path(self.temp_dir.name) / "test.db"
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
        conn.commit()
        conn.close()

        self.repository = ProductRepository(db_path=self.db_path)
        self.service = ProductService(repository=self.repository)

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch("services.product_service.log")
    def test_add_and_view_product(self, mock_log):
        product = Product("Gadget", "SKU100", 3, 19.99, None, None)
        self.service.add_product(product)

        products = self.service.view_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0][1], "Gadget")
        mock_log.info.assert_called_once()

    def test_search_product_by_id_and_name(self):
        product = Product("Gadget", "SKU100", 3, 19.99, None, None)
        self.service.add_product(product)

        by_id = self.service.search_product(1)
        self.assertEqual(len(by_id), 1)

        by_name = self.service.search_product("gadget")
        self.assertEqual(len(by_name), 1)

    def test_low_stock_products(self):
        self.service.add_product(Product("Low", "SKU1", 2, 5.0, None, None))
        self.service.add_product(Product("High", "SKU2", 20, 5.0, None, None))

        low_stock = self.service.low_stock_products(threshold=5)
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0][1], "Low")


if __name__ == "__main__":
    unittest.main()
