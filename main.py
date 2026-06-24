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
          
    def run(self):
        while self.current_user is None:
            print("====== Welcome =======")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("===Register Yourself===")
                self.auth_menu()
            elif choice == "2":
                print("===Login===")
                result = self.login_menu()
                print(result)
                self.current_user = result
                while self.current_user:
                    result = self.inventory_menu()
                    if result is False:
                        break
        
    def auth_menu(self):
        first_name = input("Enter the First Name: ")
        last_name = input("Enter the Last Name: ")
        email = input("Enter the Email: ")
        password = getpass.getpass("Enter the Password: ")

        user = User(first_name,last_name,email,password)
        self.auth.register(user)
        
        print("\n Registered Successful!")
    
    def login_menu(self):
        email = input("Enter the Email: ")
        password = getpass.getpass('Enter the Password: ')
        user = self.auth.login(email,password)

        if user:
            print("Login")
            return user
        else:
            pass
    
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


if __name__ == "__main__":

    app = Application()
    app.run()


            
