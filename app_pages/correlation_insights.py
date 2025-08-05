import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title("📊 Correlation Insights")

    df = pd.read_csv('data/processed/cleaned_housing_data.csv')
    numeric_df = df.select_dtypes(include='number')

    # Compute correlations with SalePrice
    corr = numeric_df.corr()['SalePrice'].sort_values(ascending=False)

    st.subheader("Top Correlated Features with SalePrice")
    st.dataframe(corr.head(10))

    # Heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(numeric_df.corr(), cmap='coolwarm', center=0)
    plt.title("Feature Correlation Heatmap")
    st.pyplot(fig)
