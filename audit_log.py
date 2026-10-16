
import csv
import os
from datetime import datetime, timezone

CSV_FILE = "security_logs.csv"

FIELDNAMES = [
    "timestamp",
    "username",
    "event",
    "success",
    "role",
]


def log_security_event(username, event, success, role="Unknown"):
    """Save a security event without recording passwords or patient data."""

    file_exists = os.path.exists(CSV_FILE)

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8",
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDNAMES,
        )

        if not file_exists or os.path.getsize(CSV_FILE) == 0:
            writer.writeheader()

        writer.writerow({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "username": username,
            "event": event,
            "success": success,
            "role": role,
        })

    print(f"Security event recorded: {event}")
