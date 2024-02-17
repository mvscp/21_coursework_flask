from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> Director:
        return self.session.query(Director).get(id)

    def get_all(self):
        return self.session.query(Director).all()
