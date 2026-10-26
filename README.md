# BhashaStudy — Learn in Your Language

**A multilingual, voice-based study assistant powered by Gnani AI speech-to-text technology.**

BhashaStudy aims to make learning more accessible by allowing users to upload spoken audio and convert it into readable text in their chosen language.

## Features

- **Multilingual transcription:** Select a language before transcribing audio.
- **Gnani AI integration:** Uses the Gnani AI speech-to-text API.
- **Audio uploads:** Supports M4A, WAV, MP3, FLAC, and OGG files.
- **Transcript display:** View the generated transcript in a clean interface.
- **Copy to clipboard:** Copy transcribed text for notes and study material.
- **Input validation:** Checks file format, file size, empty uploads, and supported language codes.
- **REST API:** FastAPI backend with interactive API documentation.
- **Automated tests:** Tests for API health, invalid uploads, and language validation.

## Supported Languages

The current interface offers these language options:

| Language | Code |
|---|---|
| Hindi | `hi-IN` |
| English (India) | `en-IN` |
| Tamil | `ta-IN` |
| Telugu | `te-IN` |
| Kannada | `kn-IN` |
| Bengali | `bn-IN` |
| Marathi | `mr-IN` |
| Gujarati | `gu-IN` |
| Malayalam | `ml-IN` |
| Punjabi | `pa-IN` |
| Urdu | `ur-IN` |

Language availability and transcription quality depend on Gnani AI's support for the configured API account. Hindi, English, and Tamil have been tested successfully.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI, Uvicorn
- **Speech recognition:** Gnani AI STT API
- **Configuration:** Environment variables with `python-dotenv`
- **Testing:** Python `unittest`, FastAPI `TestClient`

## Project Structure

```text
BhashaStudy/
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── src/
│   ├── main.py
│   └── gnani_stt.py
├── tests/
│   ├── test_api.py
│   ├── test_stt.py
│   └── test_stt_unit.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone <https://github.com/Vivek9942>
cd BhashaStudy
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```text
GNANI_API_KEY=your_gnani_api_key_here
```

Replace the placeholder with your own API key. **Never commit your actual API key to GitHub.**

Ensure `.env` is listed in `.gitignore`.

### 5. Start the backend

From the project root, run:

```powershell
python -m uvicorn main:app --app-dir src --reload
```

The backend will run at:

- API: `http://127.0.0.1:8000`
- Interactive API documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

### 6. Start the frontend

Open `frontend/index.html` using the VS Code Live Server extension.

The frontend currently expects the backend at:

`http://127.0.0.1:8000`

Keep the backend terminal running while using the frontend.

## Running Tests

Run the automated tests from the project root:

```powershell
python -m unittest discover -s tests -v
```

Run only the API tests:

```powershell
python -m unittest discover -s tests -p "test_api.py" -v
```

Run the STT unit tests:

```powershell
python -m unittest discover -s tests -p "test_stt_unit.py" -v
```

The live STT test in `tests/test_stt.py` sends an audio file to Gnani AI and may consume API credits.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| POST | `/api/transcribe` | Transcribe an uploaded audio file |

The transcription endpoint accepts an audio file and a language code as multipart form data.

## Current Status

- Frontend and backend integration: working locally
- Gnani AI speech-to-text integration: tested successfully
- Hindi, English, and Tamil transcription: tested successfully
- File and language validation: implemented
- Automated API and unit tests: passing

## Future Improvements

- Expand language testing and improve language-specific error handling.
- Add study-note generation and transcript summarization.
- Allow users to save and organize transcripts.
- Improve accessibility and mobile responsiveness.
- Deploy the application for public access.

## Security

- Keep API keys in environment variables.
- Do not commit `.env`, credentials, or private configuration.
- Review file-size limits and API usage before deploying publicly.

## About

BhashaStudy is being developed for the **Gnani AI Great Indian AI Internship Challenge 2026**. Its goal is to make voice-based learning more accessible across languages.

*Built with Python, FastAPI, JavaScript, and Gnani AI.*
