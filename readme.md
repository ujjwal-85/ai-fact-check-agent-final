# AI Fact Check Agent

AI Fact Check Agent is a simple web application that allows users to upload PDF documents and analyze the content using AI.
The application extracts text from the uploaded PDF and uses an AI model to identify potentially false claims, outdated information, misleading statistics, and factual inconsistencies.

The project is built using Streamlit and OpenRouter API integration.

---

## Features

* Upload PDF documents
* Extract text automatically from PDFs
* AI-based claim analysis
* Detect misleading or outdated information
* Simple and user-friendly interface
* Deployed on Streamlit Cloud

---

## Tech Stack

* Python
* Streamlit
* pdfplumber
* OpenRouter API
* OpenAI SDK

---

## Project Workflow

1. User uploads a PDF file
2. Text is extracted using pdfplumber
3. Extracted content is sent to the AI model
4. AI analyzes the document
5. Results are displayed inside the web application

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai-fact-check-agent.git
```

Open the project folder:

```bash
cd ai-fact-check-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run App.py
```

---

## Environment Variables

Create Streamlit Secrets or add your API key:

```toml
OPENROUTER_API_KEY="your_api_key"
```

---

## Challenges Faced

During development, the main challenges included:

* handling API integration issues
* deployment configuration
* managing environment variables securely
* handling different AI model responses

These issues were resolved through testing and debugging.

---

## Future Improvements

* Add live web verification
* Highlight incorrect claims directly in text
* Add confidence scores
* Export fact-check reports
* Support multiple file formats

---

## Author

Developed as a learning and assessment project focused on AI integration, document analysis, and deployment using Streamlit.
