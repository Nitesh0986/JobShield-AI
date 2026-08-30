import re


SCAM_PATTERNS = {

    "payment_request": [
        r"registration fee",
        r"processing fee",
        r"pay.*fee",
        r"payment.*required",
        r"pay.*to.*confirm",
        r"deposit.*amount",
        r"security deposit",
    ],

    "urgency": [
        r"apply immediately",
        r"act now",
        r"limited seats",
        r"limited vacancies",
        r"offer expires",
        r"urgent",
        r"today only",
        r"within \d+ hours",
    ],

    "unrealistic_offer": [
        r"guaranteed job",
        r"guaranteed placement",
        r"100% placement",
        r"no interview",
        r"earn.*\d+.*month",
    ],

    "sensitive_information": [
        r"send.*otp",
        r"share.*otp",
        r"send.*password",
        r"share.*password",
        r"send.*bank details",
        r"share.*bank details",
        r"send.*credit card",
        r"share.*credit card",
        r"send.*aadhaar",
        r"share.*aadhaar",
        r"send.*pan card",
        r"share.*pan card",
    ],

    "suspicious_contact": [
        r"contact.*whatsapp",
        r"contact.*telegram",
        r"message.*whatsapp",
        r"message.*telegram",
        r"only.*whatsapp",
        r"only.*telegram",
    ],
}


RISK_WEIGHTS = {
    "payment_request": 30,
    "urgency": 15,
    "unrealistic_offer": 20,
    "sensitive_information": 30,
    "suspicious_contact": 10,
}


EVIDENCE_MESSAGES = {
    "payment_request":
        "The message appears to request an upfront registration, processing, or security fee.",

    "urgency":
        "The message creates pressure to act quickly or suggests that the opportunity is time-limited.",

    "unrealistic_offer":
        "The opportunity contains potentially unrealistic job, salary, or placement claims.",

    "sensitive_information":
        "The message appears to request sensitive information such as OTPs, passwords, bank details, Aadhaar, or PAN information.",

    "suspicious_contact":
        "The message relies on communication channels such as WhatsApp or Telegram in a way that may require additional verification.",
}


SEVERITY = {
    "payment_request": "high",
    "urgency": "medium",
    "unrealistic_offer": "high",
    "sensitive_information": "high",
    "suspicious_contact": "medium",
}


def analyze_job_text(job_text: str):

    detected_signals = []
    evidence = []

    text = job_text.lower()

    for category, patterns in SCAM_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                if category not in detected_signals:

                    detected_signals.append(category)

                    evidence.append({
                        "type": category,
                        "severity": SEVERITY[category],
                        "message": EVIDENCE_MESSAGES[category]
                    })

                break

    score = sum(
        RISK_WEIGHTS[signal]
        for signal in detected_signals
    )

    score = min(score, 100)

    if score >= 70:
        risk_level = "HIGH"

    elif score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "detected_signals": detected_signals,
        "evidence": evidence
    }


if __name__ == "__main__":

    test_message = """
    Congratulations! You have been selected for a work-from-home job.
    Pay ₹2000 registration fee today to confirm your position.
    Limited seats available. Act now!
    """

    result = analyze_job_text(test_message)

    print(result)