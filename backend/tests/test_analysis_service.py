from app.services.analysis_service import analyze_resume


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

    assert "match_score" in result

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

    assert result["match_score"] > 0
