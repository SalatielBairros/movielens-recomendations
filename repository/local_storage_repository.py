import pandas as pd
from utils.memo_cache import memo

class LocalStorageRepository:
    def __init__(self, local_storage_path = './data', type = 'small') -> None:
        self.files_path = f'{local_storage_path}/{type}'

    @memo
    def get_original_ratings(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/original/ratings.csv')

    @memo
    def get_original_movies(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/original/movies.csv')

    def save_ratings(self, ratings):
        ratings.to_csv(f'{self.files_path}/processed/ratings.csv', index=False)

    def save_movies(self, movies: pd.DataFrame):
        movies.reset_index(inplace=True)
        movies.to_csv(f'{self.files_path}/processed/movies.csv', index=False)

    def save_user_genres(self, user_genres: pd.DataFrame):
        user_genres.reset_index(inplace=True)
        user_genres.to_csv(f'{self.files_path}/processed/user_genres.csv', index=False)

    @memo
    def get_user_genres(self, user_id: int) -> pd.DataFrame:
        user_genres = pd.read_csv(f'{self.files_path}/processed/user_genres.csv')
        return user_genres.query(f'userId == {user_id}')

    @memo
    def get_processed_ratings(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/processed/ratings.csv')

    @memo
    def get_processed_movies(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/processed/movies.csv')