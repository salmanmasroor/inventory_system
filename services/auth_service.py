import hashlib

from models.user import User
from repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, repository=None):
        self.repository = repository or UserRepository()

    def email_exists(self, email):
        return self.repository.email_exists(email)

    def register(self, user):
        hashed_password = self._hash_password(user.password)
        try:
            self.repository.create(
                user.first_name,
                user.last_name,
                user.email,
                hashed_password,
            )
            return True
        except Exception as exc:
            print(exc)
            return False

    def login(self, email, password):
        hashed_password = self._hash_password(password)
        return self.repository.authenticate(email, hashed_password)

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
