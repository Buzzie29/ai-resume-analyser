from fastapi import APIRouter

from app.database.analysis_repository import get_recent_analyses

router = APIRouter(
    prefix="/api/history",
    tags=["History"],
)


@router.get("")
def get_history():
    """Return recent resume analyses."""

    analyses = get_recent_analyses()

    for analysis in analyses:
        analysis["id"] = str(analysis.pop("_id"))

    return analyses
