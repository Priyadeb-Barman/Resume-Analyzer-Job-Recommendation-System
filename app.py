import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="AI Resume Analyzer & Job Recommendation System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

import os

# Backend API URL (FastAPI) - defaults to localhost, can be overridden by Docker env var
API_URL = os.getenv("API_URL", "http://localhost:8000/api/analyze")

def main():
    st.title(" AI Resume Analyzer & Job Recommendation System")
    st.markdown("Upload your resume in PDF format to get ATS insights, skill analysis, and role recommendations powered by AI/NLP.")

    # Sidebar for Job Target Selection
    st.sidebar.header(" Target Job Role")
    st.sidebar.markdown("Select a role to generate an ATS Score and find missing skills.")
    target_role = st.sidebar.selectbox(
        "Choose Target Role",
        ["", "Machine Learning Engineer", "Data Analyst", "Software Developer", "Python Developer", "Full Stack Developer"]
    )

    # File uploader
    uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    if uploaded_file is not None:
        if st.button("Analyze Resume", type="primary"):
            with st.spinner("Analyzing resume using NLP..."):
                try:
                    # Prepare file for upload
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                    data = {"target_role": target_role} if target_role else {}
                    
                    # Call FastAPI backend
                    response = requests.post(API_URL, files=files, data=data)
                    
                    if response.status_code == 200:
                        result = response.json()
                        display_results(result)
                    else:
                        st.error(f"Error from API: {response.text}")
                except Exception as e:
                    st.error(f"Failed to connect to backend: {e}. Make sure FastAPI is running on port 8000.")

def display_results(result):
    st.success(" Analysis Complete!")
    
    st.markdown("---")
    
    # 1. ATS Score Section (If Target Role selected)
    if result.get("target_role") and result.get("ats_score") is not None:
        st.header(f" ATS Compatibility: {result['target_role']}")
        ats_score = result["ats_score"]
        
        # Gauge Chart for ATS Score
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = ats_score,
            title = {'text': "ATS Score (%)"},
            gauge = {
                'axis': {'range': [None, 100]},
                'bar': {'color': "green" if ats_score > 70 else ("orange" if ats_score > 40 else "red")},
                'steps' : [
                    {'range': [0, 40], 'color': "lightgray"},
                    {'range': [40, 70], 'color': "gray"}
                ]
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

    # 2. Extracted vs Missing Skills
    st.header(" Skills Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(" Extracted Skills")
        extracted = result.get("extracted_skills", [])
        if extracted:
            st.write(", ".join(extracted))
        else:
            st.warning("No skills found.")
            
    with col2:
        if result.get("target_role") and result.get("missing_skills") is not None:
            st.subheader(" Missing Skills")
            missing = result.get("missing_skills", [])
            if missing:
                st.write(", ".join(missing))
            else:
                st.success("You have all the core required skills!")

    # 3. Recommended Roles
    st.markdown("---")
    st.header(" Top Job Role Recommendations")
    
    recommended_roles = result.get("recommended_roles", [])
    if recommended_roles:
        # Create DataFrame for Bar Chart
        df_roles = pd.DataFrame(recommended_roles)
        
        # Display Bar Chart
        fig2 = px.bar(
            df_roles, 
            x='match_percentage', 
            y='role', 
            orientation='h',
            title='Role Compatibility Match (%)',
            color='match_percentage',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # Detailed Expanders
        for role in recommended_roles:
            with st.expander(f"{role['role']} - {role['match_percentage']}% Match"):
                st.write("**Matched Skills:**")
                st.write(", ".join(role['matched_skills']))
    else:
        st.info("Not enough skills extracted to recommend specific roles.")

    # 4. Resume Strengths
    st.markdown("---")
    st.header(" Resume Strengths")
    num_skills = len(result.get("extracted_skills", []))
    if num_skills > 15:
        st.success("Excellent! Your resume showcases a wide variety of technical skills.")
    elif num_skills > 5:
        st.info("Good start. You have a solid foundational skill set, but adding more specific tools/libraries could help.")
    else:
        st.warning("Your resume appears to lack technical keywords. Consider adding specific programming languages, frameworks, and tools.")

if __name__ == "__main__":
    main()
