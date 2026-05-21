import os

# Base directory of the project (parent of the utils/ folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def allowed_file(filename: str) -> bool:
    """Check if the uploaded file is a PDF."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

def get_file_path(filename: str, directory: str = "sample_resumes") -> str:
    """Get the full path for a file within a specific directory, relative to the project root."""
    return os.path.join(BASE_DIR, directory, filename)

def read_text_file(filepath: str) -> str:
    """Read contents of a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""
