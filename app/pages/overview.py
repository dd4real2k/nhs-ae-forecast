import streamlit as st
from src.app_data import load_model_ready_data
from src.charts import plot_monthly_attendance

df = load_model_ready_data()

monthly = df.groupby("period", as_index=False)["total_attendances"].sum()

st.title("Overview")
fig = plot_monthly_attendance(monthly)
st.plotly_chart(fig, use_container_width=True)
