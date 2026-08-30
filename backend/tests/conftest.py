from unittest.mock import patch

import pytest


@pytest.fixture(autouse=True)
def mock_gemini_recommendations():
    """Replace real Gemini API calls with a fake response during tests.

    Applied automatically to every test (autouse=True) so no test suite
    run ever depends on network access or burns free-tier API quota,
    and tests stay fast and deterministic.
    """

    fake_recommendations = [
        {
            "title": "Test Recommendation",
            "message": "This is a mocked recommendation for testing.",
            "type": "skill",
        }
    ]

    with patch(
        "app.services.analysis_service.generate_ai_recommendations",
        return_value=fake_recommendations,
    ):
        yield


@pytest.fixture(autouse=True)
def mock_gemini_semantic_score():
    """Replace real Gemini embedding calls with a fake score during tests."""

    with patch(
        "app.services.analysis_service.calculate_semantic_score",
        return_value=75.0,
    ):
        yield
