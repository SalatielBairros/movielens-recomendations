import pandas as pd
from utils.memo_cache import memo

class LocalStorageRepository:
    def __init__(self, local_storage_path = './data', type = 'small'):
        self.files_path = f'{local_storage_path}/{type}/'
        
    @memo
    def get_ratings(self):
        return pd.read_csv(f'{self.files_path}ratings.csv')
