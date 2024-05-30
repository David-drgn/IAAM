import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os


clientes_df = pd.read_csv("C:\\Users\\aluno78\\Downloads\\clientes.csv")


onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(clientes_df[['sexo']])
onehot_encoded_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['sexo']))
clientes_df = pd.concat([clientes_df, onehot_encoded_df], axis=1)
clientes_df = clientes_df.drop(columns=['sexo'])


os.makedirs("C:\\Users\\bruna\\PycharmProjects\\pythonProject\\datasets\\processados\\", exist_ok=True)


clientes_df.to_csv("C:\\Users\\bruna\\PycharmProjects\\pythonProject\\datasets\\processados\\clientes_codificado.csv", index=False)


print(clientes_df)
