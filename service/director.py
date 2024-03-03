from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_by_id(self, id: int):
        return self.dao.get_by_id(id)

    def get_all(self, filters: dict = None):
        return self.dao.get_all(filters)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, data: dict):
        director = self.get_by_id(data.get('id'))
        director.name = data['name']
        return self.dao.update(director)

    def partial_update(self, data: dict):
        director = self.get_by_id(data.get('id'))

        if data.get('name'):
            director.name = data.get('name')

        return self.dao.update(director)

    def delete(self, id: int):
        self.dao.delete(id)