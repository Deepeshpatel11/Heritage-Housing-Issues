import streamlit as st
from app_pages import (
    project_summary,
    correlation_insights,
    price_prediction,
    hypothesis_validation,
    model_performance
)

# Streamlit Config
st.set_page_config(page_title="Heritage Housing Dashboard", layout="wide")

st.sidebar.title("🏡 Heritage Housing Dashboard")
page = st.sidebar.radio(
    "Navigate",
    (
        "Project Summary",
        "Correlation Insights",
        "Price Prediction",
        "Hypothesis Validation",
        "Model Performance"
    )
)

if page == "Project Summary":
    project_summary.app()
elif page == "Correlation Insights":
    correlation_insights.app()
elif page == "Price Prediction":
    price_prediction.app()
elif page == "Hypothesis Validation":
    hypothesis_validation.app()
elif page == "Model Performance":
    model_performance.app()
