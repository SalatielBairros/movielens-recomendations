from environment.env_configuration import prepare_environment
from models.most_popular import MostPopularRecommendation
import logging
from feature_engineering.feature_engineering_executor import execute_feature_engineering

prepare_environment()
_ , _ = execute_feature_engineering()
most_popular_recommendations = MostPopularRecommendation().get_recommendations(1, size=10)
logging.info(f'Most Popular Recommendations: \n {most_popular_recommendations}')