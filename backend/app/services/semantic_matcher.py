import math
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

MODEL = "gemini-embedding-001"


def _cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a * a for a in vec_a))
    magnitude_b = math.sqrt(sum(b * b for b in vec_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return dot_product / (magnitude_a * magnitude_b)


def calculate_semantic_score(resume_text: str, job_description: str) -> float:
    """Calculate semantic similarity between resume and job description
    using Gemini's embedding API, comparing meaning rather than exact
    word overlap (unlike TF-IDF).
    """

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set.")

    client = genai.Client(api_key=api_key)

    result = client.models.embed_content(
        model=MODEL,
        contents=[resume_text, job_description],
    )

    if result.embeddings is None or len(result.embeddings) < 2:
        raise ValueError("Gemini returned no embeddings.")

    resume_embedding = result.embeddings[0].values
    job_embedding = result.embeddings[1].values

    if resume_embedding is None or job_embedding is None:
        raise ValueError("Gemini returned no embedding values.")

    similarity = max(_cosine_similarity(resume_embedding, job_embedding), 0)

    return round(similarity * 100, 2)
