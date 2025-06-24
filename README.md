# Smart Research Assistant with GenAI

This application allows users to upload a PDF or TXT document, generates a summary using NLP, answers user questions based on the document, and generates logic-based comprehension questions with answer evaluation.


## Features

-  Document Upload (PDF/TXT)
-  Automatic Summary (≤ 150 words)
-  Ask Anything (Q&A mode based on document)
-  Challenge Me (Auto-generated logic questions with evaluation)
-  Streamlit UI with Hugging Face Transformers

---

 Architecture / Reasoning Flow:
 
Step 1: Upload PDF or TXT document
      
Step 2: Extract text using pdfminer (PDF) or read (TXT)
        
Step 3: Generate automatic summary using BART model
        
Step 4: User selects interaction mode:

    [Ask Anything]
        → User types a question
        → DistilBERT QA model searches document
        → Returns answer + justification

    [Challenge Me]
        → GPT-2 generates 3 logic-based questions
        → User submits answers
        → System compares answers and gives feedback
Step 5: All answers grounded in document content (no hallucinations)


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


SAMPLE IMAGES

![Screenshot 2025-06-24 220411](https://github.com/user-attachments/assets/15ab4d47-f8c6-4602-b491-0279f0bd6b9d)

![Screenshot 2025-06-24 220429](https://github.com/user-attachments/assets/c08b452a-519d-4bb7-8462-3442489abede)

![Screenshot 2025-06-24 220450](https://github.com/user-attachments/assets/2e5f06b0-0c09-4143-ba55-77a224501724)

![Screenshot 2025-06-24 220519](https://github.com/user-attachments/assets/29bba190-d1fd-45b2-af1b-cd6e5aa94bea)


