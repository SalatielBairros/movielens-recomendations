from fastapi import APIRouter
from api.invalid_model_exception import InvalidRecommendationModelException
from api.model_name_request import ModelNameRequest

router = APIRouter(prefix="")

@router.get("/")
def get_index():
    return {"message": "Welcome to Movie Recommender API"}
