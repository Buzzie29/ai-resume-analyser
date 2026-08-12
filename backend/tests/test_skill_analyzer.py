from app.services.skill_analyzer import (
    compare_skills,
    extract_skills,
)

SKILLS = [
    "Python",
    "FastAPI",
    "Django",
    "Git",
    "Docker",
    "PostgreSQL",
]


def test_extract_skills():
    text = """
    Python developer with experience in FastAPI,
    Git and Docker.
    """

    result = extract_skills(text, SKILLS)

    assert "Python" in result
    assert "FastAPI" in result
    assert "Git" in result
    assert "Docker" in result
    assert "Django" not in result


def test_compare_skills():
    resume = """
    Python developer with FastAPI and Git experience.
    """

    job_description = """
    Looking for a Python developer with FastAPI,
    Docker and PostgreSQL.
    """

    result = compare_skills(
        resume,
        job_description,
        SKILLS,
    )

    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["matched_skills"]

    assert "Docker" in result["missing_skills"]
    assert "PostgreSQL" in result["missing_skills"]
