import pdfplumber
import io

def extract_text_from_pdf(pdf_file_bytes: bytes) -> str:
    """
    Extracts text from a PDF file using pdfplumber.
    Takes file bytes as input to handle FastAPI UploadFile easily.
    """
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(pdf_file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def extract_skills_from_text(text: str, all_skills: set) -> list:
    """
    Extracts skills from text by matching against a predefined set of skills.
    Simple keyword matching is used for this beginner-friendly project.
    """
    if not text:
        return []
        
    extracted_skills = []
    # Tokenize the text by spaces (assuming text is already preprocessed/lowercased)
    words = set(text.split())
    
    # We also check the raw lowercase text for multi-word skills like "machine learning"
    text_lower = text.lower()
    
    for skill in all_skills:
        skill_lower = skill.lower()
        if " " in skill_lower:
            # Multi-word skill
            if skill_lower in text_lower:
                extracted_skills.append(skill_lower)
        else:
            # Single-word skill
            if skill_lower in words:
                extracted_skills.append(skill_lower)
                
    return list(set(extracted_skills))
