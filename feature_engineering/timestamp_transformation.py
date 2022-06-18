import pandas as pd

class TimestampTransformation:
    __name__ = "TimestampTransformation"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        self.ratings['date'] = pd.to_datetime(self.ratings['timestamp'], unit='s')
        self.ratings.drop(columns=['timestamp'], inplace=True)        
        return self.ratings, self.movies
