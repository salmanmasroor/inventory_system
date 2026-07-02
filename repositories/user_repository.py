from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def email_exists(self, email):
        row = self.fetchone(
            "SELECT id, email FROM users WHERE email = ?",
            (email,),
        )
        return row is not None

    def create(self, first_name, last_name, email, hashed_password):
        self.execute(
            "INSERT INTO users(first_name, last_name, email, password) VALUES (?, ?, ?, ?)",
            (first_name, last_name, email, hashed_password),
        )

    def authenticate(self, email, hashed_password):
        return self.fetchall(
            "SELECT id, first_name, last_name, email FROM users "
            "WHERE email = ? AND password = ?",
            (email, hashed_password),
        )
