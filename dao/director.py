from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> Director:
        return self.session.query(Director).get(id)

    def get_all(self, filters: dict = None):
        directors = self.session.query(Director)
        if filters.get('page'):
            directors = directors.paginate(page=int(filters.get('page')), per_page=12, error_out=False)
            return directors.items
        return directors.all()

    def create(self, data: dict) -> Director:
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, director: Director) -> Director:
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, id: int):
        director = self.get_by_id(id)
        self.session.delete(director)
        self.session.commit()
