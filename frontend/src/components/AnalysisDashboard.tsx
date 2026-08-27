import CircularScore from "./CircularScore";
import { motion } from "framer-motion";
import SkillChip from "./SkillChip";
import ResumeSnapshot from "./ResumeSnapshot";
import {
    CheckCircle,
    CircleAlert,
} from "lucide-react";

import RecommendationCard from "./RecommendationCard";

import type { AnalysisResult } from "../types/analysis";

interface Props {
    result: AnalysisResult;
    fileName: string;
    resumeText: string;
}

export default function AnalysisDashboard({
    result,
    fileName,
    resumeText,
}: Props) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 40 }}
            animate={{ opacity: 1, y: 0 }}
            className="mt-12 w-full max-w-5xl"
        >
            <div className="grid gap-6 md:grid-cols-2">
                <motion.div
                    whileHover={{ scale: 1.03 }}
                    className="rounded-3xl border border-cyan-400/40 bg-slate-900/50 p-8 backdrop-blur"
                >
                    <CircularScore
                        value={Number(result.match_score.toFixed(0))}
                        label="Match Score"
                        color="#22d3ee"
                    />
                </motion.div>

                <motion.div
                    whileHover={{ scale: 1.03 }}
                    className="rounded-3xl border border-green-400/40 bg-slate-900/50 p-8 backdrop-blur"
                >
                    <CircularScore
                        value={result.ats_score}
                        label="ATS Score"
                        color="#22c55e"
                    />
                </motion.div>
            </div>

            <div className="mt-6 grid gap-6 lg:grid-cols-2">
                <div className="rounded-3xl border border-slate-700 bg-slate-900/50 p-6 backdrop-blur">
                    <h3 className="text-xl font-semibold text-cyan-300">
                        {result.grade}
                    </h3>

                    <p className="mt-3 text-slate-300">
                        {result.summary}
                    </p>
                </div>

                <ResumeSnapshot
                    fileName={fileName}
                    resumeText={resumeText}
                    skills={result.resume_skills}
                />
            </div>

            <div className="mt-6 grid gap-6 md:grid-cols-2">
                <SkillCard
                    title="Matched Skills"
                    icon={<CheckCircle className="text-green-400" />}
                    skills={result.matched_skills}
                    chip="bg-green-500/20 text-green-300"
                />

                <SkillCard
                    title="Missing Skills"
                    icon={<CircleAlert className="text-red-400" />}
                    skills={result.missing_skills}
                    chip="bg-red-500/20 text-red-300"
                />
            </div>
            <div className="mt-8">
                <h3 className="mb-4 text-2xl font-semibold text-cyan-300">
                    AI Recommendations
                </h3>

                <div className="grid gap-4 md:grid-cols-2">
                    {(result.recommendations ?? []).map((rec, index) => (
                        <RecommendationCard
                            key={index}
                            title={rec.title}
                            message={rec.message}
                            type={rec.type}
                        />
                    ))}
                </div>
            </div>
        </motion.div>

    );
}

interface SkillCardProps {
    title: string;
    skills: string[];
    icon: React.ReactNode;
    chip: string;
}

function SkillCard({
    title,
    skills,
    icon,
}: SkillCardProps) {
    return (
        <div className="rounded-3xl border border-slate-700 bg-slate-900/50 p-6 backdrop-blur">
            <div className="mb-4 flex items-center gap-2 text-lg font-semibold">
                {icon}
                {title}
            </div>

            <div className="flex flex-wrap gap-2">
                {skills.map((skill, index) => (
                    <SkillChip
                        key={skill}
                        skill={skill}
                        delay={index * 0.12}
                        color="green"
                    />
                ))}
            </div>
        </div>
    );
}
