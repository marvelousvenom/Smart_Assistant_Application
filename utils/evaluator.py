def evaluate_answer(user_answer, correct_answer):
    if user_answer.strip().lower() in correct_answer.strip().lower():
        return "Correct!"
    else:
        return f"Incorrect. Expected: **{correct_answer}**"
