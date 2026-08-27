# AI Resume Analyzer

An intelligent full-stack resume analysis platform that compares resumes against job descriptions, identifies matching and missing skills, calculates ATS compatibility, and provides actionable recommendations.

The application is built with a **FastAPI backend**, **React + TypeScript frontend**, and **MongoDB Atlas** database. It currently provides resume upload, job description analysis, ATS scoring, skill matching, recommendations, persistent analysis history, and restoration of previous reports.

---

## Project Status

**MVP — Functional and Under Development**

The core full-stack application is working end-to-end.

### Current Status

* FastAPI backend: **Working**
* React frontend: **Working**
* MongoDB Atlas: **Connected**
* Resume upload: **Working**
* Resume parsing: **Working**
* Job description analysis: **Working**
* Resume/JD matching: **Working**
* Skill analysis: **Working**
* ATS scoring: **Working**
* Recommendations: **Working**
* Analysis persistence: **Working**
* Analysis history: **Working**
* Previous analysis restoration: **Working**
* Automated backend tests: **29 passing**
* Frontend production build: **Passing**
* AI/LLM integration: **Planned**
* Production deployment: **Next milestone**

---

## Features

### Resume Analysis

* Upload PDF, DOCX, or TXT resumes
* Extract resume text
* Clean and preprocess resume content
* Compare resume against a job description
* Calculate TF-IDF similarity
* Detect relevant technical skills
* Identify matched skills
* Identify missing skills
* Calculate ATS score
* Generate match grade
* Generate analysis summary
* Generate improvement recommendations

### Analysis History

Every completed analysis is stored in MongoDB.

Users can:

* View previous analyses
* See match and ATS scores
* View previous match grades
* Open previous analysis results
* Restore the previous resume analysis
* Restore the associated job description

Each analysis receives a unique MongoDB `analysis_id`.

### Frontend

* Modern dark interface
* Responsive design
* Glassmorphism-inspired UI
* Animated components
* Drag-and-drop resume upload
* Resume upload feedback
* Job description input
* Interactive analysis dashboard
* Match score display
* ATS score display
* Skill comparison
* Recommendations
* Analysis history

---

## Architecture

```text
                         AI RESUME ANALYZER

                              USER
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │  TypeScript + Vite  │
                    └──────────┬──────────┘
                               │
                         HTTP / Fetch
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      Resume Parser      Analysis Service   History API
             │                 │                 │
             ▼                 ▼                 ▼
      Text Processor      Match Engine     Repository Layer
                               │                 │
             ┌─────────────────┼─────────────────┘
             │                 │
             ▼                 ▼
       Skill Analyzer      ATS Analyzer
             │                 │
             └────────┬────────┘
                      ▼
              Recommendation Engine
                      │
                      ▼
                Analysis Result
                      │
                      ▼
                MongoDB Atlas
```

---

## Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* PyPDF
* python-docx
* scikit-learn
* PyMongo
* Pydantic
* pytest

### Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* Framer Motion
* Lucide React

### Database

* MongoDB Atlas
* MongoDB / PyMongo

### Development

* Git
* GitHub
* Visual Studio Code
* PowerShell

### AI — Planned

* LLM integration
* Semantic embeddings
* Semantic resume matching
* AI-powered resume analysis
* AI-generated improvement suggestions

---

## Project Structure

```text
ai-resume-analyzer/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   │       ├── analysis.py
│   │   │       ├── history.py
│   │   │       └── resume.py
│   │   │
│   │   ├── database/
│   │   │   ├── mongodb.py
│   │   │   └── analysis_repository.py
│   │   │
│   │   ├── schemas/
│   │   │   └── analysis.py
│   │   │
│   │   ├── services/
│   │   │   ├── analysis_service.py
│   │   │   ├── ats_analyzer.py
│   │   │   ├── jd_parser.py
│   │   │   ├── matcher.py
│   │   │   ├── recommendation_engine.py
│   │   │   ├── resume_parser.py
│   │   │   ├── score_interpreter.py
│   │   │   ├── skill_analyzer.py
│   │   │   └── text_processor.py
│   │   │
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── test_analysis_api.py
│   │   ├── test_analysis_service.py
│   │   ├── test_jd_parser.py
│   │   ├── test_matcher.py
│   │   ├── test_resume_parser.py
│   │   ├── test_score_interpreter.py
│   │   ├── test_skill_analyzer.py
│   │   └── test_text_processor.py
│   │
│   ├── test_mongodb.py
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── AnalysisDashboard.tsx
│   │   │   ├── AnalysisHistory.tsx
│   │   │   ├── JobDescriptionPanel.tsx
│   │   │   ├── ThinkingOverlay.tsx
│   │   │   └── UploadCard.tsx
│   │   │
│   │   ├── services/
│   │   │   └── api.ts
│   │   │
│   │   ├── types/
│   │   │   └── analysis.ts
│   │   │
│   │   └── App.tsx
│   │
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

---

## API Endpoints

### Health Check

```text
GET /health
```

Returns the backend health status.

### Resume Upload

```text
POST /api/resume/upload
```

Accepts:

* PDF
* DOCX
* TXT

Returns extracted resume text.

### Resume Analysis

```text
POST /api/analyze
```

Request:

```json
{
  "resume_text": "Resume content...",
  "job_description": "Job description..."
}
```

Response contains:

```json
{
  "analysis_id": "mongodb-object-id",
  "match_score": 68.5,
  "ats_score": 85,
  "grade": "Good Match",
  "summary": "Your resume has a strong overlap with the job description.",
  "matched_skills": [
    "Python",
    "FastAPI"
  ],
  "missing_skills": [
    "AWS"
  ],
  "resume_skills": [
    "Python",
    "FastAPI",
    "Git"
  ],
  "required_skills": [
    "Python",
    "FastAPI",
    "AWS"
  ],
  "recommendations": []
}
```

### Analysis History

```text
GET /api/history
```

Returns previously stored analyses from MongoDB.

---

## Scoring System

The current match score combines multiple signals.

### TF-IDF Similarity

Measures textual similarity between the resume and job description.

### Skill Overlap

Compares detected resume skills with the skills required by the job description.

### Keyword Bonus

A small bonus is applied when relevant required skills are detected.

### Current Weighted Formula

```text
Match Score =
    TF-IDF Score × 30%
    +
    Skill Overlap × 50%
    +
    Keyword Bonus
