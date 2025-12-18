# AssessMate AI

Smart Assessment Recommendations for Smarter Hiring

## Overview
AssessMate AI is an intelligent recommendation system that maps natural language job descriptions to relevant SHL assessments using semantic similarity.

## Tech Stack
- Python
- TF-IDF + Cosine Similarity
- FastAPI (Backend API)
- Streamlit (Frontend)
- Pandas, Scikit-learn

## Features
- Semantic matching of job descriptions
- Clean, recruiter-friendly UI
- Direct linking to official SHL assessment URLs
- REST API for recommendations

## Note on SHL URLs
Some SHL product pages are session-gated and may show fallback pages without an active SHL login. The system links to official SHL product URLs as required.

## How to Run Locally

### Backend
```bash
cd app
pip install -r requirements.txt
uvicorn app:app --reload

### Frontend
cd frontend
streamlit run frontend.py
