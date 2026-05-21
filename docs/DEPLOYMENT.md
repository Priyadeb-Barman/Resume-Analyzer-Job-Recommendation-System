# Deployment Guide

For a beginner-to-intermediate fresher portfolio, the easiest and most cost-effective way to deploy this application is by separating the Frontend and Backend.

## 1. Deploying the Backend API (FastAPI) on Render
Render is an excellent free-tier platform for hosting containerized backend services.

1. Create a free account on [Render](https://render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub account and select your `ai-resume-analyzer` repository.
4. Settings:
   - **Environment**: Docker (Since we have a Dockerfile)
   - **Branch**: main
5. Click **Create Web Service**.
6. Once deployed, Render will provide a URL (e.g., `https://ai-resume-analyzer-api.onrender.com`).
7. **Important**: Test the API by going to `https://ai-resume-analyzer-api.onrender.com/docs`.

## 2. Deploying the Frontend (Streamlit) on Streamlit Community Cloud
Streamlit Community Cloud is the best place to host Streamlit apps for free.

1. Ensure your backend URL is updated. In your GitHub repo, edit `app.py` or use Streamlit Secrets to set the `API_URL` to your new Render URL (e.g., `https://ai-resume-analyzer-api.onrender.com/api/analyze`).
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **New app**.
4. Select your repository, branch, and specify the main file path: `app.py`.
5. Click **Deploy!**
6. Streamlit will install the requirements and launch your UI.

## Why this approach?
- **Cost**: Both platforms offer generous free tiers.
- **Simplicity**: No complex Kubernetes or AWS setup required.
- **Professionalism**: Having a live link on your resume shows that you understand the complete software development lifecycle, from code to cloud.
