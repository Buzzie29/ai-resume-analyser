import re


def clean_text(text: str) -> str:
    """Clean and normalize extracted text."""

    if not text:
        return ""

    # Normalize line breaks and tabs
    text = text.replace("\n", " ")
    text = text.replace("\r", " ")
    text = text.replace("\t", " ")

    # Remove excessive whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted special characters
    text = re.sub(r"[^\w\s.,+#/-]", "", text)

    # Remove leading/trailing whitespace
    return text.strip()


def normalize_text(text: str) -> str:
    """Convert text to lowercase for comparison."""

    return clean_text(text).lower()
