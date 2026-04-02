import streamlit as st
from src.app_data import load_model_comparison_data
from src.charts import plot_metric_bar

df = load_model_comparison_data()

st.title("Model Comparison")
st.dataframe(df, use_container_width=True)

fig = plot_metric_bar(df, "RMSE", "Model Comparison by RMSE")
st.plotly_chart(fig, use_container_width=True)

fig2 = plot_metric_bar(df, "MAE", "Model Comparison by MAE")
st.plotly_chart(fig2, use_container_width=True)

fig3 = plot_metric_bar(df, "R2", "Model Comparison by R²")
st.plotly_chart(fig3, use_container_width=True)
