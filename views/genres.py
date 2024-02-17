from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.genre import GenreSchema

genres_ns = Namespace('genres')
genre_schema = GenreSchema()


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genre_schema.dump(genres, many=True), 200


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genre_service.get_by_id(id)
        return genre_schema.dump(genre), 200