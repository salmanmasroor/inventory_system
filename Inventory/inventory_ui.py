try:
    from utils import _get_int
    from models.product import Product
    from inventory_service import Inventory
    import math

except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from utils import _get_int, _get_float
    from models.product import Product
    from inventory_service import Inventory
    import math

class InventoryUI:

    def __init__(self):
        self.inventory = Inventory()


    def dashboard_menu(self,username="Admin"):
        """
        print("=" * 45)
        print("               DASHBOARD")
        print("=" * 45)
        print()

        print(f"Logged in as : {username}")
        print()

        print(f"{'Products':<18}: 253")
        print(f"{'Categories':<18}: 12")
        print(f"{'Suppliers':<18}: 18")
        print(f"{'Customers':<18}: 156")
        print()

        print(f"{'Stock Value':<18}: $85,200")
        print(f"{'Low Stock':<18}: 9")
        #print(f"{\n"Today's Sales\":<18}: $1,240")
        print()
        """
        print("=" * 45)
   
        options = [
            "Products",
        ]

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        print("0. Exit")
        print("-" * 45)

        return input("Choose: ")
    
    def run(self):
        result = self.dashboard_menu()

        if result == "1":
            self.product_menu()

        elif result == "2":
            print("Categories")

        elif result == "0":
            print("Exit")
    
    def product_menu(self):
        while True:
            print("=" * 50)
            print("Products".center(45))
            print("=" * 50)
            print()
            options = [
                "Add Products",
                "View Product",
                "Search Product",
                "Update Product",
                "Delete Product",
                "Exit"
            ]

            for i, value in enumerate(options,1):
                print(f"{i}.", value)
            
            choice = input("Choice: ")

            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.view_product()

    def add_product(self):
        print()
        print("-"*30)
        product_name = input("Product Name : ")
        sku = input("Sku : ")
        quantity = _get_int("Quantity : ")
        price = _get_float("Price : ")

        while True:

            if not product_name.isalpha():
                print("Only alphabet allowed and Can't be Empty")
                product_name = input("Product Name : ")
                continue

            if not sku.isalnum():
                print("Only alphabet and Number allowed and Can't be Empty")
                sku = input("Sku : ")
                continue

            break

        product = Product(product_name,sku,quantity,price)
        self.inventory.add_product(product)

        print("\nProduct added successfully!")

    def view_product(self,page_size=4):
        products = self.inventory.view_products()  # (id, name, price, quantity, sku)

        if not products:
            print("No products found.")
            return

        page = 1
        total_pages = math.ceil(len(products) / page_size)
    
        while True:
            start = (page - 1) * page_size
            chunk = products[start:start + page_size]

            print("=" * 55)
            print(f"{'ID':<4} {'Name':<13} {'SKU':<8} {'Price':>8} {'Stock':>8}")
            print("=" * 55)

            for pid, name, price, quantity, sku in chunk:
                sku = sku or "-"
                print(f"{pid:<4} {name:<13} {sku:<8} {price:>8} {quantity:>8}")

            print("=" * 55)
            print("N = Next Page")
            print("P = Previous Page")
            print("0 = Back")
            print("-" * 55)
            print(f"Page {page} of {total_pages}")

            choice = input("Choice: ").strip().upper()

            if choice == "N":
                if page < total_pages:
                    page += 1
                else:
                    print("Already on last page.")
            elif choice == "P":
                if page > 1:
                    page -= 1
                else:
                    print("Already on first page.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

            
if __name__ == "__main__":
    ui = InventoryUI()
    ui.run()