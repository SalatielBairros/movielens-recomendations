from os import environ as env
from environment.constants import EnvironmentVariables, DataRepositoryType
from repository.local_storage_repository import LocalStorageRepository
from utils.memo_cache import memo
import pandas as pd

class DataRepository:
    def __init__(self):
        pass

    def __get_repository__(self):
        if(env[EnvironmentVariables.data_repository_type] == DataRepositoryType.local_storage):
            return LocalStorageRepository()
        raise Exception(f'Unknown data repository type: {env[EnvironmentVariables.data_repository_type]}')

    def get_original_ratings(self) -> pd.DataFrame:
        return self.__get_repository__().get_original_ratings()

    def get_original_movies(self) -> pd.DataFrame:
        return self.__get_repository__().get_original_movies()
    
    def save_ratings(self, ratings):
        self.__get_repository__().save_ratings(ratings)

    def save_movies(self, movies):
        self.__get_repository__().save_movies(movies)

    def save_users_distanes(self, distances):
        self.__get_repository__().save_users_distanes(distances)

    def save_user_genres(self, user_genres: pd.DataFrame):
        self.__get_repository__().save_user_genres(user_genres)

    def get_user_genres(self, user_id: int) -> pd.DataFrame:
        return self.__get_repository__().get_user_genres(user_id)

    def get_processed_ratings(self) -> pd.DataFrame:
        return self.__get_repository__().get_processed_ratings()

    def get_processed_movies(self) -> pd.DataFrame:
        return self.__get_repository__().get_processed_movies()

    @memo
    def get_watched_movies(self, user_id) -> pd.DataFrame:
        ratings = self.__get_repository__().get_processed_ratings()
        return ratings[ratings['userId'] == user_id]

    @memo
    def get_not_watched_movies(self, user_id) -> pd.DataFrame:
        watched_movies = self.get_watched_movies(user_id)['movieId'].unique()
        movies = self.get_processed_movies()
        return movies[~movies['movieId'].isin(watched_movies)]

    def has_distance_file(self):
        return self.__get_repository__().has_distance_file()

    def has_genres_file(self):
        return self.__get_repository__().has_genres_file()
    
    def get_not_watched_by_genders(self, user_id: int, genders: list[str]) -> pd.DataFrame:
        not_watched = self.get_not_watched_movies(user_id)
        not_watched['to_recommend'] = not_watched['genres'].apply(lambda g: len([gen for gen in genders if gen in g]) > 0)
        return not_watched[not_watched['to_recommend'] == True].drop(columns=['to_recommend'])

    def get_user_distances(self, user_id: int) -> pd.DataFrame:
        return self.__get_repository__().get_user_distances(user_id)

    def get_ratings_by_users(self, user_ids: list[int]) -> pd.DataFrame:
        ratings = self.get_processed_ratings()
        return ratings[ratings['userId'].isin(user_ids)]

    def get_movies_by_ids(self, movie_ids: list[int]) -> pd.DataFrame:
        movies = self.get_processed_movies()
        return movies[movies['movieId'].isin(movie_ids)]