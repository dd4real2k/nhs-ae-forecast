from pathlib import Path
import joblib
import pandas as pd
import xgboost as xgb

from src.config import MODELS_DIR, DEFAULT_MODEL_FILENAME, MODEL_FEATURES, DEFAULT_MODEL_TYPE


MODEL_PATH = MODELS_DIR / DEFAULT_MODEL_FILENAME

MODEL_TYPE = DEFAULT_MODEL_TYPE


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

    if MODEL_TYPE == "xgboost" or MODEL_PATH.suffix == ".json":
        model = xgb.XGBRegressor()
        model.load_model(str(MODEL_PATH))
        return model

    if MODEL_TYPE == "random_forest" or MODEL_PATH.suffix == ".joblib":
        return joblib.load(MODEL_PATH)

    raise ValueError(
        f"Unsupported model configuration: MODEL_TYPE={MODEL_TYPE}, MODEL_PATH={MODEL_PATH}"
    )

def prepare_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])
    missing = [col for col in MODEL_FEATURES if col not in df.columns]
    if missing:
        raise ValueError(f"Missing input features: {missing}")
    return df[MODEL_FEATURES]

def model_metadata() -> dict:
    return {
        "model_path": str(MODEL_PATH),
        "model_filename": DEFAULT_MODEL_FILENAME,
        "features_count": len(MODEL_FEATURES),
        "features": MODEL_FEATURES,
    }
