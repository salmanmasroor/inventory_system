import getpass

from models.user import User
from services.auth_service import AuthService


class AuthUI:
    def __init__(self, app=None):
        self.auth = AuthService()
        self.app = app
        self.registration_title = "REGISTRATION"
        self.login_title = "LOGIN"

    def registration_menu(self):
        while True:
            self.app.clear_screen()
            self._design(self.registration_title)
            first_name = input("1. First Name : ")
            last_name = input("2. Last Name  : ")
            email = input("3. Email      : ")
            password = getpass.getpass("4. Password   : ")

            print()
            print("[1]. Register")
            print("[0]. Back")

            choose = input("Choose: ")

            if choose == "1":
                while True:
                    if len(first_name) == 0:
                        print("First Name can not be Empty ")
                        first_name = input("First Name : ")
                        continue

                    if not first_name.isalpha():
                        print("Only Alphabets Allowed")
                        first_name = input("First Name : ")
                        continue

                    if len(last_name) > 0 and not last_name.isalpha():
                        print("Only Alphabets Allowed")
                        last_name = input("Last Name  : ")
                        continue

                    if "@" not in email:
                        print("Enter the Correct Email")
                        email = input("Email      : ")
                        continue

                    if self.auth.email_exists(email):
                        print("Email Already Exist")
                        email = input("Email      : ")
                        continue

                    if len(password) < 8:
                        print("Password must have atleast 8 characters")
                        password = getpass.getpass("4. Password   : ")
                        continue

                    break

                user = User(first_name, last_name, email, password)
                result = self.auth.register(user)

                if result:
                    print("\nRegistered Successfully!")
                    input("\nEnter any button to continue ......")
                    break
            elif choose == "0":
                if self.app is not None:
                    self.app.clear_screen()
                return
            else:
                print("Invalid Option")
                input("\nPress Enter to try again the proceess)...")

    def _design(self,title):
        width = 50

        print("=" * width)
        print("SMART INVENTORY MANAGEMENT".center(width))
        print("-" * width)
        print(title.center(width))
        print("=" * width)

    def login_menu(self):
        while True:
            self.app.clear_screen()
            self._design(self.login_title)
            email = input("1. Email    : ")
            password = getpass.getpass("2. Password : ")

            print()
            print("[1]. Login")
            print("[0]. Back")

            choose = input("Choose: ")

            if choose == "1":
                if self.auth.email_exists(email):
                    user_login = self.auth.login(email, password)

                    if user_login:
                        return user_login

                    print("\nInvalid Password!")
                    input("\nPress Enter to try again .....")
                else:
                    print("Email Does not Exist")
                    input("\nPress Enter to try again .....")

            elif choose == "0":
                if self.app is not None:
                    self.app.clear_screen()
                return None

            else:
                print("Invalid Option")
                input("\nPress Enter to try again the proceess)...")
