from flask import request
from flask_restx import Namespace, Resource
from container import movie_service, user_service
from dao.model.movie import MovieSchema
from decorators import auth_required, admin_required
from constants import JWT_SECRET, JWT_ALGORITHM
import jwt

movies_ns = Namespace('movies')
movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        movies = movie_service.get_all(request.args)
        return movie_schema.dump(movies, many=True), 200

    @admin_required
    def post(self):
        movie = movie_service.create(request.json)
        return '', 201, {"location": f"/movies/{movie.id}"}


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    @auth_required
    def get(self, id):
        movie = movie_service.get_by_id(id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, id):
        request_data = request.json
        request_data['id'] = id
        movie_service.update(request_data)
        return '', 204

    @admin_required
    def patch(self, id):
        request_data = request.json
        request_data['id'] = id
        movie_service.partial_update(request_data)
        return '', 204

    @admin_required
    def delete(self, id):
        movie_service.delete(id)
        return '', 204


@movies_ns.route('/favorites/<int:movie_id>')
class FavoritesView(Resource):
    @auth_required
    def post(self, movie_id):
        token = request.headers.get('Authorization').split('Bearer ')[-1]
        email = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])['email']
        user_service.add_favorite(email, movie_id)
        return '', 201

    @auth_required
    def delete(self, movie_id):
        token = request.headers.get('Authorization').split('Bearer ')[-1]
        email = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])['email']
        user_service.delete_favorite(email, movie_id)
        return '', 204
