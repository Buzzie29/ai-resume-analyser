import { Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import { useState, useRef } from "react";

import ThinkingOverlay from "./components/ThinkingOverlay";
import UploadCard from "./components/UploadCard";
import JobDescriptionPanel from "./components/JobDescriptionPanel";
import AnalysisDashboard from "./components/AnalysisDashboard";
import AnalysisHistory from "./components/AnalysisHistory";

import { analyzeResume } from "./services/api";
import type { AnalysisResult } from "./types/analysis";

export default function App() {
  const [jobDescription, setJobDescription] = useState("");
  const [resumeText, setResumeText] = useState("");
  const [fileName, setFileName] = useState("");
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [thinking, setThinking] = useState(false);

  const dashboardRef = useRef<HTMLDivElement>(null);

  async function handleAnalyze() {
    if (!resumeText || !jobDescription.trim()) return;

    setLoading(true);
    setThinking(true);

    try {
      const result = await analyzeResume(
        resumeText,
        jobDescription
      );

      await new Promise((resolve) =>
        setTimeout(resolve, 1800)
      );

      setAnalysis(result);
      setThinking(false);

      setTimeout(() => {
        dashboardRef.current?.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }, 200);
    } catch {
      alert("Analysis failed.");
      setThinking(false);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-purple-950 text-white">
      <ThinkingOverlay open={thinking} />

      <div className="mx-auto flex max-w-6xl flex-col items-center px-6 py-20 text-center">

        <motion.div
          initial={{ opacity: 0, y: -30 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <Sparkles className="mx-auto mb-4 h-12 w-12 text-cyan-400" />

          <h1 className="text-5xl font-bold">
            AI Resume Analyzer
          </h1>

          <p className="mt-4 max-w-2xl text-lg text-slate-300">
            Upload your resume, compare it with a job description,
            and receive an ATS score, skill analysis,
            and AI-powered insights.
          </p>
        </motion.div>

        <UploadCard
          onUploadSuccess={(text, name) => {
            setResumeText(text);
            setFileName(name);
          }}
        />

        <JobDescriptionPanel
          value={jobDescription}
          onChange={setJobDescription}
        />

        <button
          onClick={handleAnalyze}
          disabled={!resumeText || !jobDescription.trim() || loading}
          className="mt-10 rounded-xl bg-cyan-500 px-8 py-4 text-lg font-semibold text-black transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>

        {analysis && (
          <div ref={dashboardRef} className="w-full">
            <AnalysisDashboard
              result={analysis}
              fileName={fileName}
              resumeText={resumeText}
            />
          </div>
        )}

        <AnalysisHistory
          onSelect={(item) => {
            setAnalysis(item);
            setResumeText(item.resume_text);
            setJobDescription(item.job_description);
            setFileName("Previous Resume");

            setTimeout(() => {
              dashboardRef.current?.scrollIntoView({
                behavior: "smooth",
                block: "start",
              });
            }, 200);
          }}
        />

      </div>
    </div>
  );
}
