import streamlit as st
import pdfplumber
from openai import OpenAI

# OpenRouter API Key
API_KEY = st.secrets["OPENROUTER_API_KEY"]

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

# UI
st.title("AI Fact Check Agent")

st.write("Upload a PDF and analyze claims using AI.")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully!")

    full_text = ""

    # Extract text from PDF
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text

    # Show text
    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # Run AI Analysis
    if st.button("Run AI Fact Check"):

        with st.spinner("Analyzing with AI..."):

            prompt = f"""
            You are an expert AI fact checker.

            Analyze the following document carefully.

            Identify:
            - False claims
            - Incorrect statistics
            - Outdated information
            - Misleading statements

            For every issue provide:

            Claim:
            Problem:
            Correct Fact:

            DOCUMENT:
            {full_text[:2000]}
            """

            try:

                response = client.chat.completions.create(

                    model="openai/gpt-3.5-turbo",

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]

                )

                result = response.choices[0].message.content

                st.subheader("Fact Check Results")

                st.success("AI Fact Check Completed")

                st.write(result)

            except Exception as e:

                st.error("Request Failed")

                st.write(str(e))