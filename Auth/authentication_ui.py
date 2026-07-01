import getpass

try:
    from .authentication import Authentication
    from models.user import User
except ImportError:
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from Auth.authentication import Authentication
    from models.user import User


class AuthenticationUI:

    def __init__(self, app=None):
        self.auth = Authentication()
        self.app = app
        self.registration_title = "REGISTRATION"
        self.login_title = "LOGIN"

    def registration_menu(self):
        print("=" * 55)
        print(self.registration_title.center(50))
        print("-" * 55)


        while True:
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

    def login_design(self):
        W = 50

        print("=" * W)
        print("SMART INVENTORY MANAGEMENT".center(W))
        print("-" * W)
        print(self.login_title.center(W))
        print("=" * W)            


    def login_menu(self): 
        user = None
        while True:
            self.app.clear_screen()
            self.login_design()
            email = input("1. Email    : ")
            password = getpass.getpass("2. Password : ")

            print()
            print("[1]. Login")
            print("[0]. Back")
            
            choose = input("Choose: ")

            if choose == "1": 
                    is_email_exist = self.auth.email_exists(email)
                    if is_email_exist is True:
                        user_login = self.auth.login(email,password)
                        user = user_login

                        if user:
                            return user
                        else:
                            print("\nInvalid Password!")
                            input("\nPress Enter to try again (else press (n/N) to stop proceess)...")
                            
                    else:
                        print("Email Does not Exist")
                        input("\nPress Enter to try again (else press (n/N) to stop proceess)...")
                        
            elif choose == "0":
                if self.app is not None:
                    self.app.clear_screen()
                return None
            else:
                print("Invalid Option")
                input("\nPress Enter to try again the proceess)...")

if __name__ == "__main__":
    ui = AuthenticationUI()
    a = ui.registration_menu()
    print(a)
