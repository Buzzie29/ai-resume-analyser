import json
import os

from google import genai

from app.services.recommendation_engine import (
    generate_recommendations as generate_rule_based_recommendations,
)

MODEL = "gemini-3.7-flash"

SYSTEM_PROMPT = """You are a resume improvement assistant. Given a resume, a job \
description, and lists of matched/missing skills, generate 2-4 specific, \
actionable recommendations to help the candidate improve their resume for \
this specific job.

Respond with ONLY a JSON array, no other text, no markdown code fences. \
Each item must have exactly these fields:
- "title": a short heading (a few words)
- "message": one specific, actionable sentence
- "type": one of "skill", "ats", "strength", "wording"

Base recommendations on the actual resume content and job description, not \
generic advice. Prefer concrete suggestions over vague ones."""


def generate_ai_recommendations(
    resume_text: str,
    job_description: str,
    matched_skills: list[str],
    missing_skills: list[str],
    ats_score: int,
) -> list[dict]:
    """Generate resume recommendations using Gemini.

    Falls back to the rule-based recommendation engine if the API call
    fails for any reason (missing key, network issue, bad response, etc.)
    so the analysis endpoint never breaks because of the LLM call.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return generate_rule_based_recommendations(
            matched_skills, missing_skills, ats_score
        )

    try:
        client = genai.Client(api_key=api_key)

        user_message = f"""Resume:
{resume_text}

Job Description:
{job_description}

Matched skills: {", ".join(matched_skills) if matched_skills else "none"}
Missing skills: {", ".join(missing_skills) if missing_skills else "none"}
ATS score: {ats_score}/100"""

        response = client.models.generate_content(
            model=MODEL,
            contents=f"{SYSTEM_PROMPT}\n\n{user_message}",
        )

        if response.text is None:
            raise ValueError("Gemini returned no text (possibly blocked).")

        raw_text = response.text.strip()

        # Gemini sometimes wraps JSON in markdown fences despite instructions;
        # strip them defensively.
        if raw_text.startswith("```"):
            raw_text = raw_text.strip("`")
            if raw_text.startswith("json"):
                raw_text = raw_text[4:].strip()

        recommendations = json.loads(raw_text)

        # Basic shape validation -- if Gemini didn't follow the format,
        # fall back rather than returning malformed data to the frontend.
        for item in recommendations:
            if not all(key in item for key in ("title", "message", "type")):
                raise ValueError("Malformed recommendation item from LLM.")

        return recommendations

    except Exception:
        # Any failure (bad JSON, API error, rate limit, etc.) falls back
        # to the deterministic rule-based engine so the app stays working.
        return generate_rule_based_recommendations(
            matched_skills, missing_skills, ats_score
        )
