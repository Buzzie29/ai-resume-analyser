import { FileText, Clock, Sparkles } from "lucide-react";
import { motion } from "framer-motion";

interface Props {
    fileName: string;
    resumeText: string;
    skills: string[];
}

export default function ResumeSnapshot({
    fileName,
    resumeText,
    skills,
}: Props) {
    const wordCount = resumeText
        .trim()
        .split(/\s+/)
        .filter(Boolean).length;

    return (
        <motion.div
            whileHover={{ scale: 1.02 }}
            className="rounded-3xl border border-slate-700 bg-slate-900/50 p-6 backdrop-blur"
        >
            <div className="mb-4 flex items-center gap-3">
                <FileText className="text-cyan-400" />

                <div>
                    <h3 className="font-semibold text-white">
                        Resume Snapshot
                    </h3>

                    <p className="text-sm text-slate-400">
                        {fileName}
                    </p> 
                </div>
            </div>

            <div className="mb-6 grid grid-cols-3 gap-3 text-center">
                <Stat value={wordCount} label="Words" />
                <Stat value={skills.length} label="Skills" />
                <Stat value="Now" label="Uploaded" />
            </div>

            <div>
                <div className="mb-3 flex items-center gap-2 text-sm text-slate-300">
                    <Sparkles size={16} className="text-cyan-400" />
                    Detected Skills
                </div>

                <div className="flex flex-wrap gap-2">
                    {skills.map((skill) => (
                        <span
                            key={skill}
                            className="rounded-full border border-cyan-400/30 bg-cyan-500/10 px-3 py-1 text-sm text-cyan-300"
                        >
                            {skill}
                        </span>
                    ))}
                </div>
            </div>

            <div className="mt-5 flex items-center gap-2 text-xs text-slate-400">
                <Clock size={14} />
                Uploaded moments ago
            </div>
        </motion.div>
    );
}

function Stat({
    value,
    label,
}: {
    value: string | number;
    label: string;
}) {
    return (
        <div className="rounded-xl bg-slate-800/60 p-3">
            <div className="text-xl font-bold text-white">
                {value}
            </div>

            <div className="text-xs text-slate-400">
                {label}
            </div>
        </div>
    );
}
