from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.invalid_model_exception import InvalidRecommendationModelException
from environment.env_configuration import prepare_environment
from api.recommendation_controller import router as recommendation_router

prepare_environment()
app = FastAPI()
app.include_router(recommendation_router)

@app.exception_handler(InvalidRecommendationModelException)
async def invalid_recommendation_model_exception_handler(request, exc):
    return JSONResponse(status_code=400, content={"message": exc.full_message})