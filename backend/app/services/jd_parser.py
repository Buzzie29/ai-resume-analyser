from app.services.text_processor import clean_text, normalize_text


def parse_job_description(text: str) -> dict:
    """Clean and normalize a job description."""

    if not text or not text.strip():
        raise ValueError("Job description cannot be empty.")

    cleaned_text = clean_text(text)
    normalized_text = normalize_text(text)

    return {
        "original_text": text.strip(),
        "cleaned_text": cleaned_text,
        "normalized_text": normalized_text,
    }
