# Base Image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
# Needed for some Python packages and NLTK
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data directly during build to save time later
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Copy the rest of the application
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# The start command is handled by docker-compose, but we can set a default
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
