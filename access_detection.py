
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load fictional labelled training data
data = pd.read_csv("access_training_data.csv")

features = [
    "access_hour",
    "failed_attempts",
    "records_accessed",
    "unusual_location",
]

X = data[features]
y = data["label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

# Train the ML model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42,
)

model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)

print("Model trained successfully!")
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# Test a sample access pattern
sample = pd.DataFrame(
    [[2, 8, 40, 1]],
    columns=features,
)

result = model.predict(sample)[0]
print("\nSample access prediction:", result)

# Save the trained model
joblib.dump(model, "access_model.pkl")
print("Model saved as access_model.pkl")
