from app.services.ats_analyzer import calculate_ats_score


def test_high_ats_score():
    resume = """
    Tanmay Kohale
    tanmay@example.com

    Skills
    Python FastAPI Git

    Experience
    Built backend APIs.

    Education
    B.Tech
    """

    jd = "Python FastAPI Git Developer"

    score = calculate_ats_score(resume, jd)

    assert score == 100


def test_partial_ats_score():
    resume = """
    Skills
    Python
    """

    jd = "Python Developer"

    score = calculate_ats_score(resume, jd)

    assert score == 40
    
