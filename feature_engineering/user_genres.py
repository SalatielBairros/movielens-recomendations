import pandas as pd
from repository.data_repository import DataRepository

class UserGenres:
    __name__ = "UserGenres"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies
        self.repository = DataRepository()

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        user_genres = []
        for _, row in self.ratings.iterrows():
            genres = self.movies.at[row['movieId'], 'genres']
            for genre in genres.split('|'):
                user_genres.append({
                    'userId': row['userId'],
                    'genre': genre,
                    'rating': row['rating'],
                    'date': row['date']
                })
        user_genres = pd.DataFrame(user_genres)
        grouped_user_genres = user_genres.groupby(by=['userId', 'genre'])
        user_genres = pd.DataFrame({ 
            'rating_mean': grouped_user_genres['rating'].mean(),
            'total_ratings': grouped_user_genres['rating'].count(),
            'last_time': grouped_user_genres['date'].max()
        }).reset_index()

        self.repository.save_user_genres(user_genres)

        return self.ratings, self.movies
