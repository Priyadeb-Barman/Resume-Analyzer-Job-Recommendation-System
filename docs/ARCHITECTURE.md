# System Architecture

The **AI Resume Analyzer & Job Recommendation System** is built on a modern, decoupled architecture separating the frontend client from the heavy ML/NLP backend processing.

## 1. Frontend (Streamlit)
- **Role**: Provides the interactive User Interface.
- **Why Streamlit?**: Rapid prototyping, excellent native data visualization support (Plotly/Altair), and purely Pythonic.
- **Workflow**:
  1. User uploads a PDF.
  2. Selects a target job role.
  3. Streamlit sends a `multipart/form-data` POST request to the FastAPI backend.
  4. Parses the JSON response and displays dynamic charts and metrics.

## 2. Backend API (FastAPI)
- **Role**: Orchestrates the business logic, ML processing, and API routing.
- **Why FastAPI?**: High performance, native async support, and automatic OpenAPI (Swagger) documentation generation.
- **Workflow**:
  1. Receives the PDF bytes.
  2. Passes bytes to the ML Pipeline.
  3. Returns structured JSON containing ATS score, skills, and recommendations.

## 3. ML & NLP Pipeline
The core intelligence of the application happens in a sequential pipeline:
1. **Extraction (`resume_parser.py`)**: Uses `pdfplumber` to accurately extract raw text from PDF bytes.
2. **Preprocessing (`preprocessing.py`)**: Uses `NLTK` and Regex to clean the text (lowercase, remove stop words, remove punctuation).
3. **Skill Identification (`skills_database.py`)**: Compares clean tokens against a predefined dictionary of technical skills to identify what the candidate knows.
4. **ATS Scoring (`ats_engine.py`)**: Uses Scikit-Learn's `TfidfVectorizer` to convert both the resume text and target Job Description text into TF-IDF vectors. It then calculates the `cosine_similarity` to determine how closely the resume matches the JD requirements.
5. **Recommendation (`recommendation_engine.py`)**: Compares extracted skills against role-specific skill maps to suggest the best alternative career paths.

## 4. Containerization (Docker)
- The entire application is containerized using Docker.
- `docker-compose` spins up two interconnected containers: `fastapi-backend` and `streamlit-frontend`.
- This ensures the application runs consistently across any environment, a crucial requirement for modern deployment pipelines.
