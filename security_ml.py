
import joblib
import pandas as pd
from pathlib import Path

MODEL_FILE = Path(__file__).with_name("access_model.pkl")

FEATURES = [
    "access_hour",
    "failed_attempts",
    "records_accessed",
    "unusual_location",
]


def predict_access(access_hour, failed_attempts,
                   records_accessed, unusual_location):
    if not MODEL_FILE.exists():
        raise FileNotFoundError(
            "Model not found. Run python access_detection.py first."
        )

    model = joblib.load(MODEL_FILE)

    sample = pd.DataFrame(
        [[access_hour, failed_attempts,
          records_accessed, unusual_location]],
        columns=FEATURES,
    )

    prediction = model.predict(sample)[0]
    return prediction
