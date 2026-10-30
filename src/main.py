
from pathlib import Path
import sys
import tempfile

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from gnani_stt import transcribe_audio

app = FastAPI(
    title="BhashaStudy API",
    description="Voice-first multilingual study assistant",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "https://bhashastudy-frontend.onrender.com",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

ALLOWED_EXTENSIONS = {".m4a", ".wav", ".mp3", ".flac", ".ogg"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


SUPPORTED_LANGUAGES = {
    "hi-IN",
    "en-IN",
    "ta-IN",
    "te-IN",
    "kn-IN",
    "bn-IN",
    "mr-IN",
    "gu-IN",
    "ml-IN",
    "pa-IN",
    "ur-IN",
}



@app.get("/")
def home():
    return {"message": "Welcome to BhashaStudy API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    language: str = Form("hi-IN"),
):
    if language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported language code: {language}",
        )
    extension = Path(file.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio format.",
        )

    content = await file.read(MAX_FILE_SIZE + 1)

    if not content:
        raise HTTPException(status_code=400, detail="Audio file is empty.")

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Audio file exceeds the 10 MB limit.",
        )

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=extension, delete=False
        ) as temp:
            temp.write(content)
            temp_path = Path(temp.name)

        result = transcribe_audio(temp_path, language_code=language)

        if result.get("success") is False:
            raise HTTPException(
                status_code=502,
                detail="Speech recognition failed.",
            )

        return {
            "success": True,
            "transcript": result.get("transcript", ""),
        }

    except HTTPException:
        raise
    except (RuntimeError, FileNotFoundError) as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
