# AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green?logo=fastapi)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript)
![Vite](https://img.shields.io/badge/Vite-8-646CFF?logo=vite)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

An intelligent **AI-powered Resume Analyzer** that compares resumes against job descriptions, calculates ATS compatibility, identifies matched and missing skills, and provides actionable insights through a modern full-stack web application.

The project is being built with a **FastAPI backend**, **React + TypeScript frontend**, and future **LLM-powered semantic analysis**.

---

## Project Status

🚧 **Under Development**

The project now includes a working backend and frontend with **real resume upload functionality**, automated testing, and a scalable architecture. The next milestone is building the **live analysis dashboard** and integrating AI-powered recommendations.

---

## Table of Contents

- [Current Features](#current-features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Roadmap](#roadmap)
- [Upcoming Demo](#upcoming-demo)
- [Development Philosophy](#development-philosophy)
- [License](#license)

---

## Current Features

### Backend

- Resume Upload API
- PDF, DOCX and TXT parsing
- Resume text preprocessing
- Job description parsing
- TF-IDF resume/job similarity scoring
- Skill extraction
- Matched skill detection
- Missing skill detection
- ATS score calculation
- Match grading and summary
- Resume analysis API
- Swagger documentation
- 26 automated backend tests

### Frontend

- React + TypeScript
- Vite development environment
- Tailwind CSS UI
- Framer Motion animations
- Glassmorphism design
- Responsive landing page
- Drag-and-drop resume upload
- Live backend integration
- Upload success feedback

### Planned AI Features

- Semantic skill matching
- LLM-powered resume analysis
- AI-generated recommendations
- Resume rewrite suggestions
- Resume section analysis
- Career improvement insights

---

## Screenshots

> Screenshots will be updated as new milestones are completed.

### Frontend Landing Page

Current features include:

- Modern dark gradient interface
- Glassmorphism upload card
- Drag-and-drop resume upload
- Live FastAPI integration
- Animated UI components

> A full demo GIF will be added after the live analysis dashboard is completed.

---

## Tech Stack

### Backend

- Python 3.13
- FastAPI
- Uvicorn
- PyPDF
- python-docx
- scikit-learn
- Pytest

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Framer Motion
- Lucide React

### AI (Planned)

- LLM Integration
- Semantic Embeddings
- AI Resume Analysis
- AI Recommendations

### Development Tools

- Git
- GitHub
- Visual Studio Code
- PowerShell
- Python Virtual Environment

---

## Architecture

```text
                  AI Resume Analyzer

              ┌─────────────────────────┐
              │     React Frontend      │
              │ Upload • Dashboard • UI │
              └─────────────┬───────────┘
                            │
                       HTTP / Fetch
                            │
              ┌─────────────▼────────────┐
              │      FastAPI Backend     │
              └─────────────┬────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   Resume Parser      Analysis Service     ATS Analyzer
        │                   │                   │
        ▼                   ▼                   ▼
 Text Processor      Match Engine      Score Interpreter
                            │
                            ▼
                     JSON Response
```

The backend follows a **modular service-based architecture**, making each feature independently testable and easy to expand with future AI capabilities.

---

## Project Structure

```text
ai-resume-analyzer/
│
├── backend/
│   ├── app/
│   │   ├── ai/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── types/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   └── vite.config.ts
│
├── docs/
├── .gitignore
└── README.md
```

---

## Backend Setup

📍 **Location**

```text
backend/
```

### 1. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 2. Activate It

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run the Backend

```powershell
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

📍 **Location**

```text
frontend/
```

### Install Dependencies

```powershell
npm install
```

### Start Development Server

```powershell
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

The frontend communicates directly with the FastAPI backend using a dedicated API service layer.

---

## API Endpoints

| Method | Endpoint             | Purpose                           |
| ------ | -------------------- | --------------------------------- |
| GET    | `/`                  | API status                        |
| GET    | `/health`            | Health check                      |
| POST   | `/api/resume/upload` | Upload and parse a resume         |
| POST   | `/api/analyze`       | Analyze resume vs job description |

### Example Analysis Response

```json
{
  "match_score": 82,
  "ats_score": 91,
  "grade": "Excellent Match",
  "summary": "Your resume aligns strongly with the job description.",
  "matched_skills": [
    "Python",
    "FastAPI",
    "Git"
  ],
  "missing_skills": [
    "Docker"
  ],
  "resume_skills": [
    "Python",
    "FastAPI",
    "Git"
  ],
  "required_skills": [
    "Python",
    "FastAPI",
    "Git",
    "Docker"
  ]
}
```

---

## Matching Algorithm

The current matching engine combines multiple techniques:

- TF-IDF Vectorization
- Cosine Similarity
- Skill Extraction
- ATS Compatibility Scoring
- Match Grade Interpretation

Current grade thresholds:

| Score  | Grade           |
| ------ | --------------- |
| 80–100 | Excellent Match |
| 60–79  | Good Match      |
| 40–59  | Moderate Match  |
| 0–39   | Low Match       |

This transparent scoring system provides an explainable baseline before introducing semantic AI models.

---

## Testing

Run all backend tests:

```powershell
cd backend
python -m pytest
```

### Current Test Coverage

- Resume parser
- Text preprocessing
- Job description parser
- Matching engine
- Skill analyzer
- ATS analyzer
- Score interpreter
- Analysis service
- Analysis API

**Current milestone:** **26 passing tests**

---

## Roadmap

### Phase 1 — Backend Foundation

- [x] Project setup
- [x] Git/GitHub setup
- [x] FastAPI setup
- [x] Resume parser
- [x] Resume upload API
- [x] Text preprocessing
- [x] Job description parser
- [x] TF-IDF matching
- [x] Skill analysis
- [x] ATS score
- [x] Match grading
- [x] Analysis API
- [x] Automated testing

### Phase 2 — Frontend Foundation

- [x] React + TypeScript setup
- [x] Tailwind CSS
- [x] Landing page
- [x] Drag-and-drop upload
- [x] Backend integration
- [ ] Live analysis dashboard
- [ ] Animated score cards
- [ ] Resume preview
- [ ] Job description input
- [ ] Analysis report UI

### Phase 3 — AI Features

- [ ] Semantic embeddings
- [ ] LLM integration
- [ ] AI recommendations
- [ ] Resume rewrite suggestions
- [ ] Resume section analysis
- [ ] Career improvement insights

### Phase 4 — Production

- [ ] Database integration
- [ ] User authentication
- [ ] Analysis history
- [ ] Deployment
- [ ] Performance optimization
- [ ] Security improvements
- [ ] Mobile application

---

## Upcoming Demo

The next major milestone will introduce:

- Animated live analysis dashboard
- ATS score cards
- Match score visualization
- Skill comparison chips
- Resume preview
- Job description editor
- AI-powered recommendations
- Smooth dashboard transitions

A demonstration GIF showcasing the complete workflow—from dragging a resume into the upload area to receiving a fully animated analysis report—will be added after the dashboard milestone.

---

## Development Philosophy

This project is being developed using a **90% coding / 10% theory** approach.

Core principles:

- Build working features incrementally.
- Keep services modular.
- Write automated tests for every major feature.
- Maintain a clean Git history.
- Understand every piece of code before moving forward.
- Add AI only where it provides meaningful value.

The objective is not only to build a useful product but also to demonstrate full-stack engineering practices, clean architecture, and scalable software development.

---

## License

This project is currently under active development.

A production-ready open-source license will be added before the first public release.
