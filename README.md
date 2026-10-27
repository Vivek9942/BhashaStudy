# BhashaStudy — Learn in Your Language

A multilingual, voice-based study assistant powered by Gnani AI speech-to-text technology.

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
├── .gitignore
├── requirements.txt
└── README.md
```

The `.env` file and virtual environment are created locally and are intentionally excluded from version control.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Vivek9942/BhashaStudy.git
cd BhashaStudy
```

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

### 4. Configure the Gnani AI API key

Create a `.env` file in the project root:

```text
GNANI_API_KEY=your_gnani_api_key_here
```

Replace the placeholder with your own API key.

**Security:** Never commit your actual API key to GitHub. Keep `.env` listed in `.gitignore`, and configure the key as an environment variable in your hosting platform when deploying.

### 5. Start the backend locally

From the project root, run:

```powershell
python -m uvicorn main:app --app-dir src --reload
```

The backend will run at:

- **API:** http://127.0.0.1:8000
- **Interactive API documentation:** http://127.0.0.1:8000/docs
- **Health check:** http://127.0.0.1:8000/health

Keep the backend terminal running while using the application.

### 6. Start the frontend locally

Open `frontend/index.html` using the VS Code Live Server extension.

The frontend currently expects the backend at:

```text
http://127.0.0.1:8000
```

Make sure the backend is running before testing transcription from the frontend.

## Deployment

BhashaStudy's backend can be deployed to a hosting platform such as Render. Deployment requires configuring the backend, API key, and frontend URL appropriately.

### Production start command

For a Linux-based hosting environment that supplies a `PORT` environment variable, use:

```bash
python -m uvicorn main:app --app-dir src --host 0.0.0.0 --port $PORT
```

This command binds the application to all network interfaces and uses the port supplied by the hosting platform.

### Required environment variable

Configure the following environment variable in the hosting platform's service settings:

| Variable | Purpose |
|---|---|
| `GNANI_API_KEY` | Authenticates requests to the Gnani AI speech-to-text API |

Do not place the API key in frontend JavaScript, public repository files, or committed configuration files.

### Frontend configuration

The frontend must send transcription requests to the deployed backend URL instead of `http://127.0.0.1:8000`.

Configure the frontend's API base URL to match the actual deployed backend address. Also configure the backend's CORS settings to allow requests from the deployed frontend origin.

**Deployment status:** The application has been tested locally. Public deployment and production URL verification are still pending.

## Running Tests

Run all tests from the project root:

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

**Note:** The live STT test in `tests/test_stt.py` sends an audio file to Gnani AI and may consume API credits. Run it only when necessary.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | API welcome message |
| GET | `/health` | Health check |
| POST | `/api/transcribe` | Transcribe an uploaded audio file |

The transcription endpoint accepts an audio file and a language code as multipart form data.

Interactive API documentation is available at `/docs` while the backend is running.

## Current Status

- Frontend and backend integration: working locally
- Gnani AI speech-to-text integration: tested successfully
- Hindi, English, and Tamil transcription: tested successfully
- File and language validation: implemented
- API tests: passing
- Dependency consistency check: passing
- GitHub repository: available
- Public deployment: pending

## Future Improvements

- Expand language testing and improve language-specific error handling.
- Add AI-powered study-note generation and transcript summarization.
- Allow users to save and organize transcripts.
- Improve accessibility and mobile responsiveness.
- Deploy the application for public access.
- Add further automated tests and production monitoring.

## Security

- Store API keys in environment variables.
- Never commit `.env`, credentials, or private configuration.
- Validate uploaded file types and sizes.
- Keep API keys on the backend; never expose them in frontend code.
- Review API usage limits and costs before public deployment.
- Configure CORS to allow only the required frontend origins in production.

## About

BhashaStudy is being developed for the **Gnani AI Great Indian AI Internship Challenge 2026**.

Its goal is to make voice-based learning more accessible by helping users convert spoken content into readable text across supported languages.

**Built with Python, FastAPI, JavaScript, and Gnani AI.**

**Developer:** [Vivek Pandey](https://github.com/Vivek9942)

**Repository:** [github.com/Vivek9942/BhashaStudy](https://github.com/Vivek9942/BhashaStudy)
