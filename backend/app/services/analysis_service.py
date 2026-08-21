from app.services.matcher import calculate_match_score
from app.services.skill_analyzer import compare_skills
from app.services.ats_analyzer import calculate_ats_score
from app.services.recommendation_engine import generate_recommendations
from app.services.score_interpreter import (
    get_match_grade,
    get_match_summary,
)

SKILLS = [
    "Python",
    "FastAPI",
    "PostgreSQL",
    "Docker",
    "Git",
    "GitHub",
    "AWS",
    "Redis",
    "Pytest",
    "Linux",
]


def analyze_resume(resume_text: str, job_description: str):
    """Analyze a resume against a job description."""

    # Existing services
    tfidf_score = calculate_match_score(resume_text, job_description)
    skill_analysis = compare_skills(
        resume_text,
        job_description,
        SKILLS,
    )
    ats_score = calculate_ats_score(resume_text, job_description)

    # ---------- Weighted Scoring ----------
    required = len(skill_analysis["required_skills"])
    matched = len(skill_analysis["matched_skills"])

    recommendations = generate_recommendations(
        matched_skills=skill_analysis["matched_skills"],
        missing_skills=skill_analysis["missing_skills"],
        ats_score=ats_score,
    )

    skill_overlap = (matched / required * 100) if required else 0

    # Small keyword bonus
    keyword_bonus = 20 if matched >= max(1, required // 2) else 10 if matched > 0 else 0

    match_score = round(
        tfidf_score * 0.30 + skill_overlap * 0.50 + keyword_bonus,
        2,
    )

    match_score = min(match_score, 100)

    grade = get_match_grade(match_score)
    summary = get_match_summary(match_score)

    return {
        "match_score": match_score,
        "ats_score": ats_score,
        "grade": grade,
        "summary": summary,
        "matched_skills": skill_analysis["matched_skills"],
        "missing_skills": skill_analysis["missing_skills"],
        "resume_skills": skill_analysis["resume_skills"],
        "required_skills": skill_analysis["required_skills"],
        "recommendations": recommendations,
    }
