import pytest
from unittest.mock import MagicMock
from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director1 = Director(id=1, name='director1')
    director2 = Director(id=2, name='director2')
    director3 = Director(id=3, name='director3')

    director_dao.get_by_id = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(director_dao)

    def test_get_by_id(self):
        director = self.director_service.get_by_id(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0

    def test_create(self):
        director_data = {
            'name': 'director1'
        }
        director = self.director_service.create(director_data)
        assert director is not None
        assert director.id is not None

    def test_update(self):
        director_data = {
            'name': 'director1'
        }
        self.director_service.update(director_data)

    def test_delete(self):
        self.director_service.delete(3)
