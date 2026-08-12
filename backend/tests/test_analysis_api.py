from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_analyze_api_success():
    response = client.post(
        "/api/analyze",
        json={
            "resume_text": (
                "Python developer with experience in " "FastAPI, Git and PostgreSQL."
            ),
            "job_description": (
                "Looking for a Python developer with "
                "FastAPI, Git, PostgreSQL and Docker."
            ),
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "match_score" in data
    assert "matched_skills" in data
    assert "missing_skills" in data

    assert "Python" in data["matched_skills"]
    assert "FastAPI" in data["matched_skills"]
    assert "Docker" in data["missing_skills"]


def test_analyze_api_empty_resume():
    response = client.post(
        "/api/analyze",
        json={
            "resume_text": "",
            "job_description": "Python developer",
        },
    )

    assert response.status_code == 400


def test_analyze_api_empty_job_description():
    response = client.post(
        "/api/analyze",
        json={
            "resume_text": "Python developer",
            "job_description": "",
        },
    )

    assert response.status_code == 400
