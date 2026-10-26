
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from gnani_stt import transcribe_audio


class TestTranscribeAudio(unittest.TestCase):

        def test_api_http_error(self):
            with patch.dict(
                os.environ, {"GNANI_API_KEY": "unit-test-placeholder"}
            ):
                mock_response = Mock()
                mock_response.status_code = 401
                mock_response.text = "Unauthorized"
                mock_response.raise_for_status.side_effect = (
                    __import__("requests").exceptions.HTTPError(
                        response=mock_response
                    )
                )

                with patch("gnani_stt.requests.post", return_value=mock_response):
                    with self.assertRaisesRegex(
                        RuntimeError, "HTTP 401"
                    ):
                        transcribe_audio(PROJECT_ROOT / "sample.m4a")

        def test_missing_api_key(self):
            with patch.dict(os.environ, {}, clear=True):
                with self.assertRaisesRegex(
                    RuntimeError, "GNANI_API_KEY is missing"
                ):
                    transcribe_audio(PROJECT_ROOT / "sample.m4a")

        def test_missing_audio_file(self):
            with patch.dict(
                os.environ, {"GNANI_API_KEY": "unit-test-placeholder"}
            ):
                missing_file = PROJECT_ROOT / "does_not_exist.m4a"

                with self.assertRaisesRegex(
                    FileNotFoundError, "Audio file not found"
                ):
                    transcribe_audio(missing_file)


if __name__ == "__main__":
    unittest.main(verbosity=2)
