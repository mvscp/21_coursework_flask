from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.user import User
from setup_db import db
from views.directors import directors_ns
from views.genres import genres_ns
from views.movies import movies_ns
from views.users import user_ns
from views.auth import auth_ns


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    #create_data(app, db)


def create_data(app: Flask, db):
    with app.app_context():
        db.create_all()
        u1 = User(username='vasya', password='<PASSWORD>', role='user')
        u2 = User(username='oleg', password='qwerty', role='user')
        u3 = User(username='gleb', password='pwd', role='admin')
        db.session.add_all((u1, u2, u3))
        db.session.commit()


if __name__ == '__main__':
    app = create_app(Config())
    app.run()
