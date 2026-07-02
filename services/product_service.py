from config import LOW_STOCK_THRESHOLD
from logger import get_logger
from repositories.product_repository import ProductRepository

log = get_logger()


class ProductService:
    def __init__(self, repository=None):
        self.repository = repository or ProductRepository()

    def add_product(self, product):
        self.repository.add(product)
        log.info("Product added successfully")

    def view_products(self, product_id=None):
        if product_id is not None:
            return self.repository.find_by_id(product_id)
        return self.repository.find_all()

    def update_product(self, product_id, field_type, value):
        self.repository.update_field(product_id, field_type, value)
        log.info("Product %s updated successfully", field_type)

    def select_option(self, option_id):
        return self.repository.field_for_option(option_id)

    def delete_product(self, product_id):
        self.repository.delete(product_id)
        log.info("Product %s deleted", product_id)

    def search_product(self, product_id):
        if isinstance(product_id, int):
            return self.repository.search_by_id(product_id)
        if isinstance(product_id, str):
            return self.repository.search_by_name(product_id)
        return []

    def low_stock_products(self, threshold=LOW_STOCK_THRESHOLD):
        return self.repository.find_low_stock(threshold)
