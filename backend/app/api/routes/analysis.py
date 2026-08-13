from fastapi import APIRouter, HTTPException

from app.schemas.analysis import AnalysisRequest
from app.services.analysis_service import analyze_resume
from app.schemas.analysis import (
    AnalysisRequest,
    AnalysisResponse,
)

router = APIRouter(
    prefix="/api/analyze",
    tags=["Analysis"],
)


@router.post("", response_model=AnalysisResponse)
def analyze(request: AnalysisRequest):
    """Analyze a resume against a job description."""

    try:
        return analyze_resume(
            request.resume_text,
            request.job_description,
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )
