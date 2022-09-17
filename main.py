from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Interface

question_bank = []
for entry in question_data:
    question = Question(q_text=entry['question'], q_answer=entry['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = Interface(quiz)
quiz.next_question()
