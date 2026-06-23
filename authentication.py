import sqlite3
import hashlib

class Authentioncation:

    def connect(self):
        return sqlite3.connect("inventory.db")
    
    def add_user(self,user):
        conn = self.connect()
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        cursor.execute(""" 
            INSERT INTO users(first_name,last_name,email,password) values (?,?,?,?)   
            """,(user.first_name,user.last_name,user.email,hashed_password))
        conn.commit()
        conn.close()

    def login(self,email,password):
        conn = self.connect()
        cursor = conn.cursor()
        password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute("""
            SELECT * FROM users WHERE email = ? AND password = ?
                       """,(email,password))
        rows = cursor.fetchall()
        conn.close()

        return rows

if __name__ == "__main__":
    auth = Authentioncation()
    email = input("Enter the Email: ")
    password = input('Enter the Password: ')

    print(auth.login(email,password))
