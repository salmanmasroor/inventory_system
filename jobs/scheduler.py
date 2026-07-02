import threading
import time

from config import SCHEDULER_INTERVAL_SECONDS
from jobs.send_email import alert_email
from services.product_service import ProductService


def low_stock_scheduler():
    product_service = ProductService()
    while True:
        time.sleep(SCHEDULER_INTERVAL_SECONDS)
        data = product_service.low_stock_products()
        for info in data:
            product_id, name, quantity = info[0], info[1], info[3]
            message = f"ID: {product_id}\nProduct Name: {name}\nQuantity: {quantity}\n"
            # alert_email(message)


def run_task():
    thread = threading.Thread(target=low_stock_scheduler)
    thread.daemon = True
    thread.start()
