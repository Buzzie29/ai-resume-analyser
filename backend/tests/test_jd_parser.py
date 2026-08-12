import pytest

from app.services.jd_parser import parse_job_description


def test_parse_job_description():
    text = """
    Python Developer

    Required Skills:
    Python, FastAPI, Git

    Experience:
    2+ years
    """

    result = parse_job_description(text)

    assert result["original_text"].startswith("Python Developer")
    assert "Python Developer" in result["cleaned_text"]
    assert "python developer" in result["normalized_text"]


def test_empty_job_description():
    with pytest.raises(ValueError):
        parse_job_description("")
