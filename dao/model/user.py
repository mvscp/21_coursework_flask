from marshmallow import Schema, fields
from setup_db import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    favorite_genre = db.Column(db.Integer, db.ForeignKey('genre.id'))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
