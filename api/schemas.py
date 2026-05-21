from pydantic import BaseModel
from typing import List, Dict, Optional

class JobRoleRecommendation(BaseModel):
    role: str
    match_percentage: float
    matched_skills: List[str]

class ResumeAnalysisResponse(BaseModel):
    filename: str
    extracted_skills: List[str]
    target_role: Optional[str] = None
    ats_score: Optional[float] = None
    matched_skills: Optional[List[str]] = None
    missing_skills: Optional[List[str]] = None
    recommended_roles: List[JobRoleRecommendation]
    error: Optional[str] = None
