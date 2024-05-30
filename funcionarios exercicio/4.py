import pandas as pd
import os

pessoas_df = pd.read_csv("C:\\Users\\aluno78\\Downloads\\pessoas.csv")

bins = [0, 12, 18, 35, 60, 100]
labels = ['Criança', 'Adolescente', 'Jovem', 'Adulto', 'Idoso']

pessoas_df['faixa_etaria'] = pd.cut(pessoas_df['idade'], bins=bins, labels=labels, right=False)


os.makedirs("C:\\Users\\bruna\\PycharmProjects\\pythonProject\\datasets\\processados\\", exist_ok=True)


pessoas_df.to_csv("C:\\Users\\bruna\\PycharmProjects\\pythonProject\\datasets\\processados\\pessoas_discretizado.csv", index=False)


print(pessoas_df)
