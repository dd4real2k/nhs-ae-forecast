import pandas as pd
import numpy as np


def clean_column_name(col: str) -> str:
    col = col.strip().lower()
    col = col.replace("&", "and")
    col = col.replace("+", "plus")
    col = col.replace("-", "_")
    col = col.replace("/", "_")
    col = col.replace(" ", "_")
    col = col.replace(".", "")
    return col


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [clean_column_name(col) for col in df.columns]
    return df


def convert_numeric(df: pd.DataFrame, numeric_cols: list[str]) -> pd.DataFrame:
    df = df.copy()
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    existing_numeric_cols = [col for col in numeric_cols if col in df.columns]
    df[existing_numeric_cols] = df[existing_numeric_cols].fillna(0)
    return df


def parse_period_column(df: pd.DataFrame, col: str = "period") -> pd.DataFrame:
    df = df.copy()
    df[col] = pd.to_datetime(df[col])
    return df


def create_time_features(df: pd.DataFrame, date_col: str = "period") -> pd.DataFrame:
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["quarter"] = df[date_col].dt.quarter
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)
    return df


def create_lag_features(
    df: pd.DataFrame,
    target_col: str,
    group_col: str,
    lags: list[int]
) -> pd.DataFrame:
    df = df.copy().sort_values([group_col, "period"])
    for lag in lags:
        df[f"lag_{lag}"] = df.groupby(group_col)[target_col].shift(lag)
    return df


def create_rolling_features(
    df: pd.DataFrame,
    target_col: str,
    group_col: str,
    windows: list[int]
) -> pd.DataFrame:
    df = df.copy().sort_values([group_col, "period"])
    for window in windows:
        df[f"rolling_mean_{window}"] = (
            df.groupby(group_col)[target_col]
            .transform(lambda x: x.shift(1).rolling(window).mean())
        )
    if 3 in windows:
        df["rolling_std_3"] = (
            df.groupby(group_col)[target_col]
            .transform(lambda x: x.shift(1).rolling(3).std())
        )
    return df


def summarise_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    missing = df.isna().sum()
    pct = (missing / len(df)) * 100
    out = pd.DataFrame({"missing_count": missing, "missing_pct": pct})
    return out.sort_values("missing_pct", ascending=False)


def add_derived_metrics(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["total_attendances"] = (
        df["aande_attendances_type_1"]
        + df["aande_attendances_type_2"]
        + df["aande_attendances_other_aande_department"]
    )

    df["total_booked_attendances"] = (
        df["aande_attendances_booked_appointments_type_1"]
        + df["aande_attendances_booked_appointments_type_2"]
        + df["aande_attendances_booked_appointments_other_department"]
    )

    df["total_over_4hrs"] = (
        df["attendances_over_4hrs_type_1"]
        + df["attendances_over_4hrs_type_2"]
        + df["attendances_over_4hrs_other_department"]
    )

    df["total_booked_over_4hrs"] = (
        df["attendances_over_4hrs_booked_appointments_type_1"]
        + df["attendances_over_4hrs_booked_appointments_type_2"]
        + df["attendances_over_4hrs_booked_appointments_other_department"]
    )

    df["total_dta_waits"] = (
        df["patients_who_have_waited_4_12_hs_from_dta_to_admission"]
        + df["patients_who_have_waited_12plus_hrs_from_dta_to_admission"]
    )

    df["total_emergency_admissions"] = (
        df["emergency_admissions_via_aande___type_1"]
        + df["emergency_admissions_via_aande___type_2"]
        + df["emergency_admissions_via_aande___other_aande_department"]
        + df["other_emergency_admissions"]
    )

    df["over_4hr_rate"] = np.where(
        df["total_attendances"] > 0,
        df["total_over_4hrs"] / df["total_attendances"],
        0
    )

    df["booked_over_4hr_rate"] = np.where(
        df["total_booked_attendances"] > 0,
        df["total_booked_over_4hrs"] / df["total_booked_attendances"],
        0
    )

    df["admission_rate"] = np.where(
        df["total_attendances"] > 0,
        df["total_emergency_admissions"] / df["total_attendances"],
        0
    )

    return df
