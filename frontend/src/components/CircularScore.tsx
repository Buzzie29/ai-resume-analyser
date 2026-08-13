import { motion, animate } from "framer-motion";
import { useEffect, useState } from "react";

interface CircularScoreProps {
    value: number;
    label: string;
    color?: string;
}

export default function CircularScore({
    value,
    label,
    color = "#22d3ee",
}: CircularScoreProps) {
    const radius = 54;
    const stroke = 8;
    const normalizedRadius = radius - stroke / 2;
    const circumference = normalizedRadius * 2 * Math.PI;

    const offset = circumference - (value / 100) * circumference;

    const [displayValue, setDisplayValue] = useState(0);

    useEffect(() => {
        const controls = animate(0, value, {
            duration: 1.3,
            onUpdate(latest) {
                setDisplayValue(Math.round(latest));
            },
        });

        return () => controls.stop();
    }, [value]);

    return (
        <div className="flex flex-col items-center">
            <svg width="120" height="120" className="-rotate-90">
                <circle
                    cx="60"
                    cy="60"
                    r={normalizedRadius}
                    stroke="#334155"
                    strokeWidth={stroke}
                    fill="transparent"
                />

                <motion.circle
                    cx="60"
                    cy="60"
                    r={normalizedRadius}
                    stroke={color}
                    strokeWidth={stroke}
                    fill="transparent"
                    strokeLinecap="round"
                    initial={{ strokeDashoffset: circumference }}
                    animate={{ strokeDashoffset: offset }}
                    transition={{ duration: 1.2 }}
                    strokeDasharray={`${circumference} ${circumference}`}
                />
            </svg>

            <div className="-mt-20 text-center">
                <div className="text-3xl font-bold">
                    {displayValue}%
                </div>

                <div className="mt-1 text-sm text-slate-400">
                    {label}
                </div>
            </div>
        </div>
    );
}
