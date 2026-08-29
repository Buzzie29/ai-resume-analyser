from functools import lru_cache

from sentence_transformers import SentenceTransformer, util


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    """Load and cache the sentence embedding model.

    Cached so the (relatively large) model is only loaded into memory
    once per process, not on every request.
    """
    return SentenceTransformer("all-MiniLM-L6-v2")


def calculate_semantic_score(resume_text: str, job_description: str) -> float:
    """Calculate semantic similarity between resume and job description.

    Unlike TF-IDF, this compares meaning rather than exact word overlap,
    so it can catch matches like "built REST APIs" vs "developed web services".
    """

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    model = get_model()

    embeddings = model.encode(
        [resume_text, job_description],
        convert_to_tensor=True,
    )

    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

    # cos_sim can technically be slightly negative for unrelated text;
    # clamp to 0 so the score stays in a sane 0-100 range.
    similarity = max(similarity, 0)

    return round(similarity * 100, 2)
