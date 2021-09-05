from question_model import Question
from data import question_data

# Create a question bank. Fill it with a list of Questions
question_bank = []
for data in question_data:
    text = data['text']
    answer = data['answer']
    question = Question(text, answer)
    question_bank.append(question)

