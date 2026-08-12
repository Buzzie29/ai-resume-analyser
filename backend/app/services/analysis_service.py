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

    skill_analysis = compare_skills(
        resume_text,
        job_description,
        DEFAULT_SKILLS,
    )

    return {
        "match_score": match_score,
        "matched_skills": skill_analysis["matched_skills"],
        "missing_skills": skill_analysis["missing_skills"],
        "resume_skills": skill_analysis["resume_skills"],
        "required_skills": skill_analysis["required_skills"],
    }
