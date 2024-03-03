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

    def get_by_email(self, email: str):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data: dict):
        data['password'] = self.get_hash(data.get('password'))
        return self.dao.create(data)

    def update(self, data: dict):
        user = self.get_by_id(data['id'])
        user.name = data['name']
        user.surname = data['surname']
        user.password = self.get_hash(data.get('password'))
        user.role = data['role']
        return self.dao.update(user)

    def partial_update(self, data: dict):
        user = self.get_by_email(data['email'])

        if data.get('name'):
            user.name = data.get('name')
        if data.get('surname'):
            user.surname = data.get('surname')
        if data.get('favorite_genre'):
            user.favorite_genre = data.get('favorite_genre')

        return self.dao.update(user)

    def update_password(self, data: dict):
        user = self.get_by_email(data['email'])
        if self.compare_passwords(user.password, data.get('old_password')):
            user.password = self.get_hash(data.get('new_password'))
            return self.dao.update(user)
        return None

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
