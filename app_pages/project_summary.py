import streamlit as st


def app():
    st.title("📄 Project Summary")
    st.markdown("""
    ### Heritage Housing Issues – Predictive Analytics

    **Business Goal**:
    - Identify features most correlated with house sale prices.
    - Predict the total value of **4 inherited houses** in Ames, Iowa.

    **Workflow (CRISP-DM)**:
    1. **Data Collection** from Kaggle
    2. **Data Cleaning & Feature Engineering**:
       - Handle missing values & outliers
       - Transform features for better predictive power
    3. **Exploratory Data Analysis (EDA)**:
       - Correlation, Distribution, and Outlier Analysis
    4. **Modeling**:
       - Baseline: Random Forest
       - Tuned: XGBoost (Best R² ~0.90, RMSE ~$27.8K)
    5. **Prediction**:
       - Individual and total predicted price for inherited houses
    6. **Dashboard**:
       - Visual insights and interactive predictions

    **Key Deliverable**:
    - Data-driven pricing insights
    and a **Streamlit dashboard** for real-time prediction.
    """)
