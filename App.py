import streamlit as st
import pdfplumber
import requests

# Hugging Face API Token
API_TOKEN = st.secrets["HF_API_KEY"]

# Correct Hugging Face endpoint
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Streamlit UI
st.title("AI Fact Check Agent")

st.write("Upload any PDF and detect potentially false or outdated claims using AI.")

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

    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # AI Fact Check
    if st.button("Run AI Fact Check"):

        with st.spinner("AI is analyzing claims..."):

            prompt = f"""
            You are an AI fact-checking assistant.

            Analyze the following text and identify:
            - false claims
            - misleading statements
            - outdated facts
            - incorrect statistics

            Return results in simple bullet points.

            TEXT:
            {full_text[:2000]}
            """

            payload = {
                "inputs": prompt,
                "parameters": {
                    "max_new_tokens": 300
                }
            }

            response = requests.post(
                API_URL,
                headers=headers,
                json=payload
            )

            st.subheader("Fact Check Results")

            try:

                result = response.json()

                if isinstance(result, list):

                    st.write(result[0]["generated_text"])

                else:

                    st.write(result)

            except Exception as e:

                st.error("Error processing AI response")

                st.text(str(e))