from flask import request
from flask_restx import Resource, Namespace
from container import director_service
from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required

directors_ns = Namespace('directors')
director_schema = DirectorSchema()


@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        return director_schema.dump(directors, many=True), 200

    @admin_required
    def post(self):
        director = director_service.create(request.json)
        return '', 201, {'location': f"/directors/{director.id}"}


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    @auth_required
    def get(self, id):
        director = director_service.get_by_id(id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, id):
        request_data = request.json
        request_data['id'] = id
        director_service.update(request_data)
        return '', 204

    @admin_required
    def patch(self, id):
        request_data = request.json
        request_data['id'] = id
        director_service.partial_update(request_data)
        return '', 204

    @admin_required
    def delete(self,id):
        director_service.delete(id)
        return '', 204
