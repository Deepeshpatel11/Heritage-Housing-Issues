import pandas as pd
import numpy as np

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values: median for numeric, mode for categorical."""
    cleaned = df.copy()
    for col in cleaned.columns:
        if cleaned[col].isnull().sum() > 0:
            if cleaned[col].dtype in ['int64','float64']:
                cleaned[col].fillna(cleaned[col].median(), inplace=True)
            else:
                cleaned[col].fillna(cleaned[col].mode()[0], inplace=True)
    return cleaned

def create_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create new features like TotalSF, HouseAge, RemodelAge."""
    engineered = df.copy()
    
    if {'1stFlrSF','2ndFlrSF','TotalBsmtSF'}.issubset(engineered.columns):
        engineered['TotalSF'] = engineered['1stFlrSF'] + engineered['2ndFlrSF'] + engineered['TotalBsmtSF']
    if 'YearBuilt' in engineered.columns:
        engineered['HouseAge'] = 2025 - engineered['YearBuilt']
    if 'YearRemodAdd' in engineered.columns:
        engineered['RemodelAge'] = 2025 - engineered['YearRemodAdd']
    
    return engineered

def save_processed_data(df: pd.DataFrame, path: str):
    """Save dataframe to CSV."""
    df.to_csv(path, index=False)
    print(f"Data saved to {path}")