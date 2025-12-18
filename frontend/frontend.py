import streamlit as st
import pandas as pd
import time
import requests

st.set_page_config(
    page_title="AssessMate AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

API_URL = "https://assessmate-ai.onrender.com/recommend"

if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def navigate_to(page):
    st.session_state.page = page

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;500;700;800&display=swap');

    :root {
        --bg-deep: #020617;
        --accent: #6366f1;
        --accent-glow: #818cf8;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --glass: rgba(30, 41, 59, 0.4);
    }

    .stApp {
        background: radial-gradient(circle at 50% 10%, #1e1b4b 0%, #020617 60%, #000000 100%);
        background-attachment: fixed;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: var(--text-primary);
    }

    header {visibility: hidden;}
    .stApp > header {display: none;}

    .block-container {
        padding-top: 1rem;
        padding-bottom: 5rem;
    }

    .navbar-logo {
        font-size: 1.5rem;
        font-weight: 800;
        color: #818cf8 !important;
        margin-top: 12px !important;
        display: inline-block;
    }

    div.stButton > button {
        background: transparent;
        border: none;
        color: #cbd5e1;
        font-weight: 600;
        padding: 10px 20px;
        border-radius: 8px;
        transition: all 0.3s;
        width: 100%;
    }

    div.stButton > button:hover {
        background: rgba(99, 102, 241, 0.1);
        color: #818cf8;
    }

    .glass-card {
        background: var(--glass);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border-color: rgba(99, 102, 241, 0.3);
    }

    h1, h2, h3 { color: white !important; }
    p { color: #94a3b8; }

    .stTextArea textarea {
        background-color: rgba(15, 23, 42, 0.6) !important;
        color: #e2e8f0 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

def render_navbar():
    col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])

    with col1:
        st.markdown('<div class="navbar-logo">⚡ AssessMate</div>', unsafe_allow_html=True)

    with col2:
        if st.button("🏠 Home", use_container_width=True): navigate_to("Home")
    with col3:
        if st.button("👤 Profile", use_container_width=True): navigate_to("Profile")
    with col4:
        if st.button("💬 Community", use_container_width=True): navigate_to("Community")
    with col5:
        if st.button("⭐ Reviews", use_container_width=True): navigate_to("Reviews")

    st.markdown("<div style='height: 2px; background: rgba(255,255,255,0.05); margin-bottom: 30px; margin-top: 10px;'></div>", unsafe_allow_html=True)

render_navbar()

if st.session_state.page == "Home":
    st.markdown("""
    <div style='text-align: center; margin-bottom: 40px;'>
        <h1 style='font-size: 3.5rem; background: linear-gradient(to right, #fff, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            Find the Perfect Assessment
        </h1>
        <p style='font-size: 1.2rem; max-width: 600px; margin: auto;'>
            AI-powered matching for technical, behavioral, and cognitive testing.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        query = st.text_area(
            "Job Description",
            placeholder="Enter job requirements here...",
            height=120,
            label_visibility="collapsed"
        )

        if st.button("🚀 Analyze & Recommend", use_container_width=True):
            if query:
                with st.spinner("Analyzing semantics..."):
                    time.sleep(0.5)
                    response = requests.post(API_URL, json={"query": query})
                    results = pd.DataFrame(response.json()["recommended_assessments"])

                st.markdown("### 🎯 Top Recommendations")
                r_col1, r_col2 = st.columns(2)

                for idx, row in results.iterrows():
                    target = r_col1 if idx % 2 == 0 else r_col2
                    with target:
                        st.markdown(f"""
                        <div class="glass-card">
                            <h4 style="color:#f8fafc;">{row['name']}</h4>
                            <p style="font-size:0.9rem;">
                                {row.get('description', row.get('summary', ''))[:120]}...
                            </p>
                            <a href="{row['url']}" target="_blank" style="color:#818cf8; font-weight:600;">
                                View Details →
                            </a>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a job description.")

elif st.session_state.page == "Profile":
    st.markdown("## 👋 Welcome back, Alex")

elif st.session_state.page == "Community":
    st.markdown("## 🌐 Community Hub")

elif st.session_state.page == "Reviews":
    st.markdown("## ⭐ What Users Are Saying")

st.markdown("""
<div style="text-align: center; margin-top: 80px; color: #475569; font-size: 0.8rem;">
    © 2025 AssessMate AI • Empowering Global Talent Acquisition
</div>
""", unsafe_allow_html=True)
