import { AnimatePresence, motion } from "framer-motion";
import { Sparkles } from "lucide-react";

interface Props {
    open: boolean;
}

const skills = [
    "Python",
    "FastAPI",
    "Git",
    "PostgreSQL",
    "Docker",
];

export default function ThinkingOverlay({ open }: Props) {
    return (
        <AnimatePresence>
            {open && (
                <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/85 backdrop-blur-md"
                >
                    <div className="relative w-[340px]">
                        <motion.div
                            initial={{ scale: 0.92, y: 30 }}
                            animate={{ scale: 1, y: 0 }}
                            className="relative overflow-hidden rounded-3xl border border-cyan-500/30 bg-slate-900 p-8 shadow-[0_0_40px_rgba(34,211,238,0.15)]"
                        >
                            <div className="mb-6 flex items-center gap-3">
                                <motion.div
                                    animate={{ rotate: 360 }}
                                    transition={{
                                        repeat: Infinity,
                                        duration: 2,
                                        ease: "linear",
                                    }}
                                >
                                    <Sparkles
                                        className="text-cyan-400"
                                        size={28}
                                    />
                                </motion.div>

                                <div>
                                    <h2 className="font-bold text-white">
                                        AI Resume Scan
                                    </h2>

                                    <p className="text-sm text-slate-400">
                                        Analyzing your profile...
                                    </p>
                                </div>
                            </div>

                            <div className="relative rounded-xl border border-slate-700 bg-slate-950 p-5">
                                <div className="space-y-3">
                                    {[1, 2, 3, 4, 5, 6].map((i) => (
                                        <div
                                            key={i}
                                            className="h-2 rounded bg-slate-700"
                                            style={{ width: `${70 + i * 4}%` }}
                                        />
                                    ))}
                                </div>

                                <motion.div
                                    initial={{ y: -120 }}
                                    animate={{ y: 230 }}
                                    transition={{
                                        duration: 1.6,
                                        repeat: Infinity,
                                        ease: "linear",
                                    }}
                                    className="absolute left-0 right-0 h-10 bg-gradient-to-b from-transparent via-cyan-400/40 to-transparent"
                                />
                            </div>

                            <div className="mt-6 flex flex-wrap gap-2">
                                {skills.map((skill, i) => (
                                    <motion.span
                                        key={skill}
                                        initial={{
                                            opacity: 0,
                                            scale: 0.7,
                                        }}
                                        animate={{
                                            opacity: [0, 1, 1],
                                            scale: [0.7, 1.08, 1],
                                        }}
                                        transition={{
                                            delay: i * 0.22,
                                            duration: 0.5,
                                            repeat: Infinity,
                                            repeatDelay: 1.2,
                                        }}
                                        className="rounded-full border border-cyan-400/40 bg-cyan-500/10 px-3 py-1 text-sm text-cyan-300"
                                    >
                                        {skill}
                                    </motion.span>
                                ))}
                            </div>

                            <motion.div
                                animate={{
                                    opacity: [0.3, 1, 0.3],
                                }}
                                transition={{
                                    repeat: Infinity,
                                    duration: 1.2,
                                }}
                                className="mt-6 text-center text-sm text-slate-300"
                            >
                                Detecting skills...
                            </motion.div>
                        </motion.div>

                        {[...Array(14)].map((_, i) => (
                            <motion.div
                                key={i}
                                initial={{
                                    x: Math.random() * 240 - 120,
                                    y: 80,
                                    opacity: 0,
                                }}
                                animate={{
                                    y: -140,
                                    opacity: [0, 1, 0],
                                }}
                                transition={{
                                    repeat: Infinity,
                                    duration: 1.8 + Math.random(),
                                    delay: i * 0.08,
                                }}
                                className="absolute left-1/2 h-1 w-1 rounded-full bg-cyan-300"
                            />
                        ))}
                    </div>
                </motion.div>
            )}
        </AnimatePresence>
    );
}
