import pandas as pd
from src.config import PROCESSED_DIR, MODEL_READY_FILENAME, MODEL_COMPARISON_FILENAME


def get_processed_data_path(filename: str):
    return PROCESSED_DIR / filename


def load_model_ready_data() -> pd.DataFrame:
    df = pd.read_csv(get_processed_data_path(MODEL_READY_FILENAME))
    df["period"] = pd.to_datetime(df["period"])
    return df


def load_model_comparison_data() -> pd.DataFrame:
    return pd.read_csv(get_processed_data_path(MODEL_COMPARISON_FILENAME))


def get_organisation_list(df: pd.DataFrame) -> list[str]:
    return sorted(df["org_name"].dropna().unique())


def filter_organisation(df: pd.DataFrame, org_name: str) -> pd.DataFrame:
    return df[df["org_name"] == org_name].sort_values("period").copy()
