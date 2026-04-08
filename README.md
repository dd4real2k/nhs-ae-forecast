## NHS A&E Performance Analysis & Forecasting
End-to-end data project analysing NHS A&E performance (2020–2026), combining SQL analytics, machine learning, and deployment (FastAPI + Streamlit) to model and forecast healthcare demand.

## Why This Project Matters
This project demonstrates the ability to:
- Analyse real-world healthcare data at scale using SQL and Python
- Identify operational pressure points in NHS A&E services
- Build and evaluate forecasting models for demand prediction
- Deploy data solutions using FastAPI and Streamlit
- Structure a production-style data project end-to-end

## Project Summary
This project analyses NHS A&E (Accident & Emergency) performance data using multi-year provider-level datasets from **April 2020 to February 2026**.

It combines **data engineering, SQL analytics, and machine learning** to explore demand patterns, waiting-time pressures, and forecast future A&E attendances.

The project demonstrates how healthcare data can be used to support operational planning and decision-making.

## Key Insights
- High-demand trusts consistently experience higher 4-hour breaches
- Significant variation exists in 12+ hour delays across organisations
- Clear seasonal patterns show increased pressure during winter months
- A small number of NHS organisations handle disproportionately high patient volumes (top 10 account for ~65% of total demand)
- A&E demand is strongly driven by recent trends and recurring patterns

