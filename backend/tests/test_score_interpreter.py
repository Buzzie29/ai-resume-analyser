from app.services.score_interpreter import (
    get_match_grade,
    get_match_summary,
)


def test_excellent_match():
    assert get_match_grade(90) == "Excellent Match"


def test_good_match():
    assert get_match_grade(70) == "Good Match"


def test_moderate_match():
    assert get_match_grade(50) == "Moderate Match"


def test_low_match():
    assert get_match_grade(20) == "Low Match"


def test_summary():
    summary = get_match_summary(85)

    assert "strongly" in summary.lower()
