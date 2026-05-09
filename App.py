import streamlit as st
import pdfplumber
import requests

# Hugging Face API Token
API_TOKEN = st.secrets["HF_API_KEY"]

# Correct API URL
API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# App UI
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

    # Extract text
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text

    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # AI Fact Check
    if st.button("Run AI Fact Check"):

        with st.spinner("Analyzing with AI..."):

            prompt = f"""
            Fact check the following text and identify:
            - false claims
            - outdated facts
            - misleading statements

            TEXT:
            {full_text[:2000]}
            """

            payload = {
                "inputs": prompt
            }

            try:

                response = requests.post(
                    API_URL,
                    headers=headers,
                    json=payload,
                    timeout=60
                )

                st.subheader("Fact Check Results")

                st.write(response.json())

            except Exception as e:

                st.error("Request Failed")

                st.write(str(e))