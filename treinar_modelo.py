import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
import os

# Carregar os dados gerados
df = pd.read_csv("dados_credito.csv")

# Separar em X e y
X = df.drop("inadimplente", axis=1)
y = df["inadimplente"]

# Dividir entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Treinar modelo com XGBoost
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Criar pasta models (dentro de backend) se não existir
model_dir = os.path.join("backend", "models")
os.makedirs(model_dir, exist_ok=True)

# Salvar modelo treinado na pasta correta
joblib.dump(model, os.path.join(model_dir, "model.pkl"))

print("✅ Modelo treinado e salvo com sucesso em: backend/models/model.pkl")
