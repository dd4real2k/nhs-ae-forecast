import json
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from src.config import MODEL_FEATURES
from src.payloads import build_prediction_payload


def prepare_training_data(df: pd.DataFrame, target_col: str):
    X = df[MODEL_FEATURES].copy()
    y = df[target_col].copy()
    return X, y


def evaluate_regression_model(y_true, y_pred) -> dict:
    return {
        "MAE": float(mean_absolute_error(y_true, y_pred)),
        "RMSE": float(root_mean_squared_error(y_true, y_pred)),
        "R2": float(r2_score(y_true, y_pred)),
    }

def save_metrics(metrics: dict, output_path: str) -> None:
    with open(output_path, "w") as f:
        json.dump(metrics, f, indent=2)
