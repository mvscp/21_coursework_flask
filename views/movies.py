from flask import request
from flask_restx import Namespace, Resource
from container import movie_service
from dao.model.movie import MovieSchema

movies_ns = Namespace('movies')
movie_schema = MovieSchema()


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.get_all(request.args)
        return movie_schema.dump(movies, many=True), 200

    def post(self):
        movie = movie_service.create(request.json)
        return '', 201, {"location": f"/movies/{movie.id}"}


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movie_service.get_by_id(id)
        return movie_schema.dump(movie), 200

    def put(self, id):
        request_data = request.json
        request_data['id'] = id
        movie_service.update(request_data)
        return '', 204

    def patch(self, id):
        request_data = request.json
        request_data['id'] = id
        movie_service.partial_update(request_data)
        return '', 204

    def delete(self, id):
        movie_service.delete(id)
        return '', 204
