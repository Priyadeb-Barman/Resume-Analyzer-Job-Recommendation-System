from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_ats_score(resume_text: str, job_description_text: str) -> float:
    """
    Calculates the ATS match score between a resume and a job description
    using TF-IDF Vectorization and Cosine Similarity.
    Returns a percentage score (0 to 100).
    """
    if not resume_text or not job_description_text:
        return 0.0

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer ONLY on the job description
    # This restricts the vocabulary to only the words that matter for the job,
    # preventing long resumes from being penalized for having extra words.
    vectorizer.fit([job_description_text])
    
    # Transform both documents using the JD's vocabulary
    tfidf_matrix = vectorizer.transform([resume_text, job_description_text])
    
    # Calculate cosine similarity between the two vectors
    # tfidf_matrix[0] is resume, tfidf_matrix[1] is job description
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # Convert to percentage and round to 2 decimal places
    score = round(similarity[0][0] * 100, 2)
    return score

def get_skill_gaps(extracted_skills: list, job_required_skills: list) -> dict:
    """
    Identifies matched and missing skills by comparing extracted skills
    with the required skills for a specific job role.
    """
    extracted_set = set([s.lower() for s in extracted_skills])
    required_set = set([s.lower() for s in job_required_skills])
    
    matched_skills = list(extracted_set.intersection(required_set))
    missing_skills = list(required_set.difference(extracted_set))
    
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(len(matched_skills) / len(required_set) * 100, 2) if required_set else 0.0
    }
