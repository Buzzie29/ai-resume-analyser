import { motion } from "framer-motion";

interface SkillChipProps {
    skill: string;
    delay?: number;
    color?: "green" | "red";
}

export default function SkillChip({
    skill,
    delay = 0,
    color = "green",
}: SkillChipProps) {
    const styles =
        color === "green"
            ? "bg-green-500/20 text-green-300 border-green-400/20"
            : "bg-red-500/20 text-red-300 border-red-400/20";

    return (
        <motion.span
            initial={{
                opacity: 0,
                y: 30,
                scale: 0.5,
            }}
            animate={{
                opacity: 1,
                y: 0,
                scale: 1,
            }}
            transition={{
                delay,
                duration: 0.4,
                type: "spring",
            }}
            whileHover={{
                scale: 1.08,
                y: -2,
            }}
            className={`rounded-full border px-3 py-1 text-sm ${styles}`}
        >
            {skill}
        </motion.span>
    );
}
