from pathlib import Path
import pandas as pd


def list_csv_files(folder_path: str) -> list[Path]:
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")

    files = sorted(folder.glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files found in: {folder_path}")

    return files


def read_csv_file(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df["source_file"] = file_path.name
    return df


def load_all_files(folder_path: str) -> pd.DataFrame:
    files = list_csv_files(folder_path)
    frames = [read_csv_file(file) for file in files]
    return pd.concat(frames, ignore_index=True)


def validate_required_columns(df: pd.DataFrame, required_cols: list[str]) -> None:
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
