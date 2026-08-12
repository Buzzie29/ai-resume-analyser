from fastapi import FastAPI

from app.api.routes.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer",
    description="Resume and Job Description Analysis API",
    version="1.0.0",
)


app.include_router(resume_router)


@app.get("/")
def root():
    return {"message": "AI Resume Analyzer API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
