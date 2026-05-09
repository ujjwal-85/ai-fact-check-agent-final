import streamlit as st
import pdfplumber
import requests

# Hugging Face API Token from Streamlit Secrets
API_TOKEN = st.secrets["HF_API_KEY"]

# Working Hugging Face model endpoint
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# App Title
st.title("AI Fact Check Agent")

st.write("Upload any PDF and analyze claims using AI.")

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

    # Show extracted text
    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # Run AI Fact Check
    if st.button("Run AI Fact Check"):

        with st.spinner("Analyzing PDF with AI..."):

            prompt = f"""
            Fact check the following text.

            Identify:
            - false claims
            - outdated facts
            - misleading statistics

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

                # Show raw API response
                st.code(response.text)

            except Exception as e:

                st.error("API Request Failed")

                st.code(str(e))