import sqlite3
import hashlib
import getpass
from model import User
class Authentioncation:

    def connect(self):
        return sqlite3.connect("inventory.db")
    
    def _query(self,query,*args):
        conn = self.connect()
        cursor= conn.cursor()

        cursor.execute(query,*args)
        conn.commit()

        conn.close()
    
    def email_exists(self,email):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, email FROM users WHERE email = ? 
                       """,(email,))
        rows = cursor.fetchall()
        conn.close()
        if len(rows) >= 1:
            return True
        else:
            return False
        
    def registration_menu(self):
        print("=" * 55)
        print("             SMART INVENTORY MANAGEMENT")
        print("=" * 55)
        print("                 REGISTER ACCOUNT")
        print("-" * 55)

        first_name = input("1. First Name : ")
        last_name = input("2. Last Name  : ")
        email = input("3. Email      : ")
        password = getpass.getpass("4. Password   : ")

        while True:
            if first_name.strip().isalpha():
                if last_name.strip().isalpha():
                    if "@" in email and "." in email:
                        if  not self.email_exists(email):
                            if len(password) >= 8:
                                break
                            else:
                                print("Password must have atleast 8 characters")
                                password = getpass.getpass("Password   : ")
                        else:
                            print("This Email already Exist")
                            email = input("Email      : ")  
                    else:
                        print("Please Enter the Correct Email")
                        email = input("Email      : ")
                else:
                    print("Only Alphabet allowed")
                    last_name = input("Last Name  : ")
            else:
                print("Only Alphabet allowed")
                first_name = input("First Name : ")

        print("-" * 55)

        user = User(first_name,last_name,email,password)
        result = self.register(user)
        return result

    def register(self,user):
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        try:
            self._query("INSERT INTO users(first_name,last_name,email,password) values (?,?,?,?)",(user.first_name,user.last_name,user.email,hashed_password))
            return True
        except Exception as e:
            print(e)
            return False
    
    def login_menu(self):
        print("=" * 55)
        print("             SMART INVENTORY MANAGEMENT")
        print("=" * 55)
        print("                   LOGIN")
        print("-" * 55)
        user = None
        while True:
            email = input("1. Email    : ")
            password = getpass.getpass("2. Password : ")

            print("-" * 55)

            is_email_exist = self.email_exists(email)
            
            if is_email_exist:
                user = self.login(email, password)
                if user:
                    print("\nLogin Successful!")
                    input("\nPress Enter to continue...")
                    return user
                else:
                    print("\nInvalid Password!")
                    response = input("\nPress Enter to try again (else press (n/N) to stop proceess)...")
                    if response == 'n' or response == 'N':
                        break
                    else:
                        pass
            else:
                print("Email Does not Exist")
                response = input("\nPress Enter to try again (else press (n/N) to stop proceess)...")
                if response == 'n' or response == 'N':
                    break
                else:
                    pass
                

    def login(self,email,password):
        conn = self.connect()
        cursor = conn.cursor()
        password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("""
            SELECT id, first_name, last_name, email FROM users WHERE email = ? AND password = ?
                       """,(email,password))
        rows = cursor.fetchall()
        conn.close()

        return rows

if __name__ == "__main__":
    auth = Authentioncation()
    email = input("Enter the Email: ")
    password = input('Enter the Password: ')
 
    print(auth.login(email,password))
