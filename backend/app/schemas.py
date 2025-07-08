from pydantic import BaseModel

class InputData(BaseModel):
    renda_mensal: float
    idade: int
    tempo_empresa: float
    possui_dividas: bool

class PredictionResult(BaseModel):
    score: float
    risco: str
    explicacao: str