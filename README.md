## NHS A&E Forecasting System
End-to-end data science project forecasting NHS Accident & Emergency (A&E) demand using SQL, machine learning, and deep learning, deployed with FastAPI and Streamlit.

Built as part of my transition from IT Support to Data Science & AI

## Why This Matters
Accurate A&E demand forecasting helps NHS organisations:
- Plan staffing levels
- Anticipate winter pressure
- Reduce patient waiting times
- Allocate resources efficiently

This project demonstrates how data science can support real healthcare decision-making.

## Live Demo
- Streamlit App: [View Dashboard](Coming Soon)
- API Docs: [View Here](https://nhs-ae-sql-analysis.onrender.com/docs)
- Health Check: [View Here](https://nhs-ae-sql-analysis.onrender.com/health)

## Dashboard Preview
Below are key views from the interactive NHS A&E demand forecasting dashboard.

### Dashboard Overview
[![Dashboard Overview](images/dashboard_main.png)](images/dashboard_main.png)

### Forecast View
[![Forecast Dashboard](images/dashboard_forecast.png)](images/dashboard_forecast.png)

### Model Comparison
[![Model Comparison](images/model_comparison.png)](images/model_comparison.png)

## Project Architecture
```
Raw NHS Data (2020-2026)
→ Data Cleaning & Standardisation
→ SQLite Database
→ SQL Analysis
→ Feature Engineering
→ Forecasting Models (XGBoost, LSTM)
→ FastAPI Backend
→ Streamlit Dashboard
```

## Key Insights
- A small number of trusts handle ~65% of total demand
- Higher demand strongly correlates with 4-hour breaches
- Significant variation exists in long (12+ hour) waits
- Clear seasonality: winter months consistently show higher pressure
- Demand is highly driven by recent historical patterns

## Approach
- Combined multi-year NHS datasets (2020–2026)
- Cleaned and standardised data across years
- Engineered operational and time-series features
- Built SQL queries for demand and performance analysis
- Developed forecasting models using multiple approaches
- Deployed predictions via API and dashboard
- Evaluated models using time-based splits to reflect real-world forecasting scenarios

## SQL Analysis
This folder contains SQL queries used for the NHS A&E analysis project.
- `01_national_summary.sql` — national totals and validation
- `02_top_attendance_orgs.sql` — busiest organisations
- `03_over4_waits.sql` — 4-hour breach analysis
- `04_long_waits.sql` — 12+ hour delays
- `05_regional_summary.sql` — regional comparison
- `06_rankings.sql` — pressure ranking across organisations

## Model Performance
| Model | MAE | RMSE | R² |
|------|-----:|------:|----:|
| XGBoost | 416.17 | 701.70 | 0.9945 |
| Random Forest | 414.32 | 720.91 | 0.9942 |
| Linear Regression | 530.18 | 802.00 | 0.9928 |
| LSTM | 528.64 | 838.55 | 0.9921 |

## Model Selection
Several forecasting models were evaluated, including Linear Regression, Random Forest, XGBoost, and LSTM.

For deployment, **XGBoost** was selected as the production model because it delivered the best overall balance of forecast quality based on **RMSE** and **R²**, while Random Forest achieved a slightly lower MAE.

## Why XGBoost performed better:
- Handles structured/tabular data more effectively
- Captures non-linear relationships with engineered features
- More stable with limited dataset size
- Easier to tune and deploy

## Why LSTM underperformed:
- Dataset is structured rather than raw sequential signals
- Limited observations per organisation
- Requires more complex tuning and scaling

For this problem, **feature engineering + tree-based models outperform deep learning.**

This highlights the importance of ** choosing models based on characteristics, not complexity.**

## Forecasting Approach
### Objective
Predict monthly A&E attendances per NHS organisation

### Features Used
- Lag features (1, 3, 6, 12 months)
- Rolling averages and variability
- Seasonal encoding (month cyclic features)
- Operational indicators (admissions, wait times, booked attendances)

## Application Layer
**FastAPI**
- Serves trained model predictions
- Provides structured API endpoints

**Streamlit**
- Interactive dashboard
- Forecast visualisation
- Model comparison display

This transforms the project into a **deployable data product**, not just analysis.

## Deployment Configuration
The live API and dashboard are configured to use:

- **Model Type:** XGBoost
- **Model File:** `models/xgboost_model.json`

## Key Takeaway
This project shows that:
- Real-world forecasting is driven more by **data quality and feature engineering** than model complexity
- Tree-based models can outperform deep learning on structured datasets
- End-to-end delivery (data → model → API → dashboard) is critical in production environments

## Tech Stack
- Python (Pandas, NumPy)
- SQL & SQLite
- Scikit-learn
- XGBoost
- TensorFlow (LSTM)
- Matplotlib & Seaborn
- FastAPI
- Streamlit

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
git clone https://github.com/dd4real2k/nhs-ae-forecast.git
cd nhs-ae-forecast
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
## What This Project Demonstrates
- Working with real NHS datasets
- Writing analytical SQL queries
- Building time-series forecasting models
- Comparing ML vs deep learning approaches
- Designing feature engineering pipelines
- Deploying models via FastAPI
- Building interactive dashboards
- Structuring a production-style data project

## Limitations
- No external drivers (weather, flu trends, population)
- Forecast currently depends on historical operational features
- SQLite used for simplicity (not production scale)
- No automated retraining or monitoring yet

## Future Improvements
- Add external features (weather, population, public holidays)
- Implement walk-forward validation
- Add SHAP explainability
- Add model monitoring & retraining pipeline

## Data Source
NHS England A&E monthly statistics (April 2020 – February 2026)

Source: [NHS England A&E Attendances and Emergency Admissions](https://www.england.nhs.uk/statistics/statistical-work-areas/ae-waiting-times-and-activity/ae-attendances-and-emergency-admissions-2025-26/)

## Summary
This project demonstrates the ability to take:
**raw healthcare data → insight → forecasting → deployment**
— reflecting how real-world data teams operate and deliver value.
