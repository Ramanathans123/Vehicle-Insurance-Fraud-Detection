import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(data_path, iterations):
    df = pd.read_csv(data_path)

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    df['FraudFound'] = df['FraudFound'].astype(int)

    return {
        "Iteration": list(range(1, iterations + 1)),
        "N-XAI": [],
        "LSTM": []
    }
