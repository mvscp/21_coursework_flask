from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id: int) -> Movie:
        return self.session.query(Movie).get(id)

    def get_all(self, filters: dict = None):
        movies = self.session.query(Movie)
        if filters:
            if filters.get('year'):
                movies = movies.filter(Movie.year == filters.get('year'))
            if filters.get('rating'):
                movies = movies.filter(Movie.rating == filters.get('rating'))
            if filters.get('genre_id'):
                movies = movies.filter(Movie.genre_id == filters.get('genre_id'))
            if filters.get('director_id'):
                movies = movies.filter(Movie.director_id == filters.get('director_id'))
        return movies.all()

    def get_by_director(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data: dict) -> Movie:
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie: Movie) -> Movie:
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, id: int):
        movie = self.get_by_id(id)
        self.session.delete(movie)
        self.session.commit()
