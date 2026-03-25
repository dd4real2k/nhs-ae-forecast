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
- Large variation in A&E demand across trusts
- Some high-volume trusts also have high wait times
- Long waits highlight pressure in patient flow
- Regional differences in performance exist

## Project Structure
- `data/` → raw dataset
- `notebooks/` → analysis notebook
- `src/` → reusable functions
- `sql/` → SQL queries
- `.db` → SQLite database
