from repository.data_repository import DataRepository

class BestRatingRecommendation:
    def __init__(self):
        self.data_repository = DataRepository()

    def get_recommendations(self, user_id, size = 5):
        # Loading the datasets
        df_movies = self.data_repository.get_not_watched_movies(user_id)

        # Get the most popular movies
        return df_movies.sort_values(by='mean_score', ascending=False).head(size)