from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.resume_parser import extract_resume_text

router = APIRouter(
    prefix="/api/resume",
    tags=["Resume"],
)


ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    """Upload a resume and extract its text."""

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No filename provided.",
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file format. " "Supported formats: PDF, DOCX, TXT.",
        )

    file_content = await file.read()

    with NamedTemporaryFile(
        suffix=extension,
        delete=False,
    ) as temp_file:
        temp_file.write(file_content)
        temp_file_path = temp_file.name

    try:
        extracted_text = extract_resume_text(temp_file_path)

        return {
            "filename": file.filename,
            "file_type": extension,
            "text": extracted_text,
        }

    finally:
        Path(temp_file_path).unlink(missing_ok=True)
