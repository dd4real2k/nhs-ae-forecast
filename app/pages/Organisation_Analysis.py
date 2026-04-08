import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.app_data import load_model_ready_data, get_organisation_list, filter_organisation
from src.charts import plot_org_attendance, plot_org_over4

df = load_model_ready_data()

st.title("Organisation Analysis")

orgs = get_organisation_list(df)
selected_org = st.selectbox("Select organisation", orgs)

org_df = filter_organisation(df, selected_org)

fig = plot_org_attendance(org_df, selected_org)
st.plotly_chart(fig, width="stretch")

fig2 = plot_org_over4(org_df, selected_org)
st.plotly_chart(fig2, width="stretch")
