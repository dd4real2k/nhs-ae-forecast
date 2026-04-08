import streamlit as st
from src.app_data import load_model_comparison_data
from src.charts import plot_metric_bar

st.set_page_config(page_title="Model Comparison", layout="wide")

df = load_model_comparison_data()

st.title("Model Comparison")
st.caption("Compare forecast models using MAE, RMSE, and R².")

best_rmse = df.sort_values("RMSE").iloc[0]
best_mae = df.sort_values("MAE").iloc[0]
best_r2 = df.sort_values("R2", ascending=False).iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Best RMSE", f"{best_rmse['Model']} ({best_rmse['RMSE']:.2f})")
col2.metric("Best MAE", f"{best_mae['Model']} ({best_mae['MAE']:.2f})")
col3.metric("Best R²", f"{best_r2['Model']} ({best_r2['R2']:.4f})")

st.dataframe(df, width="stretch")

fig = plot_metric_bar(df, "RMSE", "Model Comparison by RMSE")
st.plotly_chart(fig, width="stretch")

fig2 = plot_metric_bar(df, "MAE", "Model Comparison by MAE")
st.plotly_chart(fig2, width="stretch")

fig3 = plot_metric_bar(df, "R2", "Model Comparison by R²")
st.plotly_chart(fig3, width="stretch")
