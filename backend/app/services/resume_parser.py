from pathlib import Path

from docx import Document
from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF resume."""

    reader = PdfReader(file_path)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text).strip()


def extract_text_from_docx(file_path: str) -> str:
    """Extract text from a DOCX resume."""

    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text).strip()


def extract_text_from_txt(file_path: str) -> str:
    """Extract text from a TXT resume."""

    return Path(file_path).read_text(encoding="utf-8").strip()


def extract_resume_text(file_path: str) -> str:
    """Extract text from a supported resume file."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    if extension == ".docx":
        return extract_text_from_docx(file_path)

    if extension == ".txt":
        return extract_text_from_txt(file_path)

    raise ValueError("Unsupported file format. " "Supported formats: PDF, DOCX, TXT.")
