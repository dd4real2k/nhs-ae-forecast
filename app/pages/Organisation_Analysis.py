import streamlit as st
from src.app_data import load_model_ready_data, get_organisation_list, filter_organisation
from src.charts import plot_org_attendance, plot_org_over4

st.set_page_config(page_title="Organisation Analysis", layout="wide")

df = load_model_ready_data()

st.title("Organisation Analysis")
st.caption("Explore attendance and 4-hour pressure for individual NHS organisations.")

orgs = get_organisation_list(df)
selected_org = st.selectbox("Select organisation", orgs)

org_df = filter_organisation(df, selected_org).sort_values("period")

latest = org_df.iloc[-1]

col1, col2, col3 = st.columns(3)
col1.metric("Latest Attendance", f"{latest['total_attendances']:,.0f}")
col2.metric("Latest Over 4hrs", f"{latest['total_over_4hrs']:,.0f}")
col3.metric("Latest Over 4hr Rate", f"{latest['over_4hr_rate'] * 100:.2f}%")

fig = plot_org_attendance(org_df, selected_org)
st.plotly_chart(fig, width="stretch")

fig2 = plot_org_over4(org_df, selected_org)
st.plotly_chart(fig2, width="stretch")
