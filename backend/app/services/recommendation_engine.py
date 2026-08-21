def generate_recommendations(
    matched_skills: list[str],
    missing_skills: list[str],
    ats_score: int,
):
    """Generate actionable resume recommendations."""

    recommendations = []

    skill_messages = {
        "Docker": (
            "Learn Docker",
            "Add a Dockerized project to improve compatibility.",
        ),
        "AWS": (
            "Mention Cloud Experience",
            "Include AWS projects or coursework if applicable.",
        ),
        "PostgreSQL": (
            "Highlight Database Skills",
            "Mention PostgreSQL work from projects or coursework.",
        ),
        "Redis": (
            "Add Caching Experience",
            "Redis knowledge is valuable for backend roles.",
        ),
        "Git": (
            "Show Version Control",
            "Include Git collaboration experience.",
        ),
        "GitHub": (
            "Strengthen GitHub Portfolio",
            "Showcase active repositories and meaningful commits.",
        ),
    }

    for skill in missing_skills:
        if skill in skill_messages:
            title, message = skill_messages[skill]
            recommendations.append(
                {
                    "title": title,
                    "message": message,
                    "type": "skill",
                }
            )

    if ats_score < 60:
        recommendations.append(
            {
                "title": "Improve ATS Compatibility",
                "message": "Add clear section headings like Skills, Experience, and Education.",
                "type": "ats",
            }
        )

    if matched_skills:
        recommendations.append(
            {
                "title": "Highlight Your Strengths",
                "message": f"Emphasize {matched_skills[0]} projects near the top of your resume.",
                "type": "strength",
            }
        )

    return recommendations
