# BhashaStudy – Multilingual Voice-First Study Assistant

<p align="center">
  <strong>Making educational audio accessible through multilingual Speech-to-Text technology.</strong>
</p>

<p align="center">
  <a href="https://bhashastudy-frontend.onrender.com"> Live Demo</a> •
  <a href="https://github.com/Vivek9942/BhashaStudy">GitHub Repository</a>
</p>

---

## Overview

**BhashaStudy** is a multilingual, voice-first learning assistant designed to convert spoken educational content into readable text.

Students often need to revisit lectures, recorded lessons, and other educational audio materials. Listening to long recordings repeatedly can be time-consuming. BhashaStudy addresses this challenge by allowing users to upload audio recordings, select their preferred language, and generate text transcriptions using **Gnani AI's Prisma V2.5 Speech-to-Text model**.

The goal is to make spoken learning content easier to access, read, revisit, and revise, particularly across supported Indian languages.

## Key Features

- **Multilingual Speech-to-Text:** Converts audio recordings into readable text.
- **Indian Language Support:** Supports multiple Indian languages through Gnani AI.
- **Audio Upload:** Accepts `.mp3`, `.wav`, `.m4a`, `.flac`, and `.ogg` files.
- **Language Selection:** Allows users to select their preferred transcription language.
- **FastAPI Backend:** Handles audio uploads, validation, and API communication.
- **Simple User Interface:** Provides a clean and straightforward audio transcription experience.
- **Input Validation:** Checks file type, file size, and supported language selection.
- **Cloud Deployment:** Frontend and backend are deployed separately on Render.

## Supported Languages

The application currently supports the following language codes:

| Language | Language Code |
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

*Transcription availability and quality may vary depending on the selected language and audio quality.*

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Speech-to-Text | Gnani AI Prisma V2.5 |
| API Communication | Requests |
| Frontend | HTML, CSS, JavaScript |
| Environment Management | Python Virtual Environment |
| Configuration | Python Dotenv |
| Testing | Python Unittest |
| Backend Deployment | Render Web Service |
| Frontend Deployment | Render Static Site |
| Version Control | Git and GitHub |

## System Architecture

```text
                  USER
                    |
                    v
          BhashaStudy Frontend
             (HTML, CSS, JS)
                    |
                    v
               Audio Upload
                    |
                    v
             FastAPI Backend
                    |
                    v
             Input Validation
                    |
                    v
            Gnani AI API Request
                    |
                    v
       Prisma V2.5 Speech-to-Text
                    |
                    v
          Generated Transcription
                    |
                    v
            Display Text to User
```

## Project Structure

```text
BhashaStudy/
│
├── src/
│   ├── main.py
│   └── gnani_stt.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── tests/
│   ├── test_api.py
│   ├── test_stt.py
│   └── test_stt_unit.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started – Run Locally

Follow these instructions to run BhashaStudy on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/Vivek9942/BhashaStudy.git
cd BhashaStudy
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory:

```env
GNANI_API_KEY=your_gnani_api_key
```

Replace the placeholder with your own Gnani AI API key.

**Security:** Never upload your actual API key or `.env` file to GitHub.

### 5. Start the FastAPI backend

```bash
python -m uvicorn main:app --app-dir src --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

### 6. Open the frontend

Open `frontend/index.html` in your browser or use the VS Code Live Server extension.

For a fully local setup, configure the frontend API URL in `frontend/script.js` to:

```javascript
const API_URL = "http://127.0.0.1:8000/api/transcribe";
```

The deployed frontend is already configured to communicate with the deployed backend.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks backend health |
| POST | `/api/transcribe` | Uploads audio and returns transcription |
| GET | `/docs` | Interactive API documentation |

## Audio Upload Specifications

| Parameter | Configuration |
|---|---|
| Maximum File Size | 10 MB |
| Supported Formats | MP3, WAV, M4A, FLAC, OGG |
| Language | Supported language code |
| Processing | Gnani AI Prisma V2.5 |

## Testing

BhashaStudy includes unit tests and API tests to verify core application functionality.

Run the test suite using:

```powershell
python -m unittest discover -s tests -v
```

The tests cover:

- Backend health endpoint.
- Empty audio upload validation.
- Unsupported file format rejection.
- Unsupported language validation.
- Speech-to-Text functionality and related unit tests.

*Note: Live Speech-to-Text tests may require a valid API key and consume API credits.*

## Gnani AI Integration

BhashaStudy uses **Gnani AI Prisma V2.5**, a Speech-to-Text model, to convert audio recordings into text.

The integration enables:

1. Audio submission through the FastAPI backend.
2. Communication with the Gnani AI Speech-to-Text API.
3. Language-specific transcription requests.
4. Returning generated text to the frontend.

**Gnani AI Resources:**

- [Gnani AI Website](https://www.gnani.ai/)
- [Gnani AI Documentation](https://docs.gnani.ai/)
- [Gnani AI API Dashboard](https://app.gnani.ai/voice)

## Deployment

BhashaStudy is deployed using Render:

- **Frontend:** Render Static Site
- **Backend:** Render Web Service

The frontend communicates with the deployed FastAPI backend, which securely communicates with the Gnani AI API.

*Note: The backend uses Render's free hosting tier, so the first request after inactivity may take additional time while the service starts.*

## Future Scope

The project can be extended with additional learning-focused capabilities, including:

- Automatic generation of study notes from transcriptions.
- AI-generated quizzes and multiple-choice questions.
- Contextual question answering based on lecture transcripts.
- Transcript export in TXT and PDF formats.
- Text-to-Speech support for audio-based learning.

*These are planned enhancements and are not currently implemented features.*

## Project Information

| Detail | Information |
|---|---|
| Project Name | BhashaStudy |
| Project Type | Multilingual Voice-First Study Assistant |
| Challenge | Gnani AI Great Indian AI Internship Challenge 2026 |
| Core AI Technology | Gnani AI Prisma V2.5 – Speech-to-Text |
| Developer | Vivek Pandey |

**GitHub:** [Vivek9942](https://github.com/Vivek9942)  
**LinkedIn:** [Vivek Pandey](https://www.linkedin.com/in/vivek-pandey-978128328)

---

## Acknowledgements

Special thanks to **Gnani AI** for providing Speech-to-Text technology and the opportunity to build an application using its AI models through the Great Indian AI Internship Challenge 2026.

---

<p align="center">
  <strong>BhashaStudy – Turning Spoken Learning into Readable Knowledge.</strong>
</p>
