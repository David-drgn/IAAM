import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
df = pd.read_csv("./datasets/funcionarios.csv")
# Instanciando o MinMaxScaler
scaler = MinMaxScaler()
# Escolhendo as colunas para normalizar
columns_to_scale = ["idade", "salario", "peso", "altura" ]

# Aplicando o MinMaxScaler
df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
# Salvando o processamento para um novo arquivo
os.makedirs("datasets/processados", exist_ok=True)
df.to_csv("datasets/processados/funcionarios_normalizado.csv", index=False)
print(df)
