import streamlit as st
from utils.summarizer import generate_summary
from utils.qa import answer_question
from utils.question_generator import generate_questions
from utils.evaluator import evaluate_answer
from pdfminer.high_level import extract_text
import os

st.set_page_config(page_title="Smart Assistant", layout="wide")

st.title("Smart Research Assistant with GenAI")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

document_text = ""

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        document_text = extract_text("temp.pdf")
    elif uploaded_file.type == "text/plain":
        document_text = uploaded_file.read().decode("utf-8")
    st.success("Document uploaded successfully!")
    
    # Auto Summary
    st.subheader("Document Summary (Auto-generated)")
    summary = generate_summary(document_text)
    st.info(summary)

    # Choose Mode
    mode = st.radio("Choose a mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("❓ Ask Anything About the Document")
        user_question = st.text_input("Enter your question:")
        if user_question:
            response = answer_question(document_text, user_question)
            st.success(f"Answer: {response['answer']}")
            st.caption(f"Confidence: {round(response['score'], 2)} | Start: {response['start']}")

    elif mode == "Challenge Me":
        st.subheader("Challenge Questions from Document")
        questions = generate_questions(document_text)
        for idx, q in enumerate(questions):
            user_ans = st.text_input(f"Q{idx+1}: {q['question']}", key=idx)
            if user_ans:
                feedback = evaluate_answer(user_ans, q["answer"])
                st.markdown(f"{feedback}")

