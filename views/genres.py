from flask import request
from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required

genres_ns = Namespace('genres')
genre_schema = GenreSchema()


@genres_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres, many=True), 200

    @admin_required
    def post(self):
        genre = genre_service.create(request.json)
        return '', 201, {"location": f"/genres/{genre.id}"}


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    @auth_required
    def get(self, id):
        genre = genre_service.get_by_id(id)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, id):
        request_data = request.json
        request_data['id'] = id
        genre_service.update(request_data)
        return '', 204

    @admin_required
    def patch(self, id):
        request_data = request.json
        request_data['id'] = id
        genre_service.partial_update(request_data)
        return '', 204

    @admin_required
    def delete(self, id):
        genre_service.delete(id)
        return '', 204
