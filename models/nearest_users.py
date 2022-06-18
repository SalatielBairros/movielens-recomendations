from repository.data_repository import DataRepository

class NearestUsersRecommendation:
    def __init__(self):
        self.data_repository = DataRepository()        

    def get_recommendations(self, user_id, size = 5):
        watched_movies_ratings = self.data_repository.get_watched_movies(user_id)
        watched_movies_ratings[['movieId', 'rating']].set_index('movieId')