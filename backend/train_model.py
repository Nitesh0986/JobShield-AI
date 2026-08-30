import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

from pathlib import Path


# Find the project directory.
BASE_DIR = Path(__file__).resolve().parent

# Create the path to our dataset.
DATA_PATH = BASE_DIR / "data" / "jobs.csv"

# Create the path where the trained model will be saved.
MODEL_PATH = BASE_DIR / "models" / "scam_model.pkl"


# Load the dataset.
data = pd.read_csv(DATA_PATH)


# Separate input text from the target label.
X = data["text"]
y = data["label"]


# Divide the dataset into training and testing data.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# Create a machine-learning pipeline.
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )
])


# Train the complete pipeline.
model.fit(X_train, y_train)


# Predict labels for the test data.
y_pred = model.predict(X_test)


# Calculate accuracy.
accuracy = accuracy_score(y_test, y_pred)


print("Model Training Complete")
print("-----------------------")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Accuracy: {accuracy:.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save the trained model.
import joblib

joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")