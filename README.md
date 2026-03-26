# NHS A&E Performance Analysis and Demand Forecasting (2020-2026)

## Overview
This project analyses NHS A&E (Accident & Emergency) performance data using multi-year provider lever datasets from **April 2020 to Feb 2026**.

It combines __data engineering, SQL analysis, and machine learning__ to explore demand patterns, waiting-time pressures, and forecast future A&E attendances.

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- SQL
- Matplotlib & Seaborn
- Scikit-learn (Machine Learning)
- Jupyter Notebook

## Project Workflow
1. Multi-file data ingestion and cleaning (2020-2026)
2. Data Standardisation and Feature Engineering
3. Storage in SQLite database
4. SQL-base exploratory analysis
5. Data visualisation
6. Time-series feature engineering (lags, rolling statitics)
7. Predictive modelling for demand forecasting

## Business Problem
NHS A&E departments face increasing operational pressure due to:

- Rising patient demand
- Long waiting times
- Resource and capacity constraints

This project investigates these challenges using historical data and extends the analysis into __predictive modelling__ to support better planning and decision-making.

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
- Trained a machine learning model to predict A&E demand

## Predictive Modelling

A Random Forest model was developed to forecast NHS A&E demand using:

- Lag features (previous attendances: 1, 3, 6, 12 months)
- Rolling averages and variability
- Seasonal encoding (month cyclic features)
- Operational indicators (admissions, wait times, booked attendances)

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R² Score

The model achieved strong predictive performance, demonstrating that A&E demand is highly predictable using historical patterns.

## Feature Importance Insights

The model relies most heavily on:

- Recent attendances (lag features)
- Rolling averages (short-term trends)
- Seasonal signals (monthly patterns)

This indicates that A&E demand is driven by __recent activity and recurring seasonal behaviour__

## Project Structure
- `data/raw` → original NHS dataset (2020-2026)
- `data/processed`→ cleaned and model-ready datasets
- `notebooks/` → analysis and forecasting notebooks
- `src/` → reusable data processing functions
- `sql/` → SQL analysis queries
- `.db` → SQLite database

## How to Run
1. Clone the repository
2. Install dependencies:
  pip install -r requirements.txt
3. Run the analysis notebook:
  notebooks/01_data_analysis.ipynb
4. Run the forecasting notebook:
  notebooks/02_forecasting_model.ipynb

## Future Improvements
- Build an interactive dashboard (Streamlit or Power BI)
- Extend forecasting with advanced models (XGBoost, LSTM)
- Incorporate external features (weather, population, public holidays)
- Add predictive modelling for demand forecasting
- Deploy model as an API for real-time predictions
