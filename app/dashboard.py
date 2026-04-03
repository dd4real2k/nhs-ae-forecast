import streamlit as st

st.set_page_config(
    page_title="NHS A&E Forecast Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("NHS A&E Performance Analysis and Demand Forecasting")
st.markdown(
    """
    Explore NHS A&E demand trends, waiting-time pressure, organisation-level analysis
    forecasting outputs, and model comparison results.
    """
)

st.info("Use the navigation panel on the left to move between pages.")
