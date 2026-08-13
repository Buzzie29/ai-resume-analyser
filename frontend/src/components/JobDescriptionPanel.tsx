import { FileSearch } from "lucide-react";

interface JobDescriptionPanelProps {
    value: string;
    onChange: (value: string) => void;
}

export default function JobDescriptionPanel({
    value,
    onChange,
}: JobDescriptionPanelProps) {
    const characters = value.length;

    return (
        <div className="mt-10 w-full max-w-2xl rounded-3xl border border-slate-700 bg-slate-900/50 p-8 backdrop-blur">
            <div className="mb-4 flex items-center gap-3">
                <FileSearch className="h-7 w-7 text-cyan-400" />
                <h2 className="text-2xl font-semibold">
                    Job Description
                </h2>
            </div>

            <p className="mb-4 text-slate-400">
                Paste the job description you want to compare against your resume.
            </p>

            <textarea
                value={value}
                onChange={(e) => onChange(e.target.value)}
                placeholder="Paste the complete job description here..."
                className="h-56 w-full resize-none rounded-xl border border-slate-600 bg-slate-950/70 p-4 text-white outline-none transition focus:border-cyan-400"
            />

            <div className="mt-3 flex justify-between text-sm text-slate-400">
                <span>Supports long job descriptions</span>
                <span>{characters} characters</span>
            </div>
        </div>
    );
}
