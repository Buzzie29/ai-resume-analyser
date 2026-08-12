import re


def extract_skills(text: str, skills: list[str]) -> list[str]:
    """Find known skills that appear in the text."""

    normalized_text = text.lower()

    found_skills = []

    for skill in skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, normalized_text):
            found_skills.append(skill)

    return found_skills


def compare_skills(
    resume_text: str,
    job_description: str,
    skills: list[str],
) -> dict:
    """Compare skills found in a resume against a job description."""

    resume_skills = extract_skills(
        resume_text,
        skills,
    )

    required_skills = extract_skills(
        job_description,
        skills,
    )

    matched_skills = [skill for skill in required_skills if skill in resume_skills]

    missing_skills = [skill for skill in required_skills if skill not in resume_skills]

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }
