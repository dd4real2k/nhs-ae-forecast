import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st

from src.app_data import load_model_ready_data, get_organisation_list, filter_organisation
from src.forecasting import build_prediction_payload
from src.config import API_BASE_URL

st.set_page_config(page_title="Forecast", layout="wide")

df = load_model_ready_data()

st.title("Forecast NHS A&E Attendances")
st.caption("Generate the next-month attendance forecast for a selected NHS organisation.")

orgs = get_organisation_list(df)
selected_org = st.selectbox("Select organisation", orgs)

org_df = filter_organisation(df, selected_org).sort_values("period")
latest = org_df.iloc[-1]
payload = build_prediction_payload(latest)

# Show recent history
history_window = st.slider(
    "Months of history to display",
    min_value=12,
    max_value=60,
    value=24,
    step=6,
)

plot_df = org_df.tail(history_window).copy()

col1, col2, col3 = st.columns(3)
col1.metric("Latest Actual Attendance", f"{plot_df.iloc[-1]['total_attendances']:,.0f}")
col2.metric("Latest Total Over 4hrs", f"{plot_df.iloc[-1]['total_over_4hrs']:,.0f}")
col3.metric("Latest Emergency Admissions", f"{plot_df.iloc[-1]['total_emergency_admissions']:,.0f}")

if st.button("Generate Forecast"):
    with st.spinner("Generating forecast..."):
        try:
            response = requests.post(f"{API_BASE_URL}/predict", json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()

            predicted_value = float(result["predicted_attendance"])
            last_date = pd.to_datetime(org_df["period"].max())
            next_date = last_date + pd.offsets.MonthBegin(1)

            change = predicted_value - float(plot_df.iloc[-1]["total_attendances"])
            pct_change = (
                change / float(plot_df.iloc[-1]["total_attendances"]) * 100
                if float(plot_df.iloc[-1]["total_attendances"]) != 0
                else 0
            )

            st.metric(
                "Predicted Next-Month Attendance",
                f"{predicted_value:,.0f}",
                f"{pct_change:+.2f}% vs latest month",
            )

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=plot_df["period"],
                    y=plot_df["total_attendances"],
                    mode="lines+markers",
                    name="Historical Attendances",
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=[last_date, next_date],
                    y=[plot_df.iloc[-1]["total_attendances"], predicted_value],
                    mode="lines+markers",
                    name="Forecast",
                    line=dict(dash="dash"),
                )
            )

            fig.update_layout(
                title=f"A&E Attendance Trend and Forecast — {selected_org}",
                xaxis_title="Period",
                yaxis_title="Total Attendances",
                hovermode="x unified",
            )

            st.plotly_chart(fig, width="stretch")

            forecast_summary = pd.DataFrame(
                {
                    "Period": [last_date.date(), next_date.date()],
                    "Value": [plot_df.iloc[-1]["total_attendances"], predicted_value],
                    "Type": ["Latest Actual", "Forecast"],
                }
            )
            st.dataframe(forecast_summary, width="stretch")

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the API. Make sure FastAPI is running.")
        except requests.exceptions.Timeout:
            st.error("The API request timed out.")
        except requests.exceptions.HTTPError:
            st.error(f"API error: {response.text}")
        except Exception as exc:
            st.error(f"Unexpected error: {e}")
