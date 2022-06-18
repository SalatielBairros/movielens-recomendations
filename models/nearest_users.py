from repository.data_repository import DataRepository

class NearestUsersRecommendation:
    def __init__(self):
        self.data_repository = DataRepository()        

    def get_recommendations(self, user_id, size = 5):
        # Loading the datasets
        df_user_genres = self.data_repository.get_user_genres(user_id)
        if(len(df_user_genres) == 0):
            return None
        
        user_genders = df_user_genres.sort_values(by='total_ratings', ascending=False).head(self.genders_to_recommend)['genre'].tolist()
        return self.data_repository.get_not_watched_by_genders(user_id, user_genders).sort_values(by='mean_score', ascending=False).head(size)        