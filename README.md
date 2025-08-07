# Heritage Housing Issues – House Price Prediction for Ames, Iowa

This project aims to support a fictional client, Lydia Doe, in estimating the value of four inherited properties located in Ames, Iowa. The project delivers both a detailed analytical study and a predictive Machine Learning application that can estimate house prices based on their features. The solution is deployed as a Streamlit dashboard and available publicly.

---

## How to Use This Repo

1. Fork this repo.

2. In your forked repo, click the green **Code** button.

3. From the *Codespaces* tab, click **Create codespace on main**.

4. Wait for the workspace to initialize.

5. Open a new terminal and run:

   ```bash

   pip install -r requirements.txt

6. From the notebook toolbar, select the kernal:

   Python 3.12.x (from workspace)

7. Confirm your environment is ready with:

    ```bash

    !python --version

## Dataset Content

This project uses publicly available datasets from [Kaggle's House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) competition. The data represents residential property sales in Ames, Iowa, and contains detailed information on various physical attributes of houses sold between 2006 and 2010.

In addition, a small custom dataset (inherited_houses.csv) was introduced for a hypothetical client. This dataset includes 4 inherited houses for which the client wishes to predict sale prices.

The main dataset includes 81 variables, covering a range of attributes:

Key Feature Categories:

* Location & Lot Details: Lot Area, Lot Shape, Land Slope, Neighborhood

* Exterior Features: Roof Style, Exterior Materials, Masonry Veneer

* Basement & Foundation: Basement Condition, Square Footage, Walkout Basement

* Interior Features: Number of Bedrooms, Full/Half Bathrooms, Kitchen Quality, Fireplace Quality

* Garage & Parking: Garage Type, Year Built, Garage Area, Garage Quality

* General Structure: Overall Quality, Year Built, Year Remodeled, House Age

* Sale Data: Sale Price (target variable)

Files Used:

* house_prices_records.csv: Full dataset with 1460 rows and 81 columns

* inherited_houses.csv: 4 rows of client-supplied properties to evaluate

* house_metadata.txt: Descriptions and explanations for each variable

* Processed versions: cleaned_housing_data.csv, cleaned_inherited_houses.csv were created after data wrangling

| Variable        | Description                                      |
|-----------------|--------------------------------------------------|
| `SalePrice`     | Final sale price of the house (target)           |
| `OverallQual`   | Overall material and finish quality              |
| `OverallCond`   | Overall condition rating                         |
| `GrLivArea`     | Above grade (ground) living area (sq ft)         |
| `GarageArea`    | Size of garage in square feet                    |
| `GarageFinish`  | Interior finish of the garage                    |
| `GarageYrBlt`   | Year garage was built                            |
| `TotalBsmtSF`   | Total square feet of basement area               |
| `BsmtFinSF1`    | Type 1 finished square feet in basement          |
| `BsmtFinType1`  | Type 1 finished area rating                      |
| `BsmtUnfSF`     | Unfinished basement square feet                  |
| `BsmtExposure`  | Basement exposure to outdoors                    |
| `1stFlrSF`      | First floor square feet                          |
| `2ndFlrSF`      | Second floor square feet                         |
| `BedroomAbvGr`  | Number of bedrooms above ground                  |
| `KitchenQual`   | Kitchen quality (ordinal)                        |
| `LotArea`       | Lot size in square feet                          |
| `LotFrontage`   | Linear feet of street connected to property      |
| `MasVnrArea`    | Masonry veneer area in square feet               |
| `OpenPorchSF`   | Open porch area in square feet                   |
| `YearBuilt`     | Original construction date                       |
| `YearRemodAdd`  | Remodel date                                     |
| `TotalSF`       | Total square footage (above + basement)          |
| `HouseAge`      | Age of the house (at time of sale)               |
| `RemodelAge`    | Age since last remodel                           |

## Business Requirements

The project was developed for a client who recently inherited four residential properties in Ames, Iowa. The client seeks to maximize the return on these assets and make informed decisions regarding their sale. Two main business objectives were identified:

### Business Requirement 1

* The client wants to understand which house attributes have the most significant impact on sale price. This insight will help prioritize renovation or staging efforts to improve key features that directly affect property value.

### Business Requirement 2

* The client needs a reliable system to accurately predict the sale prices of the four inherited properties and any other similar property in the Ames area. This will support decision-making around pricing, negotiations, and future real estate investments.

To meet these needs, the project delivers:

* Data exploration and visualizations to uncover patterns and correlations in the housing data.

* A machine learning model trained on historical property sales to predict sale prices based on house features.

* An interactive dashboard for visual insights and real-time predictions based on user-provided inputs.

## Hypothesis and How to Validate

This project began with several hypotheses regarding factors that may influence house prices in Ames, Iowa. These hypotheses were tested using correlation analysis, exploratory data analysis (EDA), and model performance during feature selection.

### Hypotheses

1. **Overall Quality and Overall Condition strongly influence Sale Price.**  
   * These are general indicators of the house's physical state and appeal.

2. **Larger living spaces (e.g., Above Ground Living Area and Total Basement Area) lead to higher sale prices.**  
   * Buyers typically pay more for more usable space.

3. **Garage and Lot Features contribute positively to property value.**  
   * The presence and size of garages, lot frontage, and lot area may be associated with higher prices.

4. **Year Built and Year Remodeled are positively correlated with price.**  
   * Newer or recently renovated homes tend to command higher market value.

### Validation Methods

* **Correlation Matrix (Pearson):**  
  Used to measure the linear relationships between numerical features and sale price. This helped identify top predictors.

* **Pairplots & Visualizations:**  
  Visual tools were used to assess the distribution and trends of key features relative to sale price.

* **Feature Importance from Models:**  
  Random Forest and XGBoost models provided feature importance rankings, which confirmed that features like `OverallQual`, `GrLivArea`, and `TotalBsmtSF` were among the most predictive.

* **Model Performance:**  
  The predictive accuracy of trained models further validated which features had strong explanatory power. Strong model R² scores indicated that the selected features effectively captured the variability in sale price.

## 4. Rationale to Map Business Requirements to Data Visualizations and ML Tasks

To effectively address the client's business needs, the project was divided into two distinct analytical and technical components: data exploration (to meet the correlation insight requirement) and machine learning (to meet the prediction requirement).

### Business Requirement 1 → Data Visualizations

**Objective:** Identify which features most significantly impact sale price.

**Approach:**

* Performed **Exploratory Data Analysis (EDA)** to understand data distribution and missing values.
* Applied **correlation analysis** (Pearson correlation and Predictive Power Score) to rank features by relevance.
* Created a series of **visual plots** to clearly communicate patterns:
  * Scatterplots for continuous features vs. SalePrice
  * Boxplots for categorical/ordinal features (e.g., Kitchen Quality)
  * Heatmaps for identifying multicollinearity
* Validated assumptions with model-driven **feature importance rankings**

**Outcome:** A set of top-performing variables was identified, including:

* `OverallQual`, `GrLivArea`, `GarageArea`, `TotalBsmtSF`, `1stFlrSF`, `YearBuilt`, and `KitchenQual`.

These visual insights were presented to the client through a dedicated dashboard page.

### Business Requirement 2 → Machine Learning Model

**Objective:** Predict sale prices for inherited and future properties.

**Approach:**

* Converted the problem into a **supervised regression task**, with `SalePrice` as the target variable.
* Built and compared several models:
  * Linear Regression (baseline)
  * Ridge Regression
  * Random Forest Regressor
  * XGBoost Regressor
* Conducted **feature selection**, **data scaling**, and **hyperparameter tuning** for performance optimization.
* Chose the best model based on:
  * R² Score
  * RMSE
  * Generalization to unseen data

**Outcome:** The **XGBoost Regressor** was selected for deployment due to its strong predictive performance and ability to handle feature interactions effectively.

**Integration:** The final model was integrated into a **Streamlit dashboard**, allowing users to input custom property data and instantly receive predicted prices.

---

## Machine Learning Business Case

### Objective

To deliver a reliable and explainable machine learning model capable of predicting house sale prices in Ames, Iowa. The model should be usable for both inherited houses and any other user-inputted house profiles.

### Type of Machine Learning Task

This is a **supervised regression task**, where the target variable is:

* `SalePrice` – a continuous numeric variable representing the house sale price in USD.

### Model Candidates Evaluated

Four regression models were trained and evaluated using 80/20 train-test data split:

| Model               | RMSE (Test) | R² Score | Notes                                         |
|--------------------|-------------|----------|-----------------------------------------------|
| Linear Regression   | 34,280      | 0.781    | Basic benchmark model                         |
| Ridge Regression    | 33,100      | 0.792    | Slightly better with regularization           |
| Random Forest       | 30,270      | 0.853    | Non-linear model, good performance            |
| XGBoost Regressor   | **27,860**  | **0.889**| Best performer — accurate and robust          |

### Final Model: XGBoost Regressor

XGBoost was selected due to:

* The **lowest RMSE** and **highest R²** on test data
* Ability to **capture non-linear relationships**
* Built-in support for **feature importance analysis**
* Consistent performance on tabular datasets with mixed feature types

### Performance Goals and Results

| Metric            | Requirement | Achieved |
|------------------|-------------|----------|
| R² (Train/Test)   | ≥ 0.75      | ✅ 0.935 / 0.889 |
| RMSE (Test)       | ≤ $30,000   | ✅ $27,860 |
| Overfitting Gap   | ≤ 0.10      | ✅ ~0.05 |

The model meets all defined success criteria, making it suitable for production deployment.

### Model Output

* **Input:** Cleaned and encoded housing features
* **Output:** Predicted `SalePrice` in USD
* **Application:** Predicts prices for inherited properties and any other user-defined house in the dashboard interface

### Risk and Mitigation

* **Risk:** Overfitting on small sample sizes  
  **Mitigation:** Used cross-validation and tested performance on unseen data.
  
* **Risk:** Limited generalizability to other cities  
  **Mitigation:** Clear documentation and communication that the model is valid for **Ames, Iowa** only.

This model is now live within the deployed dashboard and forms the foundation for real-time price predictions.

## 6. Dashboard Design

The dashboard was developed using [Streamlit](https://streamlit.io/) and deployed to [Heroku](https://heritage-housing-issues-app-2516705cc4a8.herokuapp.com/). It provides an intuitive interface for users to explore data insights and predict house sale prices in real time.

The design follows a clear, modular structure with five key pages:

### Page 1: Project Summary

* Provides a brief overview of the project scope and objectives
* Describes the datasets used and outlines the client’s business requirements
* Highlights the structure of the Streamlit dashboard for easy navigation

### Page 2: Correlation Insights

* Displays the top features most strongly correlated with `SalePrice`
* Uses Pearson correlation and Predictive Power Score (PPS)
* Includes visualizations such as:
  * Heatmaps
  * Boxplots
  * Scatterplots
* Provides written summaries to explain insights in plain language

### Page 3: Price Prediction

* Displays the predicted sale prices for the 4 inherited houses
* Calculates and shows the total combined value of the inherited portfolio
* Includes an interactive form for users to input any new house details
  * Dropdowns and sliders are used for categorical and numerical inputs
* Predicts and displays the estimated sale price immediately upon form submission

### Page 4: Hypothesis Validation

* Revisits each original hypothesis from the analysis phase
* Describes how each was tested using data exploration and modeling
* Confirms or refutes each hypothesis based on empirical evidence
* Provides clear reasoning behind the inclusion or exclusion of features in the final model

### Page 5: Model Performance

* Outlines the steps taken to build and evaluate each model
* Includes performance metrics such as:
  * R² scores (train/test)
  * RMSE values
  * Cross-validation scores
* Displays a bar chart showing model comparison
* Highlights the final model selection (XGBoost) and explains why it was chosen
* Shows the most important features based on the model’s internal ranking

The dashboard is user-friendly and provides both technical transparency and business-level insights. It was designed to meet both the analytical and decision-making needs of the client.

---

## 7. Unfixed Bugs

While the application functions as intended and meets all business requirements, a few minor issues remain that could be addressed in future development cycles:

### 1. Input Validation in Prediction Form

* **Issue**: The interactive widgets on the Price Prediction page accept a limited range of input values but lack deeper validation.
* **Impact**: Users may enter extreme or unrealistic values that could lead to misleading predictions.
* **Future Fix**: Implement more robust input constraints and error messaging.

### 2. Limited Categorical Encoding Coverage

* **Issue**: Some less common categories in the original training data may not appear in new user inputs.
* **Impact**: This could lead to missing columns or misalignment in prediction features.
* **Future Fix**: Add safeguards to dynamically align new input data with the training schema (e.g., via column transformers or schema validators).

### 3. Model Update Process

* **Issue**: The current deployed model is static and not updated automatically.
* **Impact**: As new data becomes available or market trends shift, the model may become less accurate.
* **Future Fix**: Introduce a pipeline for retraining the model periodically and redeploying automatically via CI/CD.

### 4. Feature Engineering Pipeline Not Exposed in UI

* **Issue**: The preprocessing steps (e.g., handling missing values, outlier treatment) are not explicitly shown in the dashboard.
* **Impact**: Limits transparency for advanced users or stakeholders.
* **Future Fix**: Add a technical tab or expandable section that outlines preprocessing logic used in the pipeline.

Despite these known limitations, none of them affect the core functionality of the project or prevent users from gaining valuable insights and predictions.

---
