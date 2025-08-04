import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a regression model using R² and RMSE.
    Returns (r2, rmse).
    """
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    return r2, rmse, y_pred

def print_evaluation(model_name, r2, rmse):
    print(f"{model_name} R²: {r2:.4f}")
    print(f"{model_name} RMSE: {rmse:.2f}")

def plot_residuals(y_true, y_pred, model_name):
    """
    Plot residuals to check model errors visually.
    """
    residuals = y_true - y_pred
    sns.scatterplot(x=y_true, y=residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.title(f"Residual Plot - {model_name}")
    plt.xlabel("Actual SalePrice")
    plt.ylabel("Residuals")
    plt.show()

def plot_feature_importance(model, feature_names, top_n=10, model_name='Model'):
    """
    Plot top N feature importances for tree-based models.
    """
    if hasattr(model, 'feature_importances_'):
        importances = pd.Series(model.feature_importances_, index=feature_names)
        importances.nlargest(top_n).sort_values().plot(kind='barh')
        plt.title(f"Top {top_n} Feature Importances - {model_name}")
        plt.show()
    else:
        print(f"{model_name} does not support feature_importances_.")
