# Smart Research Assistant with GenAI

This application allows users to upload a PDF or TXT document, generates a summary using NLP, answers user questions based on the document, and generates logic-based comprehension questions with answer evaluation.


## Features

-  Document Upload (PDF/TXT)
-  Automatic Summary (≤ 150 words)
-  Ask Anything (Q&A mode based on document)
-  Challenge Me (Auto-generated logic questions with evaluation)
-  Streamlit UI with Hugging Face Transformers

---

##  Setup Instructions

### Clone the repository

```bash
git clone https://github.com/marvelousvenom/Smart_Assistant_Application.git
cd Smart_Assistant_Application
2. Create virtual environment (recommended)
python -m venv assistant_env
assistant_env\Scripts\activate  # On Windows
# OR
source assistant_env/bin/activate  # On Mac/Linux
3. Install all required packages
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run app.py
Then open in your browser:
http://localhost:8501
