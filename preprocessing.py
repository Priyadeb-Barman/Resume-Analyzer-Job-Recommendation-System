import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Setup NLTK - this needs to run once to ensure the packages are downloaded.
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except Exception:
    nltk.download('punkt')
    nltk.download('stopwords')
    
# We will use NLTK punkt_tab as it's the newer tokenizer requirement for some NLTK versions
try:
    nltk.data.find('tokenizers/punkt_tab')
except Exception:
    nltk.download('punkt_tab')

def clean_text(text: str) -> str:
    """
    Cleans the input text by:
    - Lowercasing
    - Removing URLs, emails, phone numbers
    - Removing special characters and punctuation
    - Removing extra spaces
    """
    if not text:
        return ""
    
    # Lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove emails
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and numbers (keeping only letters and some punctuation used in skills like C++)
    text = re.sub(r'[^a-zA-Z\s\+#]', '', text)
    
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize_and_remove_stopwords(text: str) -> list:
    """
    Tokenizes text and removes English stopwords.
    Returns a list of clean tokens.
    """
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    
    clean_tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
    return clean_tokens

def preprocess_text(text: str) -> str:
    """
    Complete preprocessing pipeline.
    Returns a cleaned string.
    """
    cleaned_text = clean_text(text)
    tokens = tokenize_and_remove_stopwords(cleaned_text)
    return " ".join(tokens)
