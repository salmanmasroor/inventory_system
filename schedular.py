import time
import threading
from Inventory.inventory_service import Inventory
from send_email import alert_email
def low_stock_scheduler():
    inv = Inventory()
    while True:
        time.sleep(50)
        data = inv.low_stock_products()
        for info in data:
            a ,b, c ,d = info
           # message = f"ID: {a}\nProduct Name: {b}\n Quantity: {d}\n"
            #alert_email(message)


def run_task():
    thread = threading.Thread(target=low_stock_scheduler)
    thread.daemon = True
    thread.start()