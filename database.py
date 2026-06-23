import sqlite3 

def connect():
    conn = sqlite3.connect("inventory.db")
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL   
            )          
                   """)
    conn.commit()
    conn.close()

def user_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL CHECK(length(first_name) <= 50),
                last_name TEXT NULL CHECK(length(last_name) <= 50),
                email UNIQUE NOT NULL,
                password TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   ) 
                   """)
    conn.cursor()
    conn.close()

user_table()
create_table()