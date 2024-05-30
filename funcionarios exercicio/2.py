import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder

# Read the CSV file
df = pd.read_csv("datasets/restaurante.csv")

# Encode the categorical variable 'tipo' using one-hot encoding
onehot_encoder = OneHotEncoder(sparse_output=False)
onehot_encoded = onehot_encoder.fit_transform(df[['tipo']])
onehot_encoded_df = pd.DataFrame(onehot_encoded, columns=onehot_encoder.get_feature_names_out(['tipo']))
df = pd.concat([df, onehot_encoded_df], axis=1)

# Remove the original 'tipo' column after encoding
df = df.drop(columns=['tipo'])

# Save the processed data to a new file
os.makedirs("datasets/processados", exist_ok=True)
df.to_csv("datasets/processados/restaurante_codificado.csv", index=False)

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Print the entire DataFrame
print(df.to_string(index=False))