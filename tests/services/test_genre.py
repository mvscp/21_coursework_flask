import pytest
from unittest.mock import MagicMock
from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre1 = Genre(id=1, name='genre1')
    genre2 = Genre(id=2, name='genre2')
    genre3 = Genre(id=3, name='genre3')

    genre_dao.get_by_id = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=2))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_by_id(self):
        genre = self.genre_service.get_by_id(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres is not None
        assert len(genres) > 0

    def test_create(self):
        genre_data = {
            'name': 'genre1'
        }
        genre = self.genre_service.create(genre_data)
        assert genre is not None
        assert genre.id is not None

    def test_update(self):
        genre_data = {
            'name': 'genre1'
        }
        self.genre_service.update(genre_data)

    def test_delete(self):
        self.genre_service.delete(3)
