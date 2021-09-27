from pydantic import BaseModel
from typing import List


class MachineLearningReponse(BaseModel):
    prediction: List[float]


class HealthResponse(BaseModel):
    status: bool
