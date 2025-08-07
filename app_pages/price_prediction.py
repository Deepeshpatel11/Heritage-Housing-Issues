import pandas as pd
import streamlit as st
import joblib


def app():
    st.title("💰 Price Prediction")

    # Load trained XGBoost model
    model = joblib.load(
        'models/house_price_model_xgb.pkl'
    )

    # Load inherited house predictions
    inherited_preds = pd.read_csv(
        'data/predictions/inherited_houses_predictions.csv'
    )

    st.subheader("Predicted Prices for Inherited Houses")
    st.dataframe(inherited_preds)

    total_value = inherited_preds['Predicted_SalePrice'].sum()
    st.success(
        f"Total Expected Sale Value: ${total_value:,.2f}"
    )

    # Interactive Prediction
    st.subheader("Interactive Prediction for a New House")

    OverallQual = st.slider("Overall Quality (1-10)", 1, 10, 5)
    GrLivArea = st.number_input(
        "Above Ground Living Area (sqft)", 500, 5000, 1500)
    GarageArea = st.number_input("Garage Area (sqft)", 0, 1500, 400)
    TotalBsmtSF = st.number_input("Total Basement Area (sqft)", 0, 3000, 800)
    FirstFlrSF = st.number_input("1st Floor Area (sqft)", 500, 3000, 1000)

    if st.button("Predict Price"):
        # Load training features
        train_data = pd.read_csv(
            'data/processed/cleaned_housing_data.csv'
        )
        feature_list = (
            train_data
            .select_dtypes(include='number')
            .drop(columns=['SalePrice'])
            .columns.tolist()
        )

        # Create median-filled input for realism
        median_values = train_data[feature_list].median()
        input_data = pd.DataFrame([median_values], columns=feature_list)

        # Fill user inputs
        input_data.loc[0, 'OverallQual'] = OverallQual
        input_data.loc[0, 'GrLivArea'] = GrLivArea
        input_data.loc[0, 'GarageArea'] = GarageArea
        input_data.loc[0, 'TotalBsmtSF'] = TotalBsmtSF
        input_data.loc[0, '1stFlrSF'] = FirstFlrSF

        prediction = model.predict(input_data)[0]
        st.success(f"Estimated Sale Price: ${prediction:,.2f}")
