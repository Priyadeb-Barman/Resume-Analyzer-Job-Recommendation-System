from skills_database import ROLE_SKILL_MAP

def recommend_job_roles(extracted_skills: list) -> list:
    """
    Recommends job roles based on the extracted skills from the resume.
    Returns a sorted list of dictionaries with role name and match percentage.
    """
    if not extracted_skills:
        return []
        
    extracted_set = set([s.lower() for s in extracted_skills])
    recommendations = []
    
    for role, required_skills in ROLE_SKILL_MAP.items():
        required_set = set([s.lower() for s in required_skills])
        matched_skills = extracted_set.intersection(required_set)
        
        match_score = round(len(matched_skills) / len(required_set) * 100, 2)
        
        if match_score > 0:
            recommendations.append({
                "role": role,
                "match_percentage": match_score,
                "matched_skills": list(matched_skills)
            })
            
    # Sort recommendations by match percentage in descending order
    recommendations.sort(key=lambda x: x["match_percentage"], reverse=True)
    
    return recommendations
