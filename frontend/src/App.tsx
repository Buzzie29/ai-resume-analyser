import { Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import UploadCard from "./components/UploadCard";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-purple-950 text-white">
      <div className="mx-auto flex max-w-6xl flex-col items-center px-6 py-20 text-center">
        <motion.div
          initial={{ opacity: 0, y: -30 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <Sparkles className="mx-auto mb-4 h-12 w-12 text-cyan-400" />

          <h1 className="text-5xl font-bold">AI Resume Analyzer</h1>

          <p className="mt-4 max-w-2xl text-lg text-slate-300">
            Upload your resume, compare it with a job description, and receive
            an ATS score, skill analysis, and AI-powered insights.
          </p>
        </motion.div>

        <UploadCard />
      </div>
    </div>
  );
}
