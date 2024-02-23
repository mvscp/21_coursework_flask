import hashlib
import hmac
import base64
from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_by_id(self, id: int):
        return self.dao.get_by_id(id)

    def get_by_username(self, username: str):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data: dict):
        data['password'] = self.get_hash(data.get('password'))
        return self.dao.create(data)

    def update(self, data: dict):
        user = self.get_by_id(data['id'])
        user.username = data['name']
        user.password = self.get_hash(data.get('password'))
        user.role = data['role']
        return self.dao.update(user)

    def delete(self, id: int):
        self.dao.delete(id)

    def get_hash(self, password: str):
        return base64.b64encode(hashlib.pbkdf2_hmac('sha256',
                                   password.encode('utf-8'),
                                   PWD_HASH_SALT,
                                   PWD_HASH_ITERATIONS))

    def compare_passwords(self, hashed_password: str, password: str) -> bool:
        return hmac.compare_digest(base64.b64decode(hashed_password),
                                   hashlib.pbkdf2_hmac('sha256',
                                                       password.encode('utf-8'),
                                                       PWD_HASH_SALT,
                                                       PWD_HASH_ITERATIONS)
                                   )
