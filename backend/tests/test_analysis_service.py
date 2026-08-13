from unittest import result

from app.services.analysis_service import analyze_resume
from app.services.ats_analyzer import calculate_ats_score


def test_analyze_resume():
    resume = """
    Python developer with experience in FastAPI,
    Git and PostgreSQL.
    """

    job_description = """
    Looking for a Python developer with FastAPI,
    Git, PostgreSQL and Docker.
    """

    result = analyze_resume(
        resume,
        job_description,
    )

    assert "ats_score" in result
    assert "grade" in result
    assert "summary" in result
    assert result["grade"] in [
        "Excellent Match",
        "Good Match",
        "Moderate Match",
        "Low Match",
    ]
    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["matched_skills"]
    assert "Git" in result["matched_skills"]
    assert "PostgreSQL" in result["matched_skills"]

    assert "Docker" in result["missing_skills"]


def test_analysis_returns_score():
    result = analyze_resume(
        "Python developer",
        "Python developer",
    )
    assert result["ats_score"] >= 0
    assert result["ats_score"] <= 100
    assert "grade" in result
    assert "summary" in result
    assert result["match_score"] >= 40
    assert result["match_score"] <= 100
