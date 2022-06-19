import logging
import pandas as pd
import numpy as np
from repository.data_repository import DataRepository
from models.knn.knn_helpers import calculate_user_distance
import os

class UsersDistances:
    __name__ = "UsersDistances"

    def __init__(self, ratings: pd.DataFrame, movies: pd.DataFrame):
        self.ratings = ratings
        self.movies = movies
        self.repository = DataRepository()

    def should_execute(self) -> bool:
        return not self.repository.has_distance_file()

    def execute(self) -> tuple[pd.DataFrame, pd.DataFrame]:
        user_distances = []
        users = np.sort(self.ratings['userId'].unique())
        size = len(users)
        for user_id_1 in users:            
            logging.info(f"Processing user {user_id_1}/{size}")
            for user_id_2 in users:
                if user_id_1 != user_id_2 and user_id_2 > user_id_1:
                    distance = calculate_user_distance(user_id_1, user_id_2)
                    if(distance < np.inf):
                        user_distances.append({
                            'userId_1': user_id_1,
                            'userId_2': user_id_2,
                            'distance': distance
                        })

        user_distances = pd.DataFrame(user_distances)
        self.repository.save_users_distanes(user_distances)
        return self.ratings, self.movies
