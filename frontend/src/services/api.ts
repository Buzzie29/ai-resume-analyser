const API_BASE = "http://127.0.0.1:8000";

export async function uploadResume(file: File) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_BASE}/api/resume/upload`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Upload failed");
    }

    return response.json();
}

export async function analyzeResume(
    resumeText: string,
    jobDescription: string
) {
    const response = await fetch(`${API_BASE}/api/analyze`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            resume_text: resumeText,
            job_description: jobDescription,
        }),
    });

    if (!response.ok) {
        throw new Error("Analysis failed");
    }

    return response.json();
}
