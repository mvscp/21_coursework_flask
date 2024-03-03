from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> Genre:
        return self.session.query(Genre).get(id)

    def get_all(self, filters: dict = None):
        genres = self.session.query(Genre)
        if filters.get('page'):
            genres = genres.paginate(page=int(filters.get('page')), per_page=12, error_out=False)
            return genres.items
        return genres.all()

    def create(self, data: dict) -> Genre:
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre: Genre) -> Genre:
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, id: int):
        genre = self.get_by_id(id)
        self.session.delete(genre)
        self.session.commit()
