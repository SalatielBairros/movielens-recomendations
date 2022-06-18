import pandas as pd

class RatingsMeanScore:
    __name__ = "RatingsMeanScore"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.movies['mean_score'] =  self.ratings.groupby(by='movieId')['rating'].mean()
        return self.ratings, self.movies
