import pandas as pd

def select_numeric_features(df: pd.DataFrame, target='SalePrice'):
    """
    Select numeric features for model training, excluding the target.
    """
    return df.drop(columns=[target]).select_dtypes(include=['int64', 'float64'])
