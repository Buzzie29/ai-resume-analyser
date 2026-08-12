from app.services.text_processor import clean_text, normalize_text


def test_clean_text():
    text = "Python    Developer\n\nFastAPI\tGit"

    result = clean_text(text)

    assert result == "Python Developer FastAPI Git"


def test_normalize_text():
    text = "Python Developer FASTAPI"

    result = normalize_text(text)

    assert result == "python developer fastapi"


def test_empty_text():
    assert clean_text("") == ""
    assert normalize_text("") == ""
