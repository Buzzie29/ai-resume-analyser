from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.resume import router as resume_router
from app.api.routes.analysis import router as analysis_router
from app.api.routes.history import router as history_router

app = FastAPI(
    title="AI Resume Analyzer",
    description="Resume and Job Description Analysis API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume_router)
app.include_router(analysis_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {"message": "AI Resume Analyzer API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
