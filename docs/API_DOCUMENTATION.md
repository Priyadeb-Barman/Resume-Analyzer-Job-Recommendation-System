# API Documentation

The backend of this project is powered by FastAPI, which automatically generates OpenAPI specifications.

## Accessing Swagger UI
Once you run the FastAPI server (either locally via `uvicorn` or via `docker-compose`), you can access the interactive API documentation at:
- **URL**: `http://localhost:8000/docs`

## Endpoint: `/api/analyze`

### Method: `POST`

### Description
Analyzes an uploaded PDF resume, extracts text and skills, and evaluates compatibility against an optional target role.

### Request Form Data
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | `file` (PDF) | **Yes** | The resume PDF file to be analyzed. |
| `target_role` | `string` | No | The target job role (e.g., "Machine Learning Engineer"). Used to calculate ATS score. |

### Response (JSON)
The API returns a JSON object matching the `ResumeAnalysisResponse` Pydantic model.

**Success Response (200 OK) Example:**
```json
{
  "filename": "john_doe_resume.pdf",
  "extracted_skills": ["python", "machine learning", "docker", "sql"],
  "target_role": "Machine Learning Engineer",
  "ats_score": 85.5,
  "matched_skills": ["python", "machine learning", "docker"],
  "missing_skills": ["scikit-learn", "tensorflow"],
  "recommended_roles": [
    {
      "role": "Machine Learning Engineer",
      "match_percentage": 85.5,
      "matched_skills": ["python", "machine learning", "docker"]
    },
    {
      "role": "Data Analyst",
      "match_percentage": 40.0,
      "matched_skills": ["python", "sql"]
    }
  ],
  "error": null
}
```

### Error Handling
- **400 Bad Request**: Raised if the uploaded file is not a PDF, or if the PDF is empty/unreadable (e.g., scanned images without OCR).

### Testing the API using cURL
```bash
curl -X 'POST' \
  'http://localhost:8000/api/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_resume.pdf;type=application/pdf' \
  -F 'target_role=Machine Learning Engineer'
```
