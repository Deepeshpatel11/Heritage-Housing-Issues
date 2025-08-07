import streamlit as st

def app():
    st.title("🔍 Hypothesis Validation")

    st.markdown("""
    ## Project Hypothesis

    > *"Larger houses with better overall quality and garage space tend to sell for higher prices."*

    This hypothesis was formed based on domain knowledge and common real estate trends. It was tested using both Exploratory Data Analysis (EDA) and feature importance from the machine learning models.

    ## Validation Summary

    The hypothesis is supported by both statistical correlations and the predictive power of features in our final model (XGBoost Regressor).

    ### 🔑 Top Predictive Features Identified:
    
    **1. `OverallQual` (Overall Quality Rating)**  
    - This feature had the **strongest positive correlation** with SalePrice.
    - Higher-quality construction and finishes significantly drive buyer willingness to pay.
    - This was consistently the most important variable in all models.

    **2. `GrLivArea` (Above Ground Living Area)**  
    - Represents the livable square footage (excluding basement).
    - Strongly correlated with SalePrice as buyers pay more for usable living space.
    - Visual analysis showed a clear linear relationship with price.

    **3. `GarageArea` (Garage Size in Square Feet)**  
    - Reflects the size of the garage, an important amenity.
    - Larger garages were associated with higher home values, particularly in newer or higher-end homes.
    - Chosen over GarageCars for its continuous nature and contribution to total usable space.

    **4. `TotalBsmtSF` (Total Basement Square Footage)**  
    - Basements often add value, particularly if finished or partially usable.
    - Even unfinished basements correlate with higher sale prices due to expansion potential.
    - Included for its linear correlation and consistency across the dataset.

    **5. `1stFlrSF` (First Floor Square Footage)**  
    - Main-level space is often more desirable than upper floors or basements.
    - This feature overlaps with GrLivArea but adds specificity about layout distribution.

    ## Supporting Evidence

    - **Pearson Correlation Analysis** revealed all of these features had strong positive correlation coefficients with SalePrice, especially `OverallQual` and `GrLivArea`.
    - **Feature Importance from XGBoost** confirmed these were the top 5 contributors to model performance.
    - **Boxplots and scatterplots** visually demonstrated these variables’ relationship with increasing sale price.
    - **Residual Analysis** indicated the model predictions were not biased toward any particular range of SalePrice, reinforcing the validity of the selected features.

    ## Conclusion

    ✅ The hypothesis is strongly supported.  
    Larger houses, higher quality construction, and additional features like garage and basement space are reliable indicators of higher sale prices in Ames, Iowa.

    These variables were not only consistent across visual and statistical exploration but were also validated through rigorous machine learning performance.
    """)
