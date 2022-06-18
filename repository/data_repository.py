from os import environ as env
from environment.constants import EnvironmentVariables, DataRepositoryType
from repository.local_storage_repository import LocalStorageRepository
from utils.memo_cache import memo

class DataRepository:
    def __init__(self):
        pass

    def __get_repository__(self):
        if(env[EnvironmentVariables.data_repository_type] == DataRepositoryType.local_storage):
            return LocalStorageRepository()
        raise Exception(f'Unknown data repository type: {env[EnvironmentVariables.data_repository_type]}')

    def get_original_ratings(self):
        return self.__get_repository__().get_original_ratings()

    def get_original_movies(self):
        return self.__get_repository__().get_original_movies()
    
    def save_ratings(self, ratings):
        self.__get_repository__().save_ratings(ratings)

    def save_movies(self, movies):
        self.__get_repository__().save_movies(movies)

    def get_processed_ratings(self):
        return self.__get_repository__().get_processed_ratings()

    def get_processed_movies(self):
        return self.__get_repository__().get_processed_movies()

    @memo
    def get_watched_movies(self, user_id):
        ratings = self.__get_repository__().get_original_ratings()
        return ratings[ratings['userId'] == user_id]['movieId'].unique()

    @memo
    def get_not_watched_movies(self, user_id):
        watched_movies = self.get_watched_movies(user_id)
        movies = self.get_processed_movies()
        return movies[~movies['movieId'].isin(watched_movies)]