import pandas as pd
from environment.constants import EnvironmentVariables
from os import environ as env

class MinRatingsFilter:
    __name__ = "MinRatingsFilter"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies
        self.min_ratings = int(env[EnvironmentVariables.min_ratings])

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        if(self.min_ratings == 0):
            return self.ratings, self.movies
            
        few_ratings = self.movies[self.movies['total_ratings'] < self.min_ratings].index
        self.ratings = self.ratings[~self.ratings['movieId'].isin(few_ratings)]
        self.movies = self.movies[self.movies['total_ratings'] >= self.min_ratings]
        return self.ratings, self.movies