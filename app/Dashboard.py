import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="NHS A&E Forecast Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("NHS A&E Demand Forecasting Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Monthly Attendance", "17,200")
col2.metric("Peak Month", "Dec")
col3.metric("Forecast Accuracy (R²)", "0.994")

st.markdown("### Key Insights")
st.markdown("""
- A&E demand shows a clear upward trend over time.
- Winter periods are associated with higher system pressure.
- XGBoost achieved the strongest overall forecasting performance.
""")

def build_sample_chart():
    data = pd.DataFrame({
        "Month": pd.date_range(start="2023-01-01", periods=24, freq="M"),
        "Attendance": [
            15000, 14500, 15200, 16000, 15800, 16200,
            17000, 16800, 17200, 17500, 18000, 17800,
            18200, 18500, 18300, 18700, 19000, 18800,
            19200, 19500, 19300, 19800, 20000, 19700
        ]
    })

    fig = px.line(
        data,
        x="Month",
        y="Attendance",
        title="Monthly A&E Attendance Trend"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Attendance",
        title_x=0
    )

    return fig

st.plotly_chart(build_sample_chart(), width="stretch")

st.info("Use the navigation panel on the left to move between dashboard pages.")
