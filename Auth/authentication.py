import sqlite3
import hashlib
import getpass

from database import DB_PATH
from models.user import User


class Authentication:

    def connect(self):
        return sqlite3.connect(DB_PATH)
    
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

    def register(self,user):
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        try:
            self._query("INSERT INTO users(first_name,last_name,email,password) values (?,?,?,?)",(user.first_name,user.last_name,user.email,hashed_password))
            return True
        except Exception as e:
            print(e)
            return False

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
    auth = Authentication()
    email = input("Enter the Email: ")
    password = input('Enter the Password: ')
 
    print(auth.login(email,password))
