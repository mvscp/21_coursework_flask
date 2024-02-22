from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_by_id(self, id: int):
        return self.dao.get_by_id(id)

    def get_all(self, filters: dict = None):
        return self.dao.get_all(filters)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, data: dict):
        movie = self.get_by_id(data.get('id'))
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        return self.dao.update(movie)

    def partial_update(self, data: dict):
        movie = self.get_by_id(data.get('id'))

        if data.get('title'):
            movie.title = data.get('title')
        if data.get('description'):
            movie.description = data.get('description')
        if data.get('trailer'):
            movie.trailer = data.get('trailer')
        if data.get('year'):
            movie.year = data.get('year')
        if data.get('rating'):
            movie.rating = data.get('rating')
        if data.get('genre_id'):
            movie.genre_id = data.get('genre_id')
        if data.get('director_id'):
            movie.director_id = data.get('director_id')

        return self.dao.update(movie)

    def delete(self, id: int):
        self.dao.delete(id)
