SAFETY_RECOMMENDATIONS = {

    "payment_request": [
        "Do not pay any registration, processing, or security fee.",
        "Verify whether the employer officially charges candidates before proceeding."
    ],

    "urgency": [
        "Do not make a rushed decision because of an urgent deadline.",
        "Verify the opportunity independently before responding."
    ],

    "unrealistic_offer": [
        "Be cautious of guaranteed jobs or unusually high salary promises.",
        "Verify the salary and position through the employer's official career page."
    ],

    "sensitive_information": [
        "Never share OTPs, passwords, bank details, or card information with recruiters.",
        "Avoid sending identity documents until the employer and recruitment process are verified."
    ],

    "suspicious_contact": [
        "Verify the recruiter through an independent source.",
        "Do not rely only on WhatsApp or Telegram communication for employment verification."
    ]
}


def generate_safety_recommendations(detected_signals):

    recommendations = []

    for signal in detected_signals:

        signal_recommendations = SAFETY_RECOMMENDATIONS.get(
            signal,
            []
        )

        for recommendation in signal_recommendations:

            if recommendation not in recommendations:
                recommendations.append(recommendation)

    if not recommendations:

        recommendations.append(
            "Verify the employer, recruiter, and job posting before sharing personal information."
        )

    return recommendations


if __name__ == "__main__":

    test_signals = [
        "payment_request",
        "urgency"
    ]

    result = generate_safety_recommendations(
        test_signals
    )

    for recommendation in result:
        print("-", recommendation)