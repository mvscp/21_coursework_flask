from dao.director import DirectorDAO
from dao.model.director import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_by_id(self, id: int) -> Director:
        return self.dao.get_by_id(id)

    def get_all(self):
        return self.dao.get_all()
