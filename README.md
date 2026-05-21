# AI Resume Analyzer & Job Recommendation System 

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.2-FF4B4B?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.2-F7931E?logo=scikit-learn)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)

A professional, deployment-ready AI-powered web application that analyzes resumes using Natural Language Processing (NLP) to evaluate job compatibility, predict ATS scores, extract skills, and recommend ideal job roles.

##  Project Overview
This project processes uploaded resume PDFs, extracts and cleans the text, and leverages **TF-IDF Vectorization** and **Cosine Similarity** to compare candidates against target job descriptions (like Machine Learning Engineer or Data Analyst). It provides visual feedback on skill gaps and overall resume strengths, making it a perfect tool for job seekers to optimize their resumes.

##  Core Features
- **PDF Resume Parsing**: Extracts clean text from resumes using `pdfplumber`.
- **NLP Text Preprocessing**: Cleans and tokenizes text using `NLTK` and Regex.
- **Skill Extraction**: Matches resume text against a predefined database of technical skills.
- **ATS Compatibility Scoring**: Generates an ATS match percentage using TF-IDF and Cosine Similarity against sample job descriptions.
- **Skill Gap Analysis**: Visually highlights extracted skills vs. missing core requirements.
- **Job Role Recommendation**: Ranks the best-fit job roles based on the candidate's skill profile.
- **Interactive UI**: A clean, responsive dashboard built with Streamlit and Plotly charts.

##  Architecture
The system follows a modular, decoupled architecture:
1. **Frontend**: Streamlit (`app.py`) for the UI and data visualization.
2. **Backend API**: FastAPI (`main.py`, `api/`) to handle PDF processing and ML logic.
3. **ML/NLP Engine**: Custom modules for preprocessing, TF-IDF calculation, and skill extraction.

*(See `docs/ARCHITECTURE.md` for a deeper dive)*

##  Screenshots
*(Add your screenshots to the `screenshots/` folder and link them here)*
- Dashboard View: `![Dashboard](screenshots/dashboard.png)`
- ATS Score Chart: `![ATS Score](screenshots/ats_score.png)`

##  Tech Stack
- **Frontend**: Streamlit, Plotly, Pandas
- **Backend**: FastAPI, Uvicorn, Python-Multipart
- **ML & NLP**: Scikit-learn (TF-IDF), NLTK (Tokenization, Stopwords), Numpy
- **Document Processing**: pdfplumber, Regex
- **DevOps**: Docker, Docker Compose

---

## 🛠 Local Installation & Setup

### Option 1: Standard Python Setup (Without Docker)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-resume-analyzer.git
   cd ai-resume-analyzer
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the FastAPI Backend:**
   ```bash
   uvicorn main:app --reload --port 8000
   ```
5. **Run the Streamlit Frontend (in a new terminal):**
   ```bash
   streamlit run app.py
   ```

### Option 2: Docker Setup (Recommended)
1. Ensure Docker and docker-compose are installed on your machine.
2. Run the application:
   ```bash
   docker-compose up --build
   ```
3. Access the Streamlit UI at `http://localhost:8501` and the API docs at `http://localhost:8000/docs`.

---

##  Deployment

### Streamlit Community Cloud (Frontend)
1. Push your repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and create a new app.
3. Select this repository and set the main file path to `app.py`.
4. Add the Backend API URL to the Streamlit secrets if hosting the backend separately.

### Render / Heroku (Backend)
- Deploy the FastAPI backend using the provided `Dockerfile` on platforms like Render, Railway, or Heroku to make the API publicly accessible.

*(See `docs/DEPLOYMENT.md` for detailed instructions)*

---

##  Folder Structure
```text
ai-resume-analyzer/
├── api/                    # FastAPI routes and Pydantic schemas
├── docs/                   # Detailed documentation and interview QA
├── sample_job_descriptions/# Text files with standard JDs for ATS scoring
├── utils/                  # Helper functions
├── app.py                  # Streamlit frontend entry point
├── main.py                 # FastAPI backend entry point
├── ats_engine.py           # TF-IDF and Cosine Similarity logic
├── preprocessing.py        # NLTK text cleaning pipeline
├── recommendation_engine.py# Role recommendation logic
├── resume_parser.py        # PDF text extraction
├── skills_database.py      # Hardcoded skills dictionary
├── Dockerfile              # Container configuration
├── docker-compose.yml      # Multi-container orchestration
└── requirements.txt        # Python dependencies
```

##  Future Scope
- **Advanced NLP**: Transition from TF-IDF to advanced transformer models (like BERT) for deeper semantic understanding.
- **Authentication**: Add user login to save resume history and track ATS score improvements over time.
- **Web Scraping**: Automatically pull live job descriptions from LinkedIn or Indeed for real-time ATS scoring.

##  Author
**Your Name**
- LinkedIn: [Priyadeb Barman](linkedin.com/in/priyadeb-barman-6893a72a8)
- Github: [Priyadeb-Barman](https://github.com/Priyadeb-Barman)
- Email: mr.priyadeb@gmail.com
