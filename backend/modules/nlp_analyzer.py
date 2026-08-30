import joblib
from pathlib import Path


# Find the backend directory.
BASE_DIR = Path(__file__).resolve().parent.parent

# Build the path to the trained ML model.
MODEL_PATH = BASE_DIR / "models" / "scam_model.pkl"


# Load the trained model when this module is imported.
model = joblib.load(MODEL_PATH)


def analyze_text_with_ml(job_text: str):
    """
    Analyze job text using the trained machine-learning model.
    """

    # Predict the class:
    # 0 = legitimate
    # 1 = suspicious/scam
    prediction = model.predict([job_text])[0]

    # Get probability for both classes.
    probabilities = model.predict_proba([job_text])[0]

    # Probability that the text belongs to class 1.
    scam_probability = probabilities[1]

    # Convert numerical prediction into a readable label.
    if prediction == 1:
        prediction_label = "suspicious"
    else:
        prediction_label = "legitimate"

    return {
        "prediction": prediction_label,
        "scam_probability": round(float(scam_probability), 4)
    }


if __name__ == "__main__":

    test_message = """
    Congratulations! You have been selected for a work-from-home job.
    Pay ₹2000 registration fee today to confirm your position.
    """

    result = analyze_text_with_ml(test_message)

    print(result)