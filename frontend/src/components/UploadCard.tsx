import { useState } from "react";
import { Upload, FileText, CheckCircle } from "lucide-react";
import { motion } from "framer-motion";
import { uploadResume } from "../services/api";

export default function UploadCard() {
    const [dragging, setDragging] = useState(false);
    const [fileName, setFileName] = useState("");
    const [uploading, setUploading] = useState(false);
    const [success, setSuccess] = useState(false);

    async function handleFile(file: File) {
        setUploading(true);
        setSuccess(false);

        try {
            await uploadResume(file);
            setFileName(file.name);
            setSuccess(true);
        } catch {
            alert("Upload failed.");
        } finally {
            setUploading(false);
        }
    }

    return (
        <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            onDragOver={(e) => {
                e.preventDefault();
                setDragging(true);
            }}
            onDragLeave={() => setDragging(false)}
            onDrop={(e) => {
                e.preventDefault();
                setDragging(false);

                if (e.dataTransfer.files.length) {
                    handleFile(e.dataTransfer.files[0]);
                }
            }}
            className={`mt-16 w-full max-w-2xl rounded-3xl border p-10 backdrop-blur transition ${dragging
                    ? "border-cyan-400 bg-cyan-500/10"
                    : "border-slate-700 bg-slate-900/50"
                }`}
        >
            {success ? (
                <CheckCircle className="mx-auto mb-4 h-12 w-12 text-green-400" />
            ) : (
                <Upload className="mx-auto mb-4 h-12 w-12 text-cyan-400" />
            )}

            <h2 className="text-center text-2xl font-semibold">
                {success ? "Resume Uploaded!" : "Upload Your Resume"}
            </h2>

            <p className="mt-2 text-center text-slate-400">
                {fileName || "Drag & drop your resume or choose a file."}
            </p>

            <label className="mt-8 block cursor-pointer rounded-xl bg-cyan-500 px-6 py-3 text-center font-semibold text-black transition hover:bg-cyan-400">
                {uploading ? "Uploading..." : "Choose Resume"}

                <input
                    type="file"
                    accept=".pdf,.docx,.txt"
                    className="hidden"
                    onChange={(e) => {
                        const file = e.target.files?.[0];
                        if (file) handleFile(file);
                    }}
                />
            </label>

            <div className="mt-8 flex justify-center gap-6 text-slate-400">
                {["PDF", "DOCX", "TXT"].map((type) => (
                    <div key={type} className="flex items-center gap-2">
                        <FileText size={18} />
                        {type}
                    </div>
                ))}
            </div>
        </motion.div>
    );
}
