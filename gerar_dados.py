import pandas as pd
import numpy as np

# Semente para reprodutibilidade
np.random.seed(42)

# Número de registros
n = 1000

# Criar colunas simuladas
data = pd.DataFrame({
    'renda_mensal': np.random.normal(4000, 1500, n).clip(800),  # média 4000, mínimo 800
    'idade': np.random.randint(18, 65, n),
    'tempo_empresa': np.random.exponential(3, n).clip(0, 30),   # de 0 a 30 anos
    'possui_dividas': np.random.choice([0, 1], size=n, p=[0.7, 0.3])
})

# Criar alvo (inadimplente)
data['inadimplente'] = (
    (data['renda_mensal'] < 3000) &
    (data['tempo_empresa'] < 1) &
    (data['possui_dividas'] == 1)
).astype(int)

# Salvar CSV
data.to_csv("dados_credito.csv", index=False)

print("✅ Base de dados gerada com sucesso: dados_credito.csv")