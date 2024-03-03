from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError

from dao.model.movie import Movie
from dao.model.user import User
from dao.model.user_movie import UserMovie


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> User:
        return self.session.query(User).get(id)

    def get_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

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

    def get_favorites(self, email: str):
        user = self.get_by_email(email)
        movies_id = self.session.query(Movie).join(UserMovie).filter(UserMovie.user_id == user.id)
        return movies_id.all()


    def add_favorite(self, email: str, movie_id: int):
        user = self.get_by_email(email)
        try:
            self.session.add(UserMovie(user_id=user.id, movie_id=movie_id))
            self.session.commit()
        except IntegrityError:
            return

    def delete_favorite(self, email: str, movie_id: int):
        user = self.get_by_email(email)
        record = self.session.query(UserMovie).filter(UserMovie.user_id == user.id, UserMovie.movie_id == movie_id).first()
        try:
            self.session.delete(record)
            self.session.commit()
        except UnmappedInstanceError:
            return
