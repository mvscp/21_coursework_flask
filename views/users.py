from flask import request
from flask_restx import Namespace, Resource
from container import user_service
from dao.model.user import UserSchema
from decorators import auth_required
from constants import JWT_SECRET, JWT_ALGORITHM
import jwt

users_ns = Namespace('users')
user_ns = Namespace('user')
user_schema = UserSchema()


@users_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        return user_schema.dump(users, many=True), 200

    def post(self):
        user = user_service.create(request.json)
        return '', 201, {'Location': f'/users/{user.id}'}


@users_ns.route('/<int:id>/')
class UserView(Resource):
    def get(self, id):
        user = user_service.get_by_id(id)
        return user_schema.dump(user), 200

    def put(self, id):
        request_data = request.json
        request_data['id'] = id
        user_service.update(request_data)
        return '', 204

    def delete(self, id):
        user_service.delete(id)
        return '', 204


@user_ns.route('/')
class UserResource(Resource):
    @auth_required
    def get(self):
        token = request.headers.get('Authorization').split('Bearer ')[-1]
        data = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = user_service.get_by_email(data.get('email'))
        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        token = request.headers.get('Authorization').split('Bearer ')[-1]
        token_data = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_data = request.json
        user_data['email'] = token_data['email']
        user_service.partial_update(user_data)
        return '', 204


@user_ns.route('/password')
class PasswordResource(Resource):
    @auth_required
    def put(self):
        token = request.headers.get('Authorization').split('Bearer ')[-1]
        token_data = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        data = request.json
        data['email'] = token_data['email']

        if not data.get('old_password') or not data.get('new_password'):
            return '', 400

        user_service.update_password(data)
        return '', 204
