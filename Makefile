install:
	pip install -r requirements.txt

test:
	pytest

run-api:
	uvicorn api.main:app --reload

run-app:
	streamlit run app/Dashboard.py
