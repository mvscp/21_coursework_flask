from flask import request
from flask_restx import Resource, Namespace
from container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class RegisterResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            return '', 400

        user_service.create(data)
        return '', 201


@auth_ns.route('/login')
class LoginResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if not email or not password:
            return '', 401

        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        data = request.json
        refresh_token = data.get('refresh_token', None)

        if not refresh_token:
            return '', 400

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
