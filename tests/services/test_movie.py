import pytest
from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from dao.model.genre import Genre
from dao.model.director import Director


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)
    movie1 = Movie(id=1, title='Movie 1', description='description1',
                   trailer='trailer1', year=2024, rating=8.1, genre_id=1, director_id=1)
    movie2 = Movie(id=2, title='Movie 2', description='description2',
                   trailer='trailer2', year=2023, rating=8.4, genre_id=2, director_id=1)
    movie3 = Movie(id=3, title='Movie 3', description="description3",
                   trailer='trailer3', year=2022, rating=7.5, genre_id=1, director_id=2)

    movie_dao.get_by_id = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_by_id(self):
        movie = self.movie_service.get_by_id(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_data = {
            'title': 'Test',
            'description': 'description_test'
        }
        movie = self.movie_service.create(movie_data)
        assert movie.id is not None

    def test_update(self):
        movie_data = {
            'title': 'Test',
            'description': 'description_test'
        }
        self.movie_service.update(movie_data)

    def test_delete(self):
        self.movie_service.delete(2)
