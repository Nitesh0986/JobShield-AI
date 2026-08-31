import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ---------------------------------------
# 1. Load dataset
# ---------------------------------------

DATA_PATH = "backend/data/jobs.csv"

df = pd.read_csv(DATA_PATH)

print("\nDataset loaded successfully.")
print("Total records:", len(df))
print("\nColumns:", df.columns.tolist())


# ---------------------------------------
# 2. Prepare data
# ---------------------------------------

X = df["text"]
y = df["label"]


# ---------------------------------------
# 3. Split dataset
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ---------------------------------------
# 4. Convert text into TF-IDF features
# ---------------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# ---------------------------------------
# 5. Train ML model
# ---------------------------------------

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)


# ---------------------------------------
# 6. Make predictions
# ---------------------------------------

y_pred = model.predict(X_test_tfidf)


# ---------------------------------------
# 7. Calculate metrics
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)


# ---------------------------------------
# 8. Display results
# ---------------------------------------

print("\n====================================")
print("       JOBSHIELD ML EVALUATION")
print("====================================")

print(f"\nAccuracy  : {accuracy:.2f}")
print(f"Precision : {precision:.2f}")
print(f"Recall    : {recall:.2f}")
print(f"F1 Score  : {f1:.2f}")


print("\n====================================")
print("Classification Report")
print("====================================")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


print("\n====================================")
print("Confusion Matrix")
print("====================================")

cm = confusion_matrix(y_test, y_pred)

print("\n                 Predicted")
print("               Legit  Scam")
print(f"Actual Legit    {cm[0][0]:>4}  {cm[0][1]:>4}")
print(f"Actual Scam     {cm[1][0]:>4}  {cm[1][1]:>4}")


# Extract individual confusion-matrix values.
tn, fp, fn, tp = cm.ravel()

print("\nConfusion Matrix Breakdown:")
print(f"True Negatives  (TN): {tn}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Positives  (TP): {tp}")