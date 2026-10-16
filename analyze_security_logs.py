
import pandas as pd
from pathlib import Path
from security_ml import predict_access

# Read the real security log
LOG_FILE = Path("security_logs.csv")

if not LOG_FILE.exists():
    print("Security log file not found.")
    raise SystemExit(1)

logs = pd.read_csv(LOG_FILE)

required_columns = [
    "timestamp",
    "username",
    "event",
    "success",
    "role",
]

if not all(column in logs.columns for column in required_columns):
    print("Security log is missing required columns.")
    raise SystemExit(1)

if logs.empty:
    print("No security events found.")
    raise SystemExit(0)

print("EHR Security Log Analysis")
print("-" * 35)

for _, row in logs.iterrows():
    event = str(row["event"]).lower()
    success = str(row["success"]).strip().lower()

    # Convert logged events into simple model features.
    failed_attempts = 0 if success in ("true", "1", "yes") else 1

    unusual_location = 0
    access_hour = 12
    records_accessed = 1

    # These are proxies, not actual measurements.
    # A failed event alone does not prove suspicious behavior.
    if any(word in event for word in ["failed", "denied", "blocked"]):
        failed_attempts = max(failed_attempts, 1)

    prediction = predict_access(
        access_hour=access_hour,
        failed_attempts=failed_attempts,
        records_accessed=records_accessed,
        unusual_location=unusual_location,
    )

    print(f"User: {row['username']}")
    print(f"Event: {row['event']}")
    print(f"Success: {row['success']}")
    print(f"ML prediction: {prediction}")
    print("-" * 35)
