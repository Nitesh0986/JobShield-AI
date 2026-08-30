def calculate_final_risk(rule_result, ml_result):
    """
    Combine Rule Engine and ML results
    into one final JobShield risk assessment.
    """

    # Get the score produced by the Rule Engine.
    rule_score = rule_result["risk_score"]

    # Get the probability produced by the ML model.
    ml_probability = ml_result["scam_probability"]

    # Convert ML probability from 0-1 into 0-100.
    ml_score = ml_probability * 100

    # Give more importance to transparent rule evidence
    # while still allowing the ML model to influence the result.
    final_score = (
        rule_score * 0.60
        + ml_score * 0.40
    )

    # Make sure the final score stays between 0 and 100.
    final_score = min(max(final_score, 0), 100)

    # Round the score for a clean user-facing result.
    final_score = round(final_score, 2)

    # Determine the final risk level.
    if final_score >= 70:
        risk_level = "HIGH"

    elif final_score >= 40:
        risk_level = "MEDIUM"

    else:
        risk_level = "LOW"

    return {
        "risk_score": final_score,
        "risk_level": risk_level
    }


if __name__ == "__main__":

    # Example Rule Engine result.
    rule_result = {
        "risk_score": 45
    }

    # Example ML result.
    ml_result = {
        "scam_probability": 0.7341
    }

    result = calculate_final_risk(
        rule_result,
        ml_result
    )

    print(result)