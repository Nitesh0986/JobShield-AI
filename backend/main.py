from fastapi import FastAPI
from pydantic import BaseModel

from backend.modules.rule_engine import analyze_job_text


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

    result = analyze_job_text(request.job_text)

    return result