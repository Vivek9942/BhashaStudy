
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_URL = "https://api.vachana.ai/stt/v3"


def transcribe_audio(
    audio_path: str | Path,
    language_code: str = "hi-IN",
) -> dict:
    """Transcribe an audio file using the Gnani STT API."""

    api_key = os.getenv("GNANI_API_KEY")
    if not api_key:
        raise RuntimeError("GNANI_API_KEY is missing from .env")

    audio_path = Path(audio_path)
    if not audio_path.is_file():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    payload = {
        "language_code": language_code,
        "preferred_language": language_code,
        "format": "transcribe",
        "itn_native_numerals": "true",
    }

    headers = {"X-API-Key-ID": api_key}

    try:
        with audio_path.open("rb") as audio:
            files = {
                "audio_file": (audio_path.name, audio)
            }
            response = requests.post(
                API_URL,
                data=payload,
                files=files,
                headers=headers,
                timeout=60,
            )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as exc:
        if exc.response is not None:
            detail = exc.response.text[:1000]
            raise RuntimeError(
                f"Gnani STT request failed: "
                f"HTTP {exc.response.status_code}: {detail}"
            ) from exc

        raise RuntimeError(
            f"Could not connect to Gnani STT: {exc}"
        ) from exc
