from flask_restx import Resource, Namespace
from container import director_service
from dao.model.director import DirectorSchema

directors_ns = Namespace('directors')
director_schema = DirectorSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        director = director_service.get_by_id(id)
        return director_schema.dump(director), 200
