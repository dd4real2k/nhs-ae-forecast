# NHS A&E Performance Analysis and Demand Forecasting (2020-2026)

## Overview
This project analyses NHS A&E (Accident & Emergency) performance data using multi-year provider-level datasets from **April 2020 to February 2026**.

It combines **data engineering, SQL analysis, and machine learning** to explore demand patterns, waiting-time pressures, and forecast future A&E attendances.

## Project Highlights
- Analysed NHS A&E provider-level data from April 2020 to February 2026
- Built SQL queries to investigate demand and waiting-time performance
- Developed and compared multiple forecasting models
- Extended the project with a FastAPI backend and Streamlit dashboard

## Live Demo
- Streamlit App: []
- API Docs: []

## Dashboard Preview

### Main Dashboard
![Dashboard](images/dashboard_main.png)

### Forecast View
![Forecast](images/dashboard_forecast.png)

### Model Comparison
![Model Comparison](images/model_comparison.png)

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- SQL
- Matplotlib & Seaborn
- Scikit-learn (Machine Learning)
- XGBoost
- TensorFlow (LSTM)
- Jupyter Notebook

## Skills Demonstrated
- Data cleaning and preprocessing
- SQL analysis
- Time-series feature engineering
- Machine learning model development
- Model evaluation and comparison
- API development with FastAPI
- Dashboard development with Streamlit

## Project Workflow
1. Multi-file data ingestion and cleaning (2020-2026)
2. Data standardisation and feature engineering
3. Storage in SQLite database
4. SQL-based exploratory analysis
5. Data visualisation
6. Time-series feature engineering (lags, rolling statistics)
7. Predictive modelling for demand forecasting
8. Model comparison and evaluation

## Project Architecture
Raw NHS Files → Data Cleaning & Standardisation → SQLite Database → SQL Analysis → Feature Engineering → Forecasting Models → FastAPI Backend → Streamlit Dashboard

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

# SQL Queries

This folder contains SQL queries used for the NHS A&E analysis project.

- `01_national_summary.sql` — national totals and row count
- `02_top_attendance_orgs.sql` — busiest organisations by attendance
- `03_over4_waits.sql` — worst over-4-hour wait pressure
- `04_long_waits.sql` — longest 12+ hour waits
- `05_regional_summary.sql` — regional/parent organisation comparison
- `06_rankings.sql` — pressure bands and ranking queries

## Predictive Modelling

Multiple models were developed to forecast A&E demand:

- Linear Regression (baseline)
- Random Forest
- XGBoost
- LSTM (deep learning)

## Best Model Summary
Among the models tested, XGBoost achieved the strongest forecasting performance based on RMSE and R², showing better ability to capture non-linear demand patterns than the baseline and tree-based alternatives.

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

## Model Performance

    model |	MAE |	RMSE |	R2 |	rmse_rank |	mae_rank |	r2_rank
0 	XGBoost |	416.167358 | 701.702238 |	0.994462 |	1.0 |	2.0 |	1.0
1 	Random Forest |	414.320308 |	720.905674 |	0.994155 |	2.0 |	1.0 |	2.0
2 	Linear Regression |	530.182780 |	802.000728 |	0.992766 |	3.0 |	4.0 |	3.0
3 	LSTM |	528.642469 |	838.547306 |	0.992092 |	4.0 |	3.0 |	4.0

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

## Data Source
This project uses NHS England A&E monthly statistics covering April 2020 to February 2026. The data was combined across multiple monthly files, cleaned, standardised, and stored in SQLite for analysis and forecasting.

Source: [NHS England A&E Attendances and Emergency Admissions](https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2025-26/)


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
  - streamlit run app/dashboard.py

## Future Improvements
- Incorporate external features (weather, population, public holidays)
- Hyperparameter tuning for improved model performance
- Deploy the Streamlit app and FastAPI service
- Add explainability tooling for model interpretation
