from src.config import MODEL_FEATURES


def build_prediction_payload(row) -> dict:
    payload = {}

    for feature in MODEL_FEATURES:
        if feature in ["year", "month", "quarter"]:
            payload[feature] = int(row[feature])
        else:
            payload[feature] = float(row[feature])

    return payload
