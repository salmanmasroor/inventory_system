import os

from cli.auth_ui import AuthUI
from cli.product_ui import ProductUI


class Application:
    def __init__(self):
        self.product_ui = ProductUI(self)
        self.auth_ui = AuthUI(self)
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
        ]

        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        print("0. Exit")

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
                result = self.auth_ui.login_menu()
                self.current_user = result

                while self.current_user:
                    self.clear_screen()
                    self.product_ui.run()

            elif option == "2":
                self.clear_screen()
                result = self.auth_ui.registration_menu()

                if result:
                    print("User Successfully Registered")

            elif option == "0":
                print("Closed!")
                break

            else:
                pass

if __name__ == "__main__":
    app = Application()
    app.run()