from app.services.recommendation_engine import generate_recommendations


def test_generates_skill_recommendations():
    result = generate_recommendations(
        matched_skills=["Python"],
        missing_skills=["Docker", "AWS"],
        ats_score=50,
    )

    assert len(result) >= 3
    assert any(r["title"] == "Learn Docker" for r in result)


def test_generates_strength_recommendation():
    result = generate_recommendations(
        matched_skills=["FastAPI"],
        missing_skills=[],
        ats_score=90,
    )

    assert any(r["type"] == "strength" for r in result)
