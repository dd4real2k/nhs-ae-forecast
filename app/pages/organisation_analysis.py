import streamlit as st
from src.app_data import load_model_ready_data, get_organisation_list, filter_organisation
from src.charts import plot_org_attendance, plot_org_over4

df = load_model_ready_data()

st.title("Organisation Analysis")

orgs = get_organisation_list(df)
selected_org = st.selectbox("Select organisation", orgs)

org_df = filter_organisation(df, selected_org)

fig = plot_org_attendance(org_df, selected_org)
st.plotly_chart(fig, use_container_width=True)

fig2 = plot_org_over4(org_df, selected_org)
st.plotly_chart(fig2, use_container_width=True)
