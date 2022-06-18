from repository.data_repository import DataRepository
from environment.constants import EnvironmentVariables
from os import environ as env

class UserGenresBasedRecommendation:
    def __init__(self):
        self.data_repository = DataRepository()
        self.genders_to_recommend = 2
        self.min_ratings = int(env[EnvironmentVariables.min_ratings])

    def get_recommendations(self, user_id, size = 5):
        # Loading the datasets
        df_user_genres = self.data_repository.get_user_genres(user_id)
        if(len(df_user_genres) == 0):
            return None
        
        user_genders = df_user_genres.sort_values(by='total_ratings', ascending=False).head(self.genders_to_recommend)['genre'].tolist()
        return self.data_repository.get_not_watched_by_genders(user_id, user_genders).query(f'total_ratings >= {self.min_ratings}').sort_values(by='mean_score', ascending=False).head(size)        