# Predefined Technical Skills Database
# This maps technical skills to specific categories to help in categorizing extracted skills.

SKILL_CATEGORIES = {
    "Programming Languages": [
        "python", "java", "c++", "c", "c#", "javascript", "typescript", "ruby", "go", "swift", "kotlin", "r", "php", "rust", "scala"
    ],
    "Data Science & Machine Learning": [
        "machine learning", "deep learning", "nlp", "natural language processing", "computer vision", 
        "scikit-learn", "tensorflow", "keras", "pytorch", "pandas", "numpy", "matplotlib", "seaborn", 
        "nltk", "spacy", "opencv", "xgboost", "data analysis", "data mining", "statistics"
    ],
    "Web Development & Frameworks": [
        "html", "css", "react", "angular", "vue", "node.js", "express", "django", "flask", "fastapi", "spring boot", "ruby on rails", "bootstrap", "tailwind"
    ],
    "Databases": [
        "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle", "redis", "cassandra", "elasticsearch", "nosql"
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "gcp", "google cloud", "azure", "docker", "kubernetes", "jenkins", "git", "github", "gitlab", "ci/cd", "linux", "bash", "terraform", "ansible"
    ],
    "Soft Skills": [
        "communication", "teamwork", "leadership", "problem solving", "critical thinking", "time management", "agile", "scrum", "project management"
    ]
}

# Role-wise skill maps for recommendation engine
ROLE_SKILL_MAP = {
    "Machine Learning Engineer": [
        "python", "machine learning", "deep learning", "scikit-learn", "tensorflow", "pytorch", "pandas", "numpy", "sql", "docker", "git", "nlp"
    ],
    "Data Analyst": [
        "python", "r", "sql", "excel", "pandas", "numpy", "matplotlib", "tableau", "powerbi", "data analysis", "statistics", "communication"
    ],
    "Software Developer": [
        "python", "java", "c++", "javascript", "git", "sql", "docker", "linux", "problem solving", "agile", "html", "css", "spring boot"
    ],
    "Python Developer": [
        "python", "django", "flask", "fastapi", "sql", "postgresql", "docker", "git", "rest api", "linux"
    ],
    "Full Stack Developer": [
        "javascript", "typescript", "react", "node.js", "express", "html", "css", "sql", "mongodb", "git", "docker", "python"
    ]
}

def get_all_skills() -> set:
    """Returns a flat set of all skills in the database across all categories."""
    all_skills = set()
    for skills in SKILL_CATEGORIES.values():
        all_skills.update(skills)
    return all_skills
