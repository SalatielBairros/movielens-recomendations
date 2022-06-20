from environment.env_configuration import prepare_environment
from models.most_popular import MostPopularRecommendation
from models.best_rating import BestRatingRecommendation
from models.user_genres_based import UserGenresBasedRecommendation
from models.knn.knn_recomendations import KnnRecommendations
import logging
from feature_engineering.feature_engineering_executor import execute_feature_engineering

prepare_environment()
_ , _ = execute_feature_engineering()

# most_popular_recommendations = MostPopularRecommendation().get_recommendations(1, size=10)
# logging.info(f'Most Popular: \n {most_popular_recommendations}')

# most_popular_recommendations = BestRatingRecommendation().get_recommendations(1, size=10)
# logging.info(f'Best rated: \n {most_popular_recommendations}')

# most_popular_recommendations = UserGenresBasedRecommendation().get_recommendations(1, size=10)
# logging.info(f'User genres based: \n {most_popular_recommendations}')

nearest_recommendations = KnnRecommendations().get_recommendations(1, size=10)
logging.info(f'Nearest users based: \n {nearest_recommendations}')