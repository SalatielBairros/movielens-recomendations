from repository.data_repository import DataRepository
from environment.constants import EnvironmentVariables
from os import environ as env

class MostPopularRecommendation:
    def __init__(self):
        self.data_repository = DataRepository()
        self.min_ratings = int(env[EnvironmentVariables.min_ratings])

    def get_recommendations(self, user_id, size = 5):
        # Loading the datasets
        df_movies = self.data_repository.get_not_watched_movies(user_id)

        # Get the most popular movies
        return df_movies.query(f'total_ratings >= {self.min_ratings}').sort_values(by='total_ratings', ascending=False).head(size)