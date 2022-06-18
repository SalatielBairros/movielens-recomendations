import pandas as pd
from repository.data_repository import DataRepository

class BasicRecommendationModel:
    def __init__(self):
        self.data_repository = DataRepository()

    def get_recommendations(self, user_id):
        df_ratings = self.data_repository.get_ratings()
        print(df_ratings.head())