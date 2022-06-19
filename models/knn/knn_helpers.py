from repository.data_repository import DataRepository
import numpy as np

def calculate_user_distance(user_id_1: int, user_id_2: int):
    """
    Calculates the distance between two users.
    """
    repository = DataRepository()
    wu1 = repository.get_watched_movies(user_id_1)[['movieId', 'rating']].set_index('movieId')
    wu2 = repository.get_watched_movies(user_id_2)[['movieId', 'rating']].set_index('movieId')
    diff = wu1.join(wu2, lsuffix='_1', rsuffix='_2').dropna()
    if(len(diff) == 0):
        return np.inf
    return np.linalg.norm(diff['rating_1'] - diff['rating_2'])

def get_nearests(user_id: int, k: int):
    """
    Returns the k nearest users to the user_id.
    """
    repository = DataRepository()
    distances = repository.get_user_distances(user_id)    
    distances = distances.sort_values(by='distance')
    return distances['userId_2'].head(k)