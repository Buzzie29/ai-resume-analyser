from pydantic import BaseModel


class AnalysisRequest(BaseModel):
    resume_text: str
    job_description: str


class Recommendation(BaseModel):
    title: str
    message: str
    type: str


class AnalysisResponse(BaseModel):
    analysis_id: str
    match_score: float
    ats_score: int
    grade: str
    summary: str
    matched_skills: list[str]
    missing_skills: list[str]
    resume_skills: list[str]
    required_skills: list[str]
    recommendations: list[Recommendation]