```

The final score is capped at `100`.

The score is then converted into a match grade and summary.

---

## Database

MongoDB Atlas stores completed analyses.

A stored analysis contains information such as:

```json
{
  "_id": "ObjectId",
  "resume_text": "...",
  "job_description": "...",
  "match_score": 68.5,
  "ats_score": 85,
  "grade": "Good Match",
  "summary": "...",
  "matched_skills": [],
  "missing_skills": [],
  "resume_skills": [],
  "required_skills": [],
  "recommendations": [],
  "created_at": "timestamp"
}
```

MongoDB is currently used for persistent analysis history.

---

## Backend Setup

Navigate to the backend:

```powershell
cd backend
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```env
MONGODB_URI=your_mongodb_connection_string
DATABASE_NAME=ai_resume_analyzer
```

Never commit `.env` or database credentials to GitHub.

### Start Backend

```powershell
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Frontend Setup

Navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Frontend:

```text
http://localhost:5173
```

### Production Build

```powershell
npm run build
```

The production build is generated in:

```text
frontend/dist/
```

---

## Testing

Backend tests are written using pytest.

Run:

```powershell
cd backend
python -m pytest
```

Current status:

```text
29 passed
```

The tests cover:

* Resume parsing
* Text processing
* Job description parsing
* Skill analysis
* Resume/JD matching
* ATS scoring
* Score interpretation
* Analysis service
* Analysis API

The MongoDB connection can also be tested with:

```powershell
python test_mongodb.py
```

Expected result:

```text
MongoDB connected successfully!
```

---

## Development Roadmap

### Phase 1 — Backend Foundation

* [x] Project setup
* [x] Git/GitHub setup
* [x] FastAPI setup
* [x] Resume parser
* [x] Resume upload API
* [x] PDF parsing
* [x] DOCX parsing
* [x] TXT parsing
* [x] Text preprocessing
* [x] Job description parser
* [x] TF-IDF matching
* [x] Skill analysis
* [x] ATS scoring
* [x] Match grading
* [x] Recommendation engine
* [x] Analysis API
* [x] Automated testing

### Phase 2 — Frontend Foundation

* [x] React + TypeScript
* [x] Vite
* [x] Tailwind CSS
* [x] Landing page
* [x] Responsive UI
* [x] Glassmorphism design
* [x] Framer Motion animations
* [x] Drag-and-drop resume upload
* [x] Backend integration
* [x] Job description input
* [x] Analysis dashboard
* [x] Score cards
* [x] Skill visualization
* [x] Recommendations

### Phase 3 — Database

* [x] MongoDB Atlas setup
* [x] MongoDB connection
* [x] Environment configuration
* [x] Analysis repository
* [x] Persistent analysis storage
* [x] Unique analysis IDs
* [x] Analysis history API
* [x] Frontend history
* [x] Previous analysis restoration

### Phase 4 — Production Readiness

* [ ] Environment-based frontend API URL
* [ ] Improved error handling
* [ ] New analysis/reset flow
* [ ] History refresh after new analysis
* [ ] Production backend configuration
* [ ] Production database configuration
* [ ] CORS production configuration
* [ ] Deployment

### Phase 5 — AI Features

* [ ] Semantic embeddings
* [ ] Semantic resume matching
* [ ] LLM integration
* [ ] AI resume insights
* [ ] AI-generated improvement suggestions
* [ ] Resume section analysis
* [ ] AI-powered resume rewriting

### Phase 6 — Advanced Features

* [ ] User authentication
* [ ] User-specific analysis history
* [ ] Resume management
* [ ] Multiple resume support
* [ ] Saved job descriptions
* [ ] Analysis analytics
* [ ] Shareable analysis reports
* [ ] PDF report generation
* [ ] Mobile application

---

## Security Notes

* MongoDB credentials must remain in environment variables.
* `.env` files should never be committed.
* Production CORS settings should use the deployed frontend domain.
* API secrets and LLM keys should be stored securely.
* Authentication should be implemented before exposing private user history in production.

---

## Current Milestone

**Full-Stack MVP + MongoDB Persistence**

The application can currently:

```text
Upload Resume
      ↓
Extract Resume Text
      ↓
Enter Job Description
      ↓
Analyze Resume
      ↓
Calculate Match Score
      ↓
Calculate ATS Score
      ↓
Analyze Skills
      ↓
Generate Recommendations
      ↓
Save Analysis to MongoDB
      ↓
Return Analysis ID
      ↓
View Analysis History
      ↓
Restore Previous Analysis
```

---

## Future Vision

The long-term goal is to turn the project into an intelligent career assistant rather than a simple resume checker.

The planned AI layer will combine resume parsing, job-description understanding, semantic matching, ATS optimization, and LLM-powered recommendations to help users understand exactly how well their resume fits a specific role and how they can improve it.

---

## License

This project is currently under development and intended for educational and portfolio purposes.
