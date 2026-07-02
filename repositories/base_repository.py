import sqlite3

from config import DB_PATH


class BaseRepository:
    def __init__(self, db_path=None):
        self.db_path = db_path or DB_PATH

    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount

    def fetchall(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetchone(self, query, params=()):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
