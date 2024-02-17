from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> Genre:
        return self.session.query(Genre).get(id)

    def get_all(self):
        return self.session.query(Genre).all()
