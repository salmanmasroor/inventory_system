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

create_table()