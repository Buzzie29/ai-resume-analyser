from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(
    resume_text: str,
    job_description: str,
) -> float:
    """Calculate similarity between a resume and job description."""

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    documents = [
        resume_text,
        job_description,
    ]

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0],
        vectors[1],
    )[
        0
    ][0]

    return round(float(similarity * 100), 2)
