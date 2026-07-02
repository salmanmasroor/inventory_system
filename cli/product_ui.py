import math

from cli.category_ui import CategoryUI
from cli.supplier_ui import SupplierUI
from core.utils import get_float, get_int
from models.product import Product
from services.category_service import CategoryService
from services.product_service import ProductService
from services.supplier_service import SupplierService


class ProductUI:
    def __init__(self, app=None):
        self.product_service = ProductService()
        self.category_service = CategoryService()
        self.supplier_service = SupplierService()
        self.app = app

    def _category_map(self):
        return {cat_id: name for cat_id, name in self.category_service.view_categories()}

    def _supplier_map(self):
        return {
            supplier.id: supplier.name
            for supplier in self.supplier_service.list_suppliers()
        }

    def _parse_product_row(self, row):
        pid = row[0]
        name = row[1] or ""
        price = row[2] if row[2] is not None else 0
        quantity = row[3] if row[3] is not None else 0
        sku = row[4] if len(row) > 4 else None
        category_id = row[5] if len(row) > 5 else None
        supplier_id = row[6] if len(row) > 6 else None
        return pid, sku, name, price, quantity, category_id, supplier_id

    def _category_label(self, category_id, category_map):
        if category_id is None:
            return "-"
        return category_map.get(category_id, "-")

    def _supplier_label(self, supplier_id, supplier_map):
        if supplier_id is None:
            return "-"
        return supplier_map.get(supplier_id, "-")

    def dashboard_menu(self, username="Admin"):
        width = 50

        options = [
            "Products",
            "Categories",
            "Suppliers",
        ]

        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("=" * width)
        print("MAIN MENU".center(width))
        print("-" * width)

        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")

        print("-" * width)
        print("  0. Exit")
        print("=" * width)

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
        elif result == "3":
            if self.app is not None:
                self.app.clear_screen()
            SupplierUI(self.app).display_menu()
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
            width = 50
            print("=" * width)
            print("SMART INVENTORY MANAGEMENT".center(width))
            print("=" * width)
            print("PRODUCTS".center(width))
            print("-" * width)

            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")

            print("-" * width)
            print("  0. Back")
            print("=" * width)

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
        width = 50
        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("=" * width)
        print("ADD PRODUCT".center(width))
        print("-" * width)
        category_list = self.category_service.view_categories()
        product_name = input("Product Name : ")
        sku = input("Sku : ")

        category_id = None
        if category_list:
            print("Categories : \n")
            for i, category in enumerate(category_list, 1):
                print(f"  {i}. {category[1]}")
            category_choice = get_int("Choose a category by number: ", min_value=1)
            if category_choice > len(category_list):
                print("Invalid category choice.")
                input("\nPress any key to continue...")
                return
            category_id = category_list[category_choice - 1][0]
        else:
            print("No categories available. Add categories first.\n")

        supplier_list = self.supplier_service.list_suppliers()
        supplier_id = None
        if supplier_list:
            print("Suppliers : ")
            for i, supplier in enumerate(supplier_list, 1):
                contact = supplier.contact or "-"
                print(f"\t {i}. {supplier.name} ({contact})")

            supplier_choice = get_int("\nChoose a supplier by number (0 to skip): ", min_value=0)
            if supplier_choice > len(supplier_list):
                print("Invalid supplier choice.")
                input("\nPress any key to continue...")
                return
            if supplier_choice > 0:
                supplier_id = supplier_list[supplier_choice - 1].id
        else:
            print("No suppliers available. You can add suppliers from the main menu.\n")

        quantity = get_int("Quantity : ")
        price = get_float("Price : ")

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
        print()
        print("[1]. Register")
        print("[0]. Back")

        while True:
            choose = input("Choose: ")
            
            if choose == "1":
                product = Product(product_name, sku, quantity, price, category_id, supplier_id)
                self.product_service.add_product(product)

                print("\nProduct added successfully!")
                input("\nPress any key to continue...")
                break
            
            elif choose == "0":
                if self.app is not None:
                    self.app.clear_screen()
                return
            else:
                print("Invalid Option")
                input("\nPress Enter to try again the proceess)...")

    def view_product(self, page_size=4):
        products = self.product_service.view_products()

        if not products:
            print("No products found.")
            return

        category_map = self._category_map()
        supplier_map = self._supplier_map()
        page = 1
        total_pages = math.ceil(len(products) / page_size)

        while True:
            self.app.clear_screen()
            width = 50
            print("=" * width)
            print("SMART INVENTORY MANAGEMENT".center(width))
            print("=" * width)
            print("VIEW PRODUCTS".center(width))
            print("-" * width)

            start = (page - 1) * page_size
            chunk = products[start:start + page_size]

            print("=" * 85)
            print(
                f"{'ID':<4} {'Name':<13} {'SKU':<8} {'Price':>8} "
                f"{'Stock':>8} {'Category':>12} {'Supplier':>12}"
            )
            print("=" * 85)

            for row in chunk:
                pid, sku, name, price, quantity, category_id, supplier_id = (
                    self._parse_product_row(row)
                )
                sku = sku or "-"
                category = self._category_label(category_id, category_map)
                supplier = self._supplier_label(supplier_id, supplier_map)
                print(
                    f"{pid:<4} {name:<13} {sku:<8} {price:>8} {quantity:>8} "
                    f"{category:>12} {supplier:>12}"
                )

            print("=" * 85)
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
                    input("Already on last page ... Press Enter to continue.")
                    break
                if choice == "P":
                    if page > 1:
                        page -= 1
                        break
                    input("Already on first page... Press Enter to continue.")
                    break
                if choice == "0":
                    return
                print("Invalid choice.")

    def search_product(self, page_size=2):
        width = 50
        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("=" * width)
        print("SEARCH PRODUCT".center(width))
        print("-" * width)

        product_id = input("Enter the name or id for search: ")
        try:
            change = int(product_id)
        except ValueError:
            change = product_id

        products = self.product_service.search_product(change)
        category_map = self._category_map()
        supplier_map = self._supplier_map()

        page = 1
        total_pages = max(1, math.ceil(len(products) / page_size)) if products else 1

        while True:
            start = (page - 1) * page_size
            chunk = products[start:start + page_size]

            print("=" * 85)
            print(
                f"{'ID':<4} {'Name':<13} {'SKU':<8} {'Price':>8} "
                f"{'Stock':>8} {'Category':>12} {'Supplier':>12}"
            )
            print("=" * 85)

            if len(chunk) == 0:
                print()
                print("No Products Found".center(80))
                print()
            else:
                for row in chunk:
                    pid, sku, name, price, quantity, category_id, supplier_id = (
                        self._parse_product_row(row)
                    )
                    sku = sku or "-"
                    category = self._category_label(category_id, category_map)
                    supplier = self._supplier_label(supplier_id, supplier_map)
                    print(
                        f"{pid:<4} {name:<13} {sku:<8} {price:>8} {quantity:>8} "
                        f"{category:>12} {supplier:>12}"
                    )

            print("=" * 85)
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
        width = 50
        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("=" * width)
        print("UPDATE PRODUCT".center(width))
        print("-" * width)

        product_id = get_int("Enter the product id to update: ")
        products = self.product_service.view_products(product_id)

        if products is None or len(products) == 0:
            print(f"No product found with ID {product_id}.")
            input("\nPress any key to continue...")
            return

        print("1. Name")
        print("2. Price")
        print("3. Quantity")
        print("4. Sku")
        choice = get_int("Enter the field to update: ")

        field = self.product_service.select_option(choice)
        value = input(f"Enter the new value for {field}: ")

        self.product_service.update_product(product_id, field, value)
        print(f"Product {field} updated successfully.")
        input("\nPress any key to continue...")

    def delete_product(self):
        width = 50
        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("=" * width)
        print("DELETE PRODUCT".center(width))
        print("-" * width)
        product_id = get_int("Enter the product id to delete: ")

        is_exist = self.product_service.search_product(product_id)
        if not is_exist:
            print(f"No product found with ID {product_id}.")
            input("\nPress any key to continue...")
            return

        self.product_service.delete_product(product_id)
        print(f"Product with ID {product_id} deleted successfully.")
        input("\nPress any key to continue...")
