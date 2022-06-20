from fastapi import APIRouter
from api.invalid_model_exception import InvalidRecommendationModelException
from api.model_name_request import ModelNameRequest

router = APIRouter(prefix="/recommendations")

@router.get("/{user_id}/{model_name}")
def get_recommendations(user_id: int, model_name: ModelNameRequest, size: int = 5):
    if model_name == ModelNameRequest.most_popular:
        from models.most_popular import MostPopularRecommendation
        return MostPopularRecommendation().get_recommendations(user_id, size).to_dict('records')
    elif model_name == ModelNameRequest.best_rated:
        from models.best_rating import BestRatingRecommendation
        return BestRatingRecommendation().get_recommendations(user_id, size).to_dict('records')
    elif model_name == ModelNameRequest.genre_based:
        from models.user_genres_based import UserGenresBasedRecommendation
        return UserGenresBasedRecommendation().get_recommendations(user_id, size).to_dict('records')
    elif model_name == ModelNameRequest.nearest_users:
        from models.knn.knn_recomendations import KnnRecommendations
        return KnnRecommendations().get_recommendations(user_id, size).to_dict('records')
    raise InvalidRecommendationModelException(detail_message=model_name)

@router.put("/feature-engineering")
def execute_feature_engineering():
    from feature_engineering.feature_engineering_executor import execute_feature_engineering
    return execute_feature_engineering()