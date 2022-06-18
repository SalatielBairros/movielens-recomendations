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

    def save_movies(self, movies):
        movies.to_csv(f'{self.files_path}/processed/movies.csv', index=False)

    @memo
    def get_processed_ratings(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/processed/ratings.csv')

    @memo
    def get_processed_movies(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.files_path}/processed/movies.csv')