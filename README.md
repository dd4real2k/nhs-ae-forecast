# NHS A&E Performance Analysis and Demand Forecasting (2020-2026)

## Overview
This project analyses NHS A&E (Accident & Emergency) performance data using multi-year provider-level datasets from **April 2020 to February 2026**.

It combines **data engineering, SQL analysis, and machine learning** to explore demand patterns, waiting-time pressures, and forecast future A&E attendances.

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- SQL
- Matplotlib & Seaborn
- Scikit-learn (Machine Learning)
- XGBoost
- TensorFlow (LSTM)
- Jupyter Notebook

## Project Workflow
1. Multi-file data ingestion and cleaning (2020-2026)
2. Data standardisation and feature engineering
3. Storage in SQLite database
4. SQL-based exploratory analysis
5. Data visualisation
6. Time-series feature engineering (lags, rolling statistics)
7. Predictive modelling for demand forecasting
8. Model comparison and evaluation

## Business Problem
NHS A&E departments face increasing operational pressure due to:

- Rising patient demand
- Long waiting times
- Resource and capacity constraints

This project investigates these challenges using historical data and extends the analysis into **predictive modelling** to support better planning and decision-making.

## Key Questions Answered
- Which organisations handle the highest A&E demand?
- Which trusts experience the worst 4-hour performance?
- Where are long (12+ hour) delays most prevalent?
- How does performance vary across regions?
- Can future A&E demand be predicted using historical data?

## Key Insights
- A small number of organisations handle disproportionately high patient volumes
- High-demand trusts often also experience higher 4-hour breaches
- Significant variation exists in 12+ hour waits across organisations
- Regional differences highlight uneven healthcare pressure distribution
- A&E demand shows strong dependence on recent historical trends and seasonality

## Approach
- Combined multiple NHS monthly datasets (2020–2026) into a unified dataset
- Cleaned and standardised data across years
- Engineered key performance metrics
- Built SQL queries to analyse demand and waiting-time performance
- Developed time-series features for forecasting
- Trained and compared multiple machine learning models

## Predictive Modelling

Multiple models were developed to forecast A&E demand:

- Linear Regression (baseline)
- Random Forest
- XGBoost
- LSTM (deep learning)

## Features Used
- Lag features (1, 3, 6, 12 months)
- Rolling averages and variability
- Seasonal encoding (month cyclic features)
- Operational indicators (admissions, wait times, booked attendances)

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Models were compared to identify the best-performing approach for forecasting NHS A&E demand.

## Feature Importance Insights

The model relies most heavily on:

- Recent attendances (lag features)
- Rolling averages (short-term trends)
- Seasonal signals (monthly patterns)

This indicates that A&E demand is driven by **recent activity and recurring seasonal behaviour**

## App and API Layer

This project also includes:

- **FastAPI backend** for serving model predictions
- **Streamlit dashboard** for interactive analysis, forecasting, and model comparison

This extends the project from notebook-based analysis to an interactive data application.

## Project Structure
- `data/raw/` → original NHS datasets (ignored in Git)
- `data/processed/` → cleaned datasets, predictions, and metrics
- `models/` → saved model artifacts
- `notebooks/` → analysis and forecasting notebooks
- `src/` → reusable data processing functions
- `sql/` → SQL analysis queries
- `api/` → FastAPI backend
- `app/` → Streamlit dashboard
- `nhs_ae_2020_2026.db` → SQLite database

## How to Run
1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the analysis notebooks in order:
- `01_data_analysis.ipynb`
- `02_forecasting_model.ipynb`
- `03_xgboost_forecasting.ipynb`
- `04_lstm_forecasting.ipynb`
- `05_model_comparison.ipynb`

4. Run the FastAPI backend:
  - uvicorn api.main:app --reload

5. Run the Streamlit app:
  - streamlit run app/streamlit_app.py

## Future Improvements
- Incorporate external features (weather, population, public holidays)
- Hyperparameter tuning for improved model performance
- Deploy the Streamlit app and FastAPI service
- Add explainability tooling for model interpretation
