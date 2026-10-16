
from security_ml import predict_access

result = predict_access(
    access_hour=2,
    failed_attempts=8,
    records_accessed=40,
    unusual_location=1,
)

print("Access prediction:", result)
