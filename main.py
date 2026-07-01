from Inventory.inventory_ui import InventoryUI
from schedular import run_task
from Auth.authentication_ui import AuthenticationUI
import os 
class Application:

    def __init__(self):
        self.inventory = InventoryUI(self)
        self.auth = AuthenticationUI(self)
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
            self.clear_screen()
            option = self._welcome_menu()
            
            if option == "1":
                self.clear_screen()
                result = self.auth.login_menu()
                self.current_user = result

                while self.current_user:
                    self.clear_screen()
                    self.inventory.run()
            
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


            
