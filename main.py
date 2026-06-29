from model import Product, User
from inventory import Inventory
from schedular import run_task
from authentication import Authentioncation
import os 
import getpass

class Application:

    def __init__(self):
        self.inventory = Inventory()
        self.auth = Authentioncation()
        self.current_user = None
    
    def _welcome_menu(self):
        print("=" * 50)
        print("        SMART INVENTORY MANAGEMENT".center(40))
        print("=" * 50)
        print()
        print("Welcome!\n")

        options = [
            "Login",
            "Register",
            "Exit"
        ]

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        print("-" * 42)

        return input("Select an option: ")
    
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
    
    def run(self):
        while self.current_user is None:
            option = self._welcome_menu()
            
            if option == "1":
                self.clear_screen()
                result = self.auth.login_menu()
                self.current_user = result

                while self.current_user:
                    self.inventory.dashboard_menu()
            
            elif option == "2":
                self.clear_screen()
                result = self.auth.registration_menu()

                if result:
                    print("User Successfully Registered")
            
            elif option == "3":
                print("Closed!")
                break

            else:
                self._welcome_menu()


if __name__ == "__main__":

    app = Application()
    app.run()


            




""" 
    def inventory_menu(self):
        print("\n=== INVENTORY SYSTEM ===")
        print("1. Add Product")
        print("2. View Product")
        print("3. Delete Product")
        print("4. Update Product")
        print("5. Search Product")
        print("6. Logout")
        print("7. Exit")
        option = input("Enter Choice: ")

        if option == "1":
            price = None
            quantity = None
            product_name  = input("Enter the Product Name: ")
            while price is None:
                try:
                    price = float(input("Enter the Price: "))
                except ValueError:
                    print("Invalid price. Please enter a numeric/decimal value.")

            while quantity is None:
                try:
                    quantity = int(input("Enter the Qty: "))
                except ValueError:
                    print("Invalid quantity. Please enter an integer value.")
            
            product = Product(product_name,price,quantity)

            print(product)
            self.inventory.add_product(product)
            print("Product added!")
        
        elif option == "2":
            data = self.inventory.view_products()
            print("ID  | Product Name | Quanity  | Price")
            print("--------------------------------------")

            for row in data:
                print(
                    str(row[0]).ljust(3),
                    "|",
                    str(row[1]).ljust(12),
                    "|",
                    str(row[3]).ljust(8),
                    "|",
                    str(row[2])
                )
        elif option == "3":
            try:
                product_id = int(input("Enter the Product ID to delete:"))
                self.inventory.delete_product(product_id)
                print("Product deleted!")
            except ValueError:
                print("Invalid ID. Please enter an integer value.")
        elif option == "4":
            try:
                product_id = int(input("Enter the Product ID to Update:"))
                print("What you want to Update")
                print("1. Name")
                print("2. Price")
                print("3. Quantity")
                choice = int(input("Enter to Choose:"))
                data = self.inventory.select_option(choice)
                value = input("Enter the value: ")
                self.inventory.update_product(product_id,data,value)
                print("updated !")
            except ValueError:
                print("Error")

        elif option == "5":
            product_id = input("Enter the name or id for search: ")
            try:
                change = int(product_id)
            except ValueError:
                change = product_id

            print(change)
            data = self.inventory.search_product(change)
            
            print("ID  | Product Name | Quanity  | Price")
            print("--------------------------------------")

            for row in data:
                print(
                    str(row[0]).ljust(3),
                    "|",
                    str(row[1]).ljust(12),
                    "|",
                    str(row[3]).ljust(8),
                    "|",
                    str(row[2])
                )
        elif option == "6":
            self.current_user = None

        elif option == "7":
            print("Closed!")
            return False
        
        else:
            print("Invalid Choice")
""" 