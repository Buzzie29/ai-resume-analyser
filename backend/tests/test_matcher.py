import pytest

from app.services.matcher import calculate_match_score


def test_matching_resume_and_job_description():
    resume = """
    Python developer with experience in FastAPI,
    Git, REST APIs and backend development.
    """

    job_description = """
    Looking for a Python developer with experience
    in FastAPI, Git and REST APIs.
    """

    score = calculate_match_score(
        resume,
        job_description,
    )

    assert score > 50


def test_unrelated_resume_and_job_description():
    resume = """
    Graphic designer experienced in Photoshop,
    Illustrator and visual design.
    """

    job_description = """
    Python backend developer with FastAPI,
    PostgreSQL and REST API experience.
    """

    score = calculate_match_score(
        resume,
        job_description,
    )

    assert score < 50


def test_empty_resume():
    with pytest.raises(ValueError):
        calculate_match_score(
            "",
            "Python developer",
        )


def test_empty_job_description():
    with pytest.raises(ValueError):
        calculate_match_score(
            "Python developer",
            "",
        )
