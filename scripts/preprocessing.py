import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def preprocess_data(df):
    # 1. Drop any missing values (if any)
    df = df.dropna()

    # 2. One-hot encode the 'State' column
    state_encoded = pd.get_dummies(df['State'], drop_first=True)
    df = pd.concat([df.drop('State', axis=1), state_encoded], axis=1)

    return df
