import { motion } from "framer-motion";
import {
    Lightbulb,
    Rocket,
    ShieldCheck,
} from "lucide-react";

interface Props {
    title: string;
    message: string;
    type: string;
}

export default function RecommendationCard({
    title,
    message,
    type,
}: Props) {
    const icon =
        type === "skill"
            ? <Lightbulb className="text-cyan-400" />
            : type === "ats"
                ? <ShieldCheck className="text-green-400" />
                : <Rocket className="text-purple-400" />;

    return (
        <motion.div
            whileHover={{
                y: -6,
                scale: 1.02,
            }}
            className="rounded-3xl border border-slate-700 bg-slate-900/50 p-6 backdrop-blur"
        >
            <div className="mb-3 flex items-center gap-3">
                {icon}

                <h4 className="text-lg font-semibold">
                    {title}
                </h4>
            </div>

            <p className="text-slate-300">
                {message}
            </p>
        </motion.div>
    );
}
