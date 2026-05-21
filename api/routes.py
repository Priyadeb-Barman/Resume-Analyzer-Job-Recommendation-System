from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from api.schemas import ResumeAnalysisResponse, JobRoleRecommendation
from utils.helpers import allowed_file, read_text_file, get_file_path
from resume_parser import extract_text_from_pdf, extract_skills_from_text
from preprocessing import preprocess_text
from skills_database import get_all_skills, ROLE_SKILL_MAP
from ats_engine import calculate_ats_score, get_skill_gaps
from recommendation_engine import recommend_job_roles
import os

router = APIRouter()

@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze_resume(
    file: UploadFile = File(...),
    target_role: str = Form(None)
):
    """
    Endpoint to analyze an uploaded resume PDF.
    Extracts text, identifies skills, recommends roles, and optionally calculates ATS score
    against a specific target role.
    """
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
        
    # Read file bytes
    file_bytes = await file.read()
    
    # Extract text from PDF
    raw_text = extract_text_from_pdf(file_bytes)
    if not raw_text.strip():
        raise HTTPException(status_code=400, detail="Could not extract text from the PDF. It might be scanned or empty.")
        
    # Preprocess text
    cleaned_text = preprocess_text(raw_text)
    
    # Extract skills
    all_skills = get_all_skills()
    extracted_skills = extract_skills_from_text(cleaned_text, all_skills)
    
    # Get role recommendations based on extracted skills
    recommended_roles = recommend_job_roles(extracted_skills)
    
    # Initialize optional ATS fields
    ats_score = None
    matched_skills = None
    missing_skills = None
    
    # If target role is provided, calculate ATS score and skill gaps
    if target_role:
        # Load sample job description for the target role
        jd_filename = f"{target_role.lower().replace(' ', '_')}.txt"
        jd_path = get_file_path(jd_filename, directory="sample_job_descriptions")
        
        if os.path.exists(jd_path):
            jd_text = read_text_file(jd_path)
            cleaned_jd = preprocess_text(jd_text)
            
            # Calculate ATS Score (Cosine Similarity)
            ats_score = calculate_ats_score(cleaned_text, cleaned_jd)
            
            # Calculate skill gaps based on the role's predefined skills
            # (Assuming the job description implies the core skills mapped in our DB)
            required_skills = ROLE_SKILL_MAP.get(target_role, [])
            if required_skills:
                skill_gaps = get_skill_gaps(extracted_skills, required_skills)
                matched_skills = skill_gaps["matched_skills"]
                missing_skills = skill_gaps["missing_skills"]
        else:
            # If no JD file found, just do simple skill matching against the database map
            required_skills = ROLE_SKILL_MAP.get(target_role, [])
            if required_skills:
                skill_gaps = get_skill_gaps(extracted_skills, required_skills)
                ats_score = skill_gaps["match_percentage"]
                matched_skills = skill_gaps["matched_skills"]
                missing_skills = skill_gaps["missing_skills"]

    return ResumeAnalysisResponse(
        filename=file.filename,
        extracted_skills=extracted_skills,
        target_role=target_role,
        ats_score=ats_score,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommended_roles=[JobRoleRecommendation(**role) for role in recommended_roles]
    )
