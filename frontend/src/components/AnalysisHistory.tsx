import { useEffect, useState } from "react";
import { Clock3, ChevronRight } from "lucide-react";
import { motion } from "framer-motion";
import { getHistory } from "../services/api";

interface HistoryItem {
    id: string;
    resume_text: string;
    job_description: string;
    match_score: number;
    ats_score: number;
    grade: string;
    summary: string;
    matched_skills: string[];
    missing_skills: string[];
    resume_skills: string[];
    required_skills: string[];
    recommendations: {
        title: string;
        message: string;
        type: string;
    }[];
    created_at: string;
}

interface AnalysisHistoryProps {
    onSelect: (analysis: HistoryItem) => void;
}

export default function AnalysisHistory({
    onSelect,
}: AnalysisHistoryProps) {
    const [history, setHistory] = useState<HistoryItem[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadHistory() {
            try {
                const data = await getHistory();
                setHistory(data);
            } catch {
                console.error("Failed to load analysis history");
            } finally {
                setLoading(false);
            }
        }

        loadHistory();
    }, []);

    if (loading) {
        return (
            <div className="mt-20 text-slate-400">
                Loading analysis history...
            </div>
        );
    }

    if (!history.length) {
        return (
            <div className="mt-20 rounded-2xl border border-slate-700 bg-slate-900/40 p-8">
                <Clock3 className="mx-auto mb-3 h-8 w-8 text-slate-500" />
                <p className="text-slate-400">
                    No previous analyses yet.
                </p>
            </div>
        );
    }

    return (
        <section className="mt-20 w-full max-w-4xl text-left">
            <div className="mb-6 flex items-center gap-3">
                <Clock3 className="h-6 w-6 text-cyan-400" />

                <h2 className="text-2xl font-semibold">
                    Analysis History
                </h2>
            </div>

            <div className="space-y-4">
                {history.map((item, index) => (
                    <motion.button
                        key={item.id}
                        initial={{ opacity: 0, y: 15 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: index * 0.05 }}
                        onClick={() => onSelect(item)}
                        className="w-full rounded-2xl border border-slate-700 bg-slate-900/50 p-6 text-left backdrop-blur transition hover:border-cyan-400/50 hover:bg-slate-900/80"
                    >
                        <div className="flex items-center justify-between gap-4">
                            <div>
                                <p className="text-lg font-semibold">
                                    {item.grade}
                                </p>

                                <p className="mt-1 text-sm text-slate-400">
                                    {new Date(
                                        item.created_at
                                    ).toLocaleString()}
                                </p>
                            </div>

                            <ChevronRight className="h-5 w-5 text-slate-500" />
                        </div>

                        <div className="mt-5 flex gap-8">
                            <div>
                                <p className="text-sm text-slate-400">
                                    Match
                                </p>
                                <p className="text-2xl font-bold text-cyan-400">
                                    {item.match_score}%
                                </p>
                            </div>

                            <div>
                                <p className="text-sm text-slate-400">
                                    ATS
                                </p>
                                <p className="text-2xl font-bold">
                                    {item.ats_score}%
                                </p>
                            </div>
                        </div>
                    </motion.button>
                ))}
            </div>
        </section>
    );
}
