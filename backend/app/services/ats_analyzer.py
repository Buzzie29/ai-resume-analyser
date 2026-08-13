import re


def calculate_ats_score(
    resume_text: str,
    job_description: str,
) -> int:
    """Calculate a simple ATS compatibility score."""

    score = 0

    text = resume_text.lower()
    jd = job_description.lower()

    # Email detection
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume_text):
        score += 20

    # Common sections
    if "skills" in text:
        score += 20

    if "experience" in text:
        score += 20

    if "education" in text:
        score += 20

    # Keyword overlap
    jd_words = set(re.findall(r"\b[a-zA-Z]{3,}\b", jd))
    resume_words = set(re.findall(r"\b[a-zA-Z]{3,}\b", text))

    if jd_words.intersection(resume_words):
        score += 20

    return score
