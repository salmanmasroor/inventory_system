import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "inventory.db"

def connect():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
         CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT NOT NULL,
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
    conn.commit()
    conn.close()

def add_column(table_name, column_name, attributes):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(f"""
            ALTER TABLE {table_name}
            ADD COLUMN {column_name} {attributes};
        """)
        conn.commit()
    except sqlite3.OperationalError:
        pass
    finally:
        conn.close()

def category_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("PRAGMA table_info(products)")
    columns = [row[1] for row in cursor.fetchall()]
    if "category_id" not in columns:
        cursor.execute("ALTER TABLE products ADD COLUMN category_id INTEGER REFERENCES categories(id)")

    conn.commit()
    conn.close()

create_table()
user_table()
category_table()