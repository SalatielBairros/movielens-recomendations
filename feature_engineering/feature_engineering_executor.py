from feature_engineering.feature_engineering_command import FeatureEngineeringCommand
from feature_engineering.movie_year import MovieYear
from feature_engineering.ratings_count import RatingsCount
from feature_engineering.ratings_mean_score import RatingsMeanScore
from feature_engineering.movies_id_index import MoviesIdIndex
from feature_engineering.timestamp_transformation import TimestampTransformation
from feature_engineering.user_genres import UserGenres
from feature_engineering.users_distances import UsersDistances
import pandas as pd

def execute_feature_engineering() -> tuple[pd.DataFrame, pd.DataFrame]:
    return FeatureEngineeringCommand() \
        .add_command(MoviesIdIndex) \
        .add_command(RatingsCount) \
        .add_command(RatingsMeanScore) \
        .add_command(MovieYear) \
        .add_command(TimestampTransformation) \
        .add_command(UserGenres) \
        .add_command(UsersDistances) \
        .execute()