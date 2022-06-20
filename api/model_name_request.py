from enum import Enum

class ModelNameRequest(str, Enum):
    most_popular = "most-popular"
    best_rated = "best-rated"
    genre_based = "genre-based"
    nearest_users = "nearest-users"