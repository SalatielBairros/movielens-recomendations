from repository.data_repository import DataRepository
from environment.constants import EnvironmentVariables
from models.knn.knn_helpers import get_nearests
from os import environ as env

class KnnRecommendations:
    def __init__(self):
        self.data_repository = DataRepository()
        self.min_ratings = int(env[EnvironmentVariables.min_ratings])

    def get_recommendations(self, user_id, size = 5):
        nearests = get_nearests(user_id, size)
        ratings = self.data_repository.get_ratings_by_users(nearests)
        watched_movies_ids = self.data_repository.get_watched_movies(user_id)['movieId'].unique()
        best_movies_mean = ratings[~ratings['movieId'].isin(watched_movies_ids)] \
            .groupby('movieId') \
            .mean()['rating']
        movies = self.data_repository.get_processed_movies()
        movies['nearest_score'] = best_movies_mean
        return movies.dropna().query(f'total_ratings > {self.min_ratings}').sort_values(by='nearest_score', ascending=False)