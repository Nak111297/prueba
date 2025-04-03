import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

def calculate_mean(X):
    if isinstance(X, pd.Series):
        return np.mean(X)
    else:
        raise ValueError("Input must be a pandas Series")

if __name__ == "__main__":
    print(calculate_mean(df['column_name']))