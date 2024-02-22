from flask import request
from flask_restx import Namespace, Resource
from container import user_service
from dao.model.user import UserSchema

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        users = user_service.get_all()
        return user_schema.dump(users, many=True), 200

    def post(self):
        user = user_service.create(request.json)
        return '', 201, {'Location': f'/users/{user.id}'}


@user_ns.route('/<int:id>')
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