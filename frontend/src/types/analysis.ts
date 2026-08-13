export interface AnalysisResult {
    match_score: number;
    ats_score: number;
    grade: string;
    summary: string;
    matched_skills: string[];
    missing_skills: string[];
    resume_skills: string[];
    required_skills: string[];
}
