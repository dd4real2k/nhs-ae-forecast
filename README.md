# NHS A&E Performance Analysis (Feb 2026)

## Overview
This project analyses NHS A&E performance data for February 2026 using Python, SQLite, and SQL.

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- SQL
- Matplotlib & Seaborn
- Jupyter Notebook

## Project Workflow
1. Data loading and cleaning
2. Feature engineering
3. Storage in SQLite database
4. SQL analysis queries
5. Data visualisation

## Key Questions Answered
- Which organisations had the highest A&E demand?
- Which trusts had the worst 4-hour performance?
- Where are long (12+ hour) waits most common?
- How do regions compare?

## Key Insights
- A small number of organisations handle disproportionately high patient volumes
- High-demand trusts often also experience higher 4-hour breaches
- Significant variation exists in 12+ hour waits across organisations
- Regional differences highlight uneven healthcare pressure distribution

## Business Problem
NHS A&E departments face increasing pressure from rising patient demand,
long waiting times, and resource constraints.

This project analyses February 2026 data to identify:
- High-demand organisations
- Waiting-time bottlenecks
- Long (12+ hour) delays
- Regional performance differences

## Approach
- Cleaned and structured raw NHS data using Python
- Engineered key performance metrics
- Loaded data into SQLite
- Performed analytical queries using SQL
- Visualised key insights

## Outcome
- Identified high-pressure trusts
- Highlighted long wait-time patterns
- Provided regional comparison of performance

## Project Structure
- `data/` → raw dataset
- `notebooks/` → analysis notebook
- `src/` → reusable functions
- `sql/` → SQL queries
- `.db` → SQLite database

## Future Improvements
- Add Power BI or Tableau dashboard
- Analyse multiple months for trend analysis
- Build a Streamlit dashboard
- Add predictive modelling for demand forecasting
