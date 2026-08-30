from fastapi import FastAPI
from pydantic import BaseModel

from backend.modules.rule_engine import analyze_job_text
from backend.modules.nlp_analyzer import analyze_text_with_ml
from backend.modules.risk_engine import calculate_final_risk
from backend.modules.safety_advisor import generate_safety_recommendations


app = FastAPI(
    title="JobShield AI",
    description="AI-powered fake job and recruitment scam detection API",
    version="1.0.0"
)


class JobAnalysisRequest(BaseModel):
    job_text: str


@app.get("/")
def home():
    return {
        "message": "Welcome to JobShield AI",
        "status": "API is running"
    }


@app.post("/analyze")
def analyze_job(request: JobAnalysisRequest):

    # Step 1: Analyze the job using rule-based detection.
    rule_result = analyze_job_text(request.job_text)

    # Step 2: Analyze the job using the ML model.
    ml_result = analyze_text_with_ml(request.job_text)

    # Step 3: Combine the rule and ML results.
    final_risk = calculate_final_risk(
        rule_result,
        ml_result
    )

    # Step 4: Generate safety recommendations
    # based on the detected scam signals.
    recommendations = generate_safety_recommendations(
        rule_result["detected_signals"]
    )

    # Step 5: Return the complete investigation.
    return {
        "risk_score": final_risk["risk_score"],
        "risk_level": final_risk["risk_level"],

        "rule_analysis": rule_result,

        "ml_analysis": ml_result,

        "safety_recommendations": recommendations
    }

    # Step 1: Analyze the job using rule-based detection.
    rule_result = analyze_job_text(request.job_text)

    # Step 2: Analyze the same job using the ML model.
    ml_result = analyze_text_with_ml(request.job_text)

    # Step 3: Combine both analyses.
    final_risk = calculate_final_risk(
        rule_result,
        ml_result
    )

    # Step 4: Return the complete investigation result.
    return {
        "risk_score": final_risk["risk_score"],
        "risk_level": final_risk["risk_level"],

        "rule_analysis": rule_result,

        "ml_analysis": ml_result
    }