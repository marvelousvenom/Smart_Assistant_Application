from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_questions(text):
    trimmed = text[:1000]  # Limit input size
    prompt = f"Generate 3 comprehension questions with answers based on this text:\n{trimmed}"
    output = generator(prompt, max_length=300, num_return_sequences=1)[0]["generated_text"]
    
    # Very basic split; in production use NLP parsing
    questions = []
    for line in output.split("\n"):
        if "?" in line:
            parts = line.split("?")
            question = parts[0].strip() + "?"
            answer = parts[1].strip().strip("-:") if len(parts) > 1 else "Not provided"
            questions.append({"question": question, "answer": answer})
            if len(questions) == 3:
                break
    return questions
