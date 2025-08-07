import streamlit as st


def app():
    st.title("🔍 Hypothesis Validation")

    st.markdown("""
    ## Project Hypothesis

    > *"Larger houses with better overall quality and garage space
    tend to sell for higher prices."*

    This hypothesis was formed based on domain knowledge and common
    real estate trends. It was tested using both Exploratory Data
    Analysis (EDA) and feature importance from the machine learning
    models.

    ## Validation Summary

    The hypothesis is supported by both statistical correlations and
    the predictive power of features in our final model
    (XGBoost Regressor).

    ### Top Predictive Features Identified

    **1. `OverallQual` (Overall Quality Rating)**
    - Strongest positive correlation with SalePrice.
    - Higher-quality construction and finishes drive buyer interest.
    - Most important variable in all models.

    **2. `GrLivArea` (Above Ground Living Area)**
    - Livable square footage (excluding basement).
    - Strong correlation with SalePrice.
    - Shows clear linear relationship with price.

    **3. `GarageArea` (Garage Size in Square Feet)**
    - Indicates garage size, a desirable feature.
    - Larger garages linked to higher home values.
    - More informative than GarageCars due to continuous scale.

    **4. `TotalBsmtSF` (Total Basement Square Footage)**
    - Basements add value, especially when finished.
    - Even unfinished space correlates with price.
    - Consistent contributor to predictive performance.

    **5. `1stFlrSF` (First Floor Square Footage)**
    - Describes main-level living space.
    - More desirable than upper floors or basements.
    - Adds layout detail beyond GrLivArea alone.

    ## Supporting Evidence

    - **Pearson Correlation Analysis**: Strong positive coefficients
      for all top features.
    - **Feature Importance**: XGBoost confirmed these as most
      influential.
    - **EDA Visuals**: Scatter and box plots supported the trends.
    - **Residual Analysis**: No clear bias in model predictions.

    ## Conclusion

    The hypothesis is strongly supported. Larger houses with
    better quality construction and usable space (e.g. garages and
    basements) consistently predict higher sale prices in Ames, Iowa.

    These features were verified through EDA, statistical testing,
    and model training.
    """)
