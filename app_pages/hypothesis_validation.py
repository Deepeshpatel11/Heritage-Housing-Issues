import streamlit as st

def app():
    st.title("🔍 Hypothesis Validation")

    st.markdown("""
    **Hypothesis**:
    > Larger houses with better overall quality and garage space sell for higher prices.
    
    **Validation**:
    - **Feature importance analysis** shows top features:
      1. OverallQual
      2. GrLivArea
      3. GarageArea
      4. TotalBsmtSF
      5. 1stFlrSF
    - **Residual analysis** confirms predictions are unbiased with no clear pattern.
    
    ✅ Hypothesis supported by EDA and model results.
    """)