## Live Demo
- Streamlit App: [View Dashboard](https://nhs-ae-forecast.streamlit.app/)
- API Docs: [View Here](https://nhs-ae-sql-analysis.onrender.com/docs)

## Dashboard Preview

### Main Dashboard
![Dashboard](images/dashboard_main.png)

### Forecast View
![Forecast](images/dashboard_forecast.png)

### Model Comparison
![Model Comparison](images/model_comparison.png)

## Project Architecture
```
Raw NHS Files
→ Data Cleaning & Standardisation
→ SQLite Database
→ SQL Analysis
→ Feature Engineering
→ Forecasting Models
→ FastAPI Backend
→ Streamlit Dashboard
```

## Tools Used
- Python (Pandas, NumPy)
- SQL & SQLite
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost
- TensorFlow (LSTM)
- FastAPI
- Streamlit
- Jupyter Notebook

## Skills Demonstrated
- Data cleaning and preprocessing
- SQL-based analysis
- Time-series feature engineering
- Machine learning model development
- Model evaluation and comparison
- API development with FastAPI
- Data app development (Streamlit)

# NHS A&E Performance Analysis & Forecasting
An end-to-end healthcare analytics project analysing NHS A&E performance from April 2020 to February 2026 using SQL, Python, machine learning, FastAPI, and Streamlit.

This project is designed to demonstrate job-ready skills in:
- SQL analytics on operational healthcare data
- Data cleaning and feature engineering
- Forecast model development and evaluation
- API deployment with FastAPI
- Dashboard development with Streamlit
- Writing reusable, testable Python code

## Business Problem
NHS A&E departments face sustained operational pressure driven by rising demand, long waiting times, and resource constraints.

This project explores those pressures using provider-level monthly NHS A&E data and extends the analysis into forecasting, helping answer questions such as:
- Which organisations experience the highest demand?
- Where are 4-hour breaches most severe?
- Which trusts face the greatest long-wait pressure?
- Can future monthly attendance be forecast from recent operational patterns?

## Project Scope
The project combines:
- **SQL analysis** for operational insight
- **Python data processing** for reusable feature engineering
- **Machine learning** for monthly demand forecasting
- **FastAPI** for serving predictions
- **Streamlit** for interactive reporting

## Key Questions Answered
- Which organisations handle the highest A&E demand?
- Which trusts experience the worst 4-hour performance?
- Where are long (12+ hour) delays most prevalent?
- How does performance vary across regions?
- Can future A&E demand be predicted using historical data?

## Approach
- Combined multiple NHS monthly datasets (2020–2026) into a unified dataset
- Cleaned and standardised data across years
- Engineered key performance metrics
- Built SQL queries to analyse demand and waiting-time performance
- Developed time-series features for forecasting
- Trained and compared multiple machine learning models

## SQL Analysis

This folder contains SQL queries used for the NHS A&E analysis project.

- `01_national_summary.sql` — national totals and validation
- `02_top_attendance_orgs.sql` — busiest organisations
- `03_over4_waits.sql` — 4-hour breach analysis
- `04_long_waits.sql` — 12+ hour delays
- `05_regional_summary.sql` — regional comparison
- `06_rankings.sql` — pressure ranking across organisations


## Predictive Modelling
Multiple models were developed to forecast A&E demand:

- Linear Regression (baseline)
- Random Forest
- XGBoost
- LSTM (deep learning)

## Best Model
XGBoost achieved the strongest performance across all evaluation metrics, indicating its effectiveness in capturing non-linear patterns in A&E demand compared to baseline and alternative models.

## Model Performance
| Model | MAE | RMSE | R² |
|------|-----:|------:|----:|
| XGBoost | 416.17 | 701.70 | 0.9945 |
| Random Forest | 414.32 | 720.91 | 0.9942 |
| Linear Regression | 530.18 | 802.00 | 0.9928 |
| LSTM | 528.64 | 838.55 | 0.9921 |

## Features Used
- Lag features (1, 3, 6, 12 months)
- Rolling averages and variability
- Seasonal encoding (month cyclic features)
- Operational indicators (admissions, wait times, booked attendances)

## Key Modelling Insight
A&E demand is primarily driven by:
- Recent historical activity (lag features)
- Short-term trends (rolling averages)
- Seasonal patterns (monthly cycles)

## Application Layer
This project includes:

- **FastAPI backend** for serving predictions
- **Streamlit dashboard** for interactive analysis and forecasting

This transforms the project from static analysis into a deployable, end-to-end data application.

This architecture reflects a simplified production setup, where models are served via an API and consumed by a frontend application.

## Project Structure
- `data/raw/` → original NHS datasets (ignored in Git)
- `data/processed/` → cleaned datasets and outputs
- `models/` → saved model artifacts
- `notebooks/` → analysis and modelling
- `src/` → reusable functions
- `sql/` → SQL queries
- `api/` → FastAPI backend
- `app/` → Streamlit dashboard

## How to Run

You can explore the dashboard directly or run the project locally using the steps below.

### 1. Clone the repository
```bash
git clone https://github.com/dd4real2k/nhs-ae-sql-analysis.git
cd nhs-ae-sql-analysis
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Run API
```
uvicorn api.main:app --reload
```
### 4. Run dashboard
```
streamlit run app/Dashboard.py
```
## What This Project Demonstrates to Employers
- Ability to work with real NHS datasets
- Strong SQL and analytical thinking
- End-to-end ML pipeline development
- Experience deploying data products
- Understanding of real-world operational problems

## Future Improvements
- Incorporate external features (weather, population, public holidays)
- Apply deeper hyperparameter tuning
- Add model explainability (SHAP)
- Automate data pipeline and retraining
- Deploy fully on cloud (AWS/GCP)

## Summary

This project demonstrates the ability to take raw healthcare data through the full data lifecycle, from ingestion and analysis to modelling and deployment, in a way that reflects real-world data roles.

## Testing and Quality

This repository includes:
- unit tests for core utility functions
- API endpoint tests
- GitHub Actions CI to run tests automatically on push and pull request

## Limitations

- Forecasting currently uses historical operational features only
- No external drivers such as weather, holidays, flu trends, or population shifts are included
- SQLite is suitable for demonstration, but a production environment would likely use PostgreSQL or a warehouse
- Monitoring, retraining, and model versioning are not yet automated

## Interview Talking Points

In interview, this project demonstrates that I can:
1. work with messy real-world healthcare data
2. write SQL to answer operational questions
3. engineer time-series features for forecasting
4. compare multiple regression approaches
5. expose a model through an API
6. build a simple user-facing analytics application
7. structure code into reusable modules with testing

## Data Source
NHS England A&E monthly statistics (April 2020 – February 2026)

Source: [NHS England A&E Attendances and Emergency Admissions](https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2025-26/)
