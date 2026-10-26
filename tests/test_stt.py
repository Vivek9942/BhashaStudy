
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from gnani_stt import transcribe_audio

AUDIO_FILE = PROJECT_ROOT / "sample.m4a"

print("Sending audio to Gnani AI...")

try:
    result = transcribe_audio(AUDIO_FILE)

    print("API success:", result.get("success"))
    print("Transcript:", result.get("transcript", ""))

except (RuntimeError, FileNotFoundError) as exc:
    print("STT test failed:", exc)
