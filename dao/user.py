from dao.model.user import User

class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> User:
        return self.session.query(User).get(id)

    def get_by_username(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data: dict) -> User:
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, id: int):
        user = self.get_by_id(id)
        self.session.delete(user)
        self.session.commit()
