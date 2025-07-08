from .schemas import InputData, PredictionResult
import joblib
import numpy as np
import os

# Caminho para o modelo
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")
model = joblib.load(model_path)

def predict_score(data: InputData) -> PredictionResult:
    # Organiza os dados de entrada em array 2D
    input_array = np.array([[data.renda_mensal, data.idade, data.tempo_empresa, int(data.possui_dividas)]])
    
    # Calcula a probabilidade da classe 1 (inadimplente)
    score = float(model.predict_proba(input_array)[0][1])

    # Define risco com base na probabilidade
    risco = "alto" if score >= 0.5 else "baixo"
    explicacao = f"Probabilidade de inadimplência estimada: {score:.2%}"

    return PredictionResult(score=score, risco=risco, explicacao=explicacao)
