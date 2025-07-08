from fastapi import APIRouter
from .schemas import InputData, PredictionResult
from .predict import predict_score

router = APIRouter()

@router.post("/predict", response_model=PredictionResult)
def predict(data: InputData):
    result = predict_score(data)
    return result