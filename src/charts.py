import plotly.express as px
import pandas as pd


def plot_monthly_attendance(monthly_df: pd.DataFrame):
    return px.line(
        monthly_df,
        x="period",
        y="total_attendances",
        title="Monthly NHS A&E Attendances"
    )


def plot_org_attendance(org_df: pd.DataFrame, org_name: str):
    return px.line(
        org_df,
        x="period",
        y="total_attendances",
        title=f"Total Attendances - {org_name}"
    )


def plot_org_over4(org_df: pd.DataFrame, org_name: str):
    return px.line(
        org_df,
        x="period",
        y="total_over_4hrs",
        title=f"Over 4-Hour Waits - {org_name}"
    )


def plot_metric_bar(df: pd.DataFrame, metric: str, title: str):
    return px.bar(df, x="model", y=metric, title=title)
