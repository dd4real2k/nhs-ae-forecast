import pandas as pd


def load_external_features(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def create_calendar_features(df: pd.DataFrame, date_col: str = "period") -> pd.DataFrame:
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["quarter"] = df[date_col].dt.quarter
    return df


def merge_external_features(
    main_df: pd.DataFrame,
    external_df: pd.DataFrame,
    keys: list[str]
) -> pd.DataFrame:
    return main_df.merge(external_df, on=keys, how="left")


def validate_merge_keys(df: pd.DataFrame, required_cols: list[str]) -> None:
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing merge keys/columns: {missing}")
