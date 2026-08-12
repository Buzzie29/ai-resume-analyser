# AI Resume Analyzer

An intelligent resume analysis platform that compares resumes against job descriptions, identifies matching and missing skills, and provides an overall compatibility score.

The project is being built as a full-stack application with a FastAPI backend, interactive frontend, and future AI/LLM integration.

---

## Project Status

🚧 **Under Development**

Current development is focused on building the backend analysis engine.

### Current Features

- Resume file upload
- PDF resume parsing
- DOCX resume parsing
- TXT resume parsing
- Resume text preprocessing
- Job description parsing
- TF-IDF based resume/JD similarity scoring
- Skill extraction
- Matched skill detection
- Missing skill detection
- Automated backend tests
- FastAPI API documentation

### Planned Features

- Interactive web frontend
- Resume analysis dashboard
- Job description input interface
- Visual match score
- Skill comparison visualization
- Resume recommendations
- AI/LLM-powered semantic analysis
- AI-generated improvement suggestions
- Resume section analysis
- Multiple resume support
- Analysis history
- Mobile application

---

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- PyPDF
- python-docx
- scikit-learn
- pytest

### Frontend

Planned:

- React
- TypeScript
- Modern CSS / UI framework

### AI

Planned:

- LLM integration
- Semantic embeddings
- AI-powered resume analysis
- AI-generated recommendations

### Development

- Git
- GitHub
- Visual Studio Code

---

## Architecture

The current backend follows a service-based architecture:

```text
                    AI Resume Analyzer
                           |
              +------------+------------+
              |                         |
           Resume                 Job Description
              |                         |
              v                         v
        Resume Parser              JD Parser
              |                         |
              v                         v
       Text Processor             Text Processor
              |                         |
              +------------+------------+
                           |
                           v
                    Analysis Service
                    /             \
                   /               \
                  v                 v
          Matching Engine      Skill Analyzer
                  \                 /
                   \               /
                    +------v------+
                           |
                    Analysis Result
