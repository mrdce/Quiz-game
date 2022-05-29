from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question = Question(q_text=entry['question'], q_answer=entry['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions() == True:
    quiz.next_question()

quiz.endgame()
