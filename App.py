import streamlit as st
import pdfplumber
import requests

# HuggingFace API Key
API_KEY = st.secrets["HF_API_KEY"]

# HuggingFace Model URL
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# App Title
st.title("AI Fact Check Agent")

st.write("Upload any PDF and detect false or outdated claims.")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully!")

    full_text = ""

    # Read PDF
    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                full_text += text

    # Show Text
    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # Fact Check Button
    if st.button("Run AI Fact Check"):

        with st.spinner("Checking facts..."):

            prompt = f"""
            Fact check this text and identify false or outdated claims:

            {full_text[:3000]}
            """

            payload = {
                "inputs": prompt
            }

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload
            )

            st.subheader("Fact Check Results")

            # Direct raw response output
            st.text(response.text)