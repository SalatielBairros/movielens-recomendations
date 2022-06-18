from feature_engineering.feature_engineering_command import FeatureEngineeringCommand
from feature_engineering.ratings_count import RatingsCount
from feature_engineering.ratings_mean_score import RatingsMeanScore
from feature_engineering.movies_id_index import MoviesIdIndex
import pandas as pd

def execute_feature_engineering() -> tuple[pd.DataFrame, pd.DataFrame]:
    return FeatureEngineeringCommand() \
        .add_command(MoviesIdIndex) \
        .add_command(RatingsCount) \
        .add_command(RatingsMeanScore) \
        .execute()