from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

MODEL_READY_FILENAME = "nhs_ae_model_ready_with_features.csv"
MODEL_COMPARISON_FILENAME = "model_comparison.csv"
DEFAULT_MODEL_FILENAME = "random_forest_model.joblib"

API_BASE_URL = "http://127.0.0.1:8000"

MODEL_FEATURES = [
    "year",
    "month",
    "quarter",
    "month_sin",
    "month_cos",
    "lag_1",
    "lag_3",
    "lag_6",
    "lag_12",
    "rolling_mean_3",
    "rolling_mean_6",
    "rolling_std_3",
    "total_over_4hrs",
    "total_emergency_admissions",
    "total_booked_attendances",
    "total_dta_waits",
]
