import streamlit as st
from src.app_data import load_model_ready_data
from src.charts import plot_monthly_attendance

st.set_page_config(page_title="Overview", layout="wide")

df = load_model_ready_data()
monthly = df.groupby("period", as_index=False)["total_attendances"].sum()

st.title("Overview")
st.caption("National-level view of NHS A&E attendance trends over time.")

col1, col2, col3 = st.columns(3)
col1.metric("Rows", f"{len(df):,}")
col2.metric("Organisations", f"{df['org_name'].nunique():,}")
col3.metric("Periods", f"{df['period'].nunique():,}")

fig = plot_monthly_attendance(monthly)
st.plotly_chart(fig, width="stretch")
