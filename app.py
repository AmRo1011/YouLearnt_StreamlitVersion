import streamlit as st
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
load_dotenv()

# Initialize Groq client
try:
    llm = ChatGroq(
        model_name=os.getenv("GROQ_MODEL", "llama3-8b-8192"),
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=float(os.getenv("TEMPERATURE", 0.7)),
        timeout=int(os.getenv("TIMEOUT", 30))
    )
    logging.info("✅ Groq client initialized successfully")
except Exception as e:
    logging.error(f"❌ Error initializing Groq: {e}")
    llm = None

# Set page config
st.set_page_config(
    page_title="AI Course Description Generator",
    page_icon="📚",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        border: 2px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        width: 100%;
        background-color: #4361ee;
        color: white;
        border: none;
        padding: 12px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #3a0ca3;
    }
    .error {
        color: #f72585;
        padding: 10px;
        border-radius: 5px;
        background: #ffebee;
        border-left: 3px solid #f72585;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("AI Course Description Generator")

# Input fields
title = st.text_input("Course Title*", placeholder="Python for Beginners")
category = st.text_input("Course Category*", placeholder="Programming")
language = st.selectbox(
    "Language",
    ["English", "Spanish", "French"]
)

# Generate button
if st.button("Generate Description"):
    if not title or not category:
        st.error("Please fill in all required fields (marked with *)")
    elif not llm:
        st.error("AI service is currently unavailable. Please try again later.")
    else:
        try:
            with st.spinner("Generating description, please wait..."):
                # Construct prompt
                prompt = f"""
                Generate a professional course description with:
                - Title: {title}
                - Category: {category}
                - Language: {language}

                Include:
                1️⃣ 3-4 detailed paragraphs about the course
                2️⃣ Target audience
                3️⃣ Learning objectives
                4️⃣ A professional and engaging tone
                """

                # Invoke AI model
                response = llm.invoke(prompt)

                # Display result
                if response and response.content:
                    st.text_area("Generated Description", response.content, height=300)
                else:
                    st.error("Failed to generate description. Please try again.")
                    
        except Exception as e:
            logging.error(f"❌ Error generating description: {e}")
            st.error("An error occurred while generating the description. Please try again.") 