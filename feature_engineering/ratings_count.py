import pandas as pd

class RatingsCount:
    __name__ = "RatingsCount"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.movies['total_ratings'] =  self.ratings['movieId'].value_counts()
        self.movies['total_ratings'] = self.movies['total_ratings'].fillna(0.0).astype(int)
        return self.ratings, self.movies
