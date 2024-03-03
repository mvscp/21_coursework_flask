from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_by_id(self, id: int):
        return self.dao.get_by_id(id)

    def get_all(self, filters: dict = None):
        return self.dao.get_all(filters)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, data: dict):
        genre = self.get_by_id(data.get('id'))
        genre.name = data['name']
        return self.dao.update(genre)

    def partial_update(self, data: dict):
        genre = self.get_by_id(data.get('id'))

        if data.get('name'):
            genre.name = data.get('name')

        return self.dao.update(genre)

    def delete(self, id: int):
        self.dao.delete(id)
