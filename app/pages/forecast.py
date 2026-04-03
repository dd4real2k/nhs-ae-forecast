import sys
from pathlib import Path
import importlib

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import requests
import streamlit as st
from src.app_data import load_model_ready_data, get_organisation_list, filter_organisation
from src.forecasting import build_prediction_payload
import src.config as cfg

API_BASE_URL = cfg.API_BASE_URL

df = load_model_ready_data()

st.title("Forecast NHS A&E Attendances")

orgs = get_organisation_list(df)
selected_org = st.selectbox("Select organisation", orgs)

org_df = filter_organisation(df, selected_org)
latest = org_df.iloc[-1]

payload = build_prediction_payload(latest)

if st.button("Generate Forecast"):
    try:
        response = requests.post(f"{API_BASE_URL}/predict", json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        predicted_value = float(result["predicted_attendance"])

        st.metric("Predicted Attendance", f"{predicted_value:,.0f}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Make sure FastAPI is running.")
    except requests.exceptions.Timeout:
        st.error("The API request timed out.")
    except requests.exceptions.HTTPError:
        st.error(f"API error: {response.text}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
