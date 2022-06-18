from repository.data_repository import DataRepository


def calculate_user_distance(user_id_1: int, user_id_2: int):
    """
    Calculates the distance between two users.
    """
    repository = DataRepository()
    wu1 = repository.get_not_watched_movies(user_id_1)[['movieId', 'rating']].set_index('movieId')
    wu2 = repository.get_not_watched_movies(user_id_2)[['movieId', 'rating']].set_index('movieId')
    wfull = wu1.join(wu2, lsuffix='_1', rsuffix='_2').dropna()