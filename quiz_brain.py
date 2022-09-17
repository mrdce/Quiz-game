import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        if self.question_number < 10:
            self.current_question = self.q_list[self.question_number]
            self.question_number += 1
            return f'Q.{self.question_number}. {html.unescape(self.current_question.text)} (True or False): '

    def still_has_questions(self):
        return self.question_number < len(self.q_list)

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True
        else:
            return False

