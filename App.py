import streamlit as st
import pdfplumber
import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# App title
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

    # Show extracted text
    st.subheader("Extracted Text")

    st.write(full_text[:3000])

    # AI Fact Check Button
    if st.button("Run AI Fact Check"):

        with st.spinner("AI is checking facts..."):

            prompt = f"""
            You are a professional AI fact checker.

            Analyze the following PDF text.

            Identify:
            - false claims
            - outdated statistics
            - incorrect dates
            - fake technical facts

            For every incorrect claim return:

            Claim:
            Status:
            Correct Fact:

            TEXT:
            {full_text[:4000]}
            """

            response = client.chat.completions.create(

                model="google/gemma-2-9b-it:free",

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            result = response.choices[0].message.content

            st.subheader("Fact Check Results")

            st.write(result)