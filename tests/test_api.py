
import sys
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from main import app

client = TestClient(app)


class TestBhashaStudyAPI(unittest.TestCase):

    def test_health_endpoint(self):
        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_rejects_unsupported_language(self):
        response = client.post(
            "/api/transcribe",
            data={"language": "xx-XX"},
            files={
                "file": (
                    "sample.m4a",
                    b"fake audio data",
                    "audio/x-m4a",
                )
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "Unsupported language code: xx-XX",
        )

    def test_rejects_pdf_upload(self):
        response = client.post(
            "/api/transcribe",
            files={
                "file": (
                    "document.pdf",
                    b"%PDF-test",
                    "application/pdf",
                )
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "Unsupported audio format.",
        )

    def test_rejects_empty_audio(self):
        response = client.post(
            "/api/transcribe",
            files={
                "file": (
                    "empty.m4a",
                    b"",
                    "audio/x-m4a",
                )
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()["detail"],
            "Audio file is empty.",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
