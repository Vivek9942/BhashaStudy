
const form = document.getElementById("transcription-form");
const audioInput = document.getElementById("audio-file");
const fileName = document.getElementById("file-name");
const languageSelect = document.getElementById("language");
const transcribeButton = document.getElementById("transcribe-button");
const message = document.getElementById("message");
const resultSection = document.getElementById("result-section");
const transcriptElement = document.getElementById("transcript");
const copyButton = document.getElementById("copy-button");

const API_URL = "https://bhashastudy.onrender.com/api/transcribe";
const MAX_FILE_SIZE = 10 * 1024 * 1024;

const allowedExtensions = [".m4a", ".wav", ".mp3", ".flac", ".ogg"];

audioInput.addEventListener("change", () => {
    const file = audioInput.files[0];

    fileName.textContent = file ? file.name : "No file selected";
    message.textContent = "";
    message.className = "message";
    resultSection.hidden = true;
});

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const file = audioInput.files[0];

    if (!file) {
        showMessage("Please choose an audio file first.", "error");
        return;
    }

    const extension = "." + file.name.split(".").pop().toLowerCase();

    if (!allowedExtensions.includes(extension)) {
        showMessage("Please select a supported audio file.", "error");
        return;
    }

    if (file.size === 0) {
        showMessage("The selected audio file is empty.", "error");
        return;
    }

    if (file.size > MAX_FILE_SIZE) {
        showMessage("The file exceeds the 10 MB limit.", "error");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("language", languageSelect.value);

    transcribeButton.disabled = true;
    transcribeButton.textContent = "Transcribing...";
    resultSection.hidden = true;
    showMessage("Uploading audio and generating your transcript...", "");

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            body: formData,
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
            throw new Error(
                data.detail || `Request failed (${response.status}).`
            );
        }

        transcriptElement.textContent = data.transcript || "";
        resultSection.hidden = false;
        showMessage("Transcription completed successfully.", "success");
    } catch (error) {
        showMessage(
            error.message.includes("Failed to fetch")
                ? "Cannot connect to BhashaStudy. Make sure the backend is running."
                : error.message,
            "error"
        );
    } finally {
        transcribeButton.disabled = false;
        transcribeButton.innerHTML =
            'Transcribe audio <span aria-hidden="true">→</span>';
    }
});

copyButton.addEventListener("click", async () => {
    try {
        await navigator.clipboard.writeText(transcriptElement.textContent);
        showMessage("Transcript copied to clipboard.", "success");
    } catch {
        showMessage(
            "Copy was blocked by the browser. Select the transcript and copy it manually.",
            "error"
        );
    }
});

function showMessage(text, type) {
    message.textContent = text;
    message.className = type ? `message ${type}` : "message";
}
