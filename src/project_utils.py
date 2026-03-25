import pandas as pd
import numpy as np

def clean_column_name(col):
    col = col.strip().lower()
    col = col.replace("&", "and")
    col = col.replace("+", "plus")
    col = col.replace("-", "_")
    col = col.replace("/", "_")
    col = col.replace(" ", "_")
    col = col.replace(".", "")
    return col

def clean_columns(df):
    df = df.copy()
    df.columns = [clean_column_name(col) for col in df.columns]
    return df

def convert_numeric(df, numeric_cols):
    df = df.copy()
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df[numeric_cols] = df[numeric_cols].fillna(0)
    return df

def add_derived_metrics(df):
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
