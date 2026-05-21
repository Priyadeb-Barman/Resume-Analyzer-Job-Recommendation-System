# Interview Preparation: AI Resume Analyzer

This document contains key questions you might be asked during an interview (especially for roles like TCS Prime, TCS Digital, or ML Internships) regarding this project.

## Q1: Can you explain your project flow?
**Answer**: 
"My project is an AI Resume Analyzer. The flow starts when a user uploads a PDF resume. The Streamlit frontend sends this PDF to a FastAPI backend. 
In the backend, I use `pdfplumber` to extract raw text. The text goes through a preprocessing pipeline using `NLTK` to remove stop words, punctuation, and lowercase everything. 
Then, I extract technical skills by matching tokens against a predefined skills database. Finally, to calculate the ATS Score against a target job role, I use Scikit-Learn to apply TF-IDF Vectorization on both the resume text and the job description, and compute their Cosine Similarity. The result is passed back to the Streamlit UI to display visual charts and missing skill recommendations."

## Q2: Why did you use TF-IDF instead of simple keyword counting?
**Answer**: 
"While keyword counting just checks if a word exists, TF-IDF (Term Frequency-Inverse Document Frequency) evaluates how *important* a word is in a document compared to a larger corpus. It penalizes common words and highlights unique, highly relevant terms. This provides a mathematically robust way to represent text as numerical vectors, which is essential for accurate document comparison using Cosine Similarity."

## Q3: What is Cosine Similarity?
**Answer**: 
"Cosine Similarity is a metric used to measure how similar two vectors are, irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. In my project, after converting the resume and the job description into TF-IDF vectors, I calculate the cosine similarity. A score closer to 1 (or 100%) means the resume highly matches the job description, while a score closer to 0 means they are very different."

## Q4: Why did you choose FastAPI over Flask or Django?
**Answer**: 
"I chose FastAPI because it is extremely fast and built on modern Python features like type hinting and asynchronous programming (`async/await`). It also automatically generates Swagger UI documentation, making it very easy to test the API endpoints during development. Django would be too heavy for a simple ML inference API, and FastAPI offers better performance than Flask."

## Q5: Why did you use Docker?
**Answer**: 
"I used Docker to containerize my application, ensuring that it runs the exact same way on my local machine, a teammate's machine, or in the cloud. By defining a `Dockerfile` and `docker-compose.yml`, I encapsulated all the dependencies (like NLTK data and Scikit-Learn versions) into isolated environments. This demonstrates deployment readiness and understanding of DevOps best practices."

## Q6: What were the biggest challenges you faced?
**Answer**: 
"One major challenge was accurately extracting text from PDFs, as PDFs often have complex formatting or are just scanned images. I initially considered PyPDF2 but switched to `pdfplumber` because it handles complex layouts better. Another challenge was deciding on the NLP approach; I had to balance between a simple keyword match and an overly complex Deep Learning model like BERT. I settled on TF-IDF and Cosine Similarity as they offer a great balance of accuracy and computational efficiency suitable for a stateless API."

## Q7: How would you improve this project in the future?
**Answer**: 
"In the future, I would replace the TF-IDF approach with a pre-trained Large Language Model (LLM) or a Transformer model like BERT to understand the semantic meaning of skills (e.g., understanding that 'React' and 'Frontend Development' are closely related). I would also add web scraping to fetch real-time job descriptions from LinkedIn or Indeed, and integrate a lightweight database like SQLite to track user progress over time."
