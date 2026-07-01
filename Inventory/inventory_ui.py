try:
    from utils import _get_int, _get_float
    from models.product import Product
    from .inventory_service import Inventory
    from .category_ui import CategoryUI
    from .category_service import CategoryService
    import math

except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from utils import _get_int, _get_float
    from models.product import Product
    from Inventory.inventory_service import Inventory
    from Inventory.category_ui import CategoryUI
    from Inventory.category_service import CategoryService
    import math

class InventoryUI:

    def __init__(self, app=None):
        self.inventory = Inventory()
        self.category_service = CategoryService()
        self.app = app

    def _category_map(self):
        return {cat_id: name for cat_id, name in self.category_service.view_categories()}

    def _parse_product_row(self, row):
        pid, name, price, quantity = row[0], row[1], row[2], row[3]
        sku = row[4] if len(row) > 4 else None
        category_id = row[5] if len(row) > 5 else None
        return pid, sku, name, price, quantity, category_id

    def _category_label(self, category_id, category_map):
        if category_id is None:
            return "-"
        return category_map.get(category_id, "-")

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
        W = 50

        options = [
            "Products",
            "Categories",
        ]

        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("=" * W)
        print("MAIN MENU".center(W))
        print("-" * W)

        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")

        print("-" * W)
        print("  0. Exit")
        print("=" * W)
        
        return input("  Choose: ")
    
    def run(self):
        result = self.dashboard_menu()
        if result == "1":
            if self.app is not None:
                self.app.clear_screen()
            self.product_menu()
        elif result == "2":
            if self.app is not None:
                self.app.clear_screen()
            CategoryUI(self.app).display_menu()

        elif result == "0":
            if self.app is not None:
                self.app.clear_screen()
                self.app.current_user = None
    


    def product_menu(self):
        options = [
            "Add Product",
            "View Products",
            "Search Product",
            "Update Product",
            "Delete Product",
        ]

        while True:
            self.app.clear_screen()
            W = 50
            print("=" * W)
            print("SMART INVENTORY MANAGEMENT".center(W))
            print("=" * W)
            print("PRODUCTS".center(W))
            print("-" * W)

            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")

            print("-" * W)
            print("  0. Back")
            print("=" * W)

            choice = input("  Choose: ").strip()

            if choice == "1":
                self.app.clear_screen()
                self.add_product()
            elif choice == "2":
                self.app.clear_screen()
                self.view_product()
            elif choice == "3":
                self.app.clear_screen()
                self.search_product()
            elif choice == "4":
                self.app.clear_screen()
                self.update_product()
            elif choice == "5":
                self.app.clear_screen()
                self.delete_product()
            elif choice == "0":
                break
            else:
                print("\n  Invalid choice. Try again.\n")

    def add_product(self):
        W = 50
        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("=" * W)
        print("ADD PRODUCT".center(W))
        print("-" * W)
        category_list = self.category_service.view_categories()
        product_name = input("Product Name : ")
        sku = input("Sku : ")

        category_id = None
        if category_list:
            print("Categories : \n")
            for i, category in enumerate(category_list, 1):
                print(f"  {i}. {category[1]}")
            category_choice = _get_int("Choose a category by number: ", min_value=1)
            if category_choice > len(category_list):
                print("Invalid category choice.")
                input("\nPress any key to continue...")
                return
            category_id = category_list[category_choice - 1][0]
        else:
            print("No categories available. Add categories first.\n")

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

        product = Product(product_name, sku, quantity, price, category_id)
        self.inventory.add_product(product)

        print("\nProduct added successfully!")

        input("\nPress any key to continue...")

    def view_product(self,page_size=4):
        products = self.inventory.view_products()

        if not products:
            print("No products found.")
            return

        category_map = self._category_map()
        page = 1
        total_pages = math.ceil(len(products) / page_size)
    
        while True:
            self.app.clear_screen()
            W = 50
            print("=" * W)
            print("SMART INVENTORY MANAGEMENT".center(W))
            print("=" * W)
            print("VIEW PRODUCTS".center(W))
            print("-" * W)

            start = (page - 1) * page_size
            chunk = products[start:start + page_size]

            print("=" * 70)
            print(f"{'ID':<4} {'Name':<13} {'SKU':<8} {'Price':>8} {'Stock':>8} {'Category':>12}")
            print("=" * 70)

            for row in chunk:
                pid, sku, name, price, quantity, category_id = self._parse_product_row(row)
                sku = sku or "-"
                category = self._category_label(category_id, category_map)
                print(f"{pid:<4} {name:<13} {sku:<8} {price:>8} {quantity:>8} {category:>12}")

            print("=" * 70)
            print("N = Next Page")
            print("P = Previous Page")
            print("0 = Back")
            print("-" * 55)
            print(f"Page {page} of {total_pages}")

            while True:
                choice = input("Choice: ").strip().upper()

                if choice == "N":
                    if page < total_pages:
                        page += 1
                        break
                    else:
                        input("Already on last page ... Press Enter to continue.")
                        break
                elif choice == "P":
                    if page > 1:
                        page -= 1
                        break
                    else:
                        input("Already on first page... Press Enter to continue.")
                        break
                elif choice == "0":
                    return
                else:
                    print("Invalid choice.")
            
    
    def search_product(self,page_size=2):
        W = 50
        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("=" * W)
        print("SEARCH PRODUCT".center(W))
        print("-" * W)
        
        product_id = input("Enter the name or id for search: ")
        try:
            change = int(product_id)
        except ValueError:
            change = product_id

        print(change)
        products = self.inventory.search_product(change)
        category_map = self._category_map()
        
        page = 1
        total_pages = max(1, math.ceil(len(products) / page_size)) if products else 1
    
        while True:
            start = (page - 1) * page_size
            chunk = products[start:start + page_size]

            print("=" * 70)
            print(f"{'ID':<4} {'Name':<13} {'SKU':<8} {'Price':>8} {'Stock':>8} {'Category':>12}")
            print("=" * 70)

            if len(chunk) == 0:
                print()
                print("No Products Found".center(50))
                print()
            else:
                for row in chunk:
                    pid, sku, name, price, quantity, category_id = self._parse_product_row(row)
                    sku = sku or "-"
                    category = self._category_label(category_id, category_map)
                    print(f"{pid:<4} {name:<13} {sku:<8} {price:>8} {quantity:>8} {category:>12}")

            print("=" * 70)
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
                    input("Already on last page ... Press Enter to continue.")
            elif choice == "P":
                if page > 1:
                    page -= 1
                else:
                    input("Already on first page... Press Enter to continue.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
    
    def update_product(self):
        W = 50
        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("=" * W)
        print("UPDATE PRODUCT".center(W))
        print("-" * W)
    
        product_id = _get_int("Enter the product id to update: ")

        a = self.inventory.view_products(product_id)

        if a is None or len(a) == 0:
            print(f"No product found with ID {product_id}.")
            input("\nPress any key to continue...")
            return
        
        print("1. Name")
        print("2. Price")
        print("3. Quantity")
        print("4. Sku")
        choice = _get_int("Enter the field to update: ")

        field = self.inventory.select_option(choice)
        value = input(f"Enter the new value for {field}: ")

        self.inventory.update_product(product_id, field, value)
        print(f"Product {field} updated successfully.")

        input("\nPress any key to continue...")
    
    def delete_product(self):
        W = 50
        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("=" * W)
        print("DELETE PRODUCT".center(W))
        print("-" * W)
        product_id = _get_int("Enter the product id to delete: ")

        is_exist = self.inventory.search_product(product_id)
        if not is_exist:
            print(f"No product found with ID {product_id}.")
            input("\nPress any key to continue...")
            return
        
        self.inventory.delete_product(product_id)
        print(f"Product with ID {product_id} deleted successfully.")

        input("\nPress any key to continue...")

            
if __name__ == "__main__":
    ui = InventoryUI()
    ui.run()