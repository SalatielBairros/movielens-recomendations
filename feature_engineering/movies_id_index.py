import pandas as pd

class MoviesIdIndex:
    __name__ = "MoviesIdIndex"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.movies.set_index('movieId', inplace=True)
        return self.ratings, self.movies