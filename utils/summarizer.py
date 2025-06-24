from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    trimmed = text[:4000]  # Hugging Face has a max token limit
    summary = summarizer(trimmed, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
