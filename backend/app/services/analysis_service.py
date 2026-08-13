from app.services.score_interpreter import (
    get_match_grade,
    get_match_summary,
)

from app.services.ats_analyzer import calculate_ats_score
from app.services.matcher import calculate_match_score
from app.services.skill_analyzer import compare_skills

DEFAULT_SKILLS = [
    "Python",
    "FastAPI",
    "Django",
    "Flask",
    "Java",
    "JavaScript",
    "TypeScript",
    "React",
    "Node.js",
    "SQL",
    "PostgreSQL",
    "MySQL",
    "MongoDB",
    "Docker",
    "Kubernetes",
    "Git",
    "GitHub",
    "AWS",
    "Azure",
]


def analyze_resume(
    resume_text: str,
    job_description: str,
) -> dict:
    """Analyze a resume against a job description."""

    match_score = calculate_match_score(
        resume_text,
        job_description,
    )
    ats_score = calculate_ats_score(
        resume_text,
        job_description,
    )

    grade = get_match_grade(match_score)
    summary = get_match_summary(match_score)

    skill_analysis = compare_skills(
        resume_text,
        job_description,
        DEFAULT_SKILLS,
    )

    return {
        "match_score": match_score,
        "ats_score": ats_score,
        "grade": grade,
        "summary": summary,
        "matched_skills": skill_analysis["matched_skills"],
        "missing_skills": skill_analysis["missing_skills"],
        "resume_skills": skill_analysis["resume_skills"],
        "required_skills": skill_analysis["required_skills"],
    }
