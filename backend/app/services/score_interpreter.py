def get_match_grade(score: float) -> str:
    """Return a human-friendly grade for a match score."""

    if score >= 80:
        return "Excellent Match"

    if score >= 60:
        return "Good Match"

    if score >= 40:
        return "Moderate Match"

    return "Low Match"


def get_match_summary(score: float) -> str:
    """Return a short explanation for the score."""

    if score >= 80:
        return "Your resume aligns strongly with the job description."

    if score >= 60:
        return "Your resume is a good match, but a few improvements could increase compatibility."

    if score >= 40:
        return "Your resume has partial overlap with the job requirements."

    return "Your resume has very little overlap with the job description."
