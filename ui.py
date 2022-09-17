from tkinter import *
from quiz_brain import QuizBrain

BG = '#E1DFE2'


class Interface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=BG)

        self.score = Label(text='Score: 0', bg=BG, font=('Arial', 10, 'normal'), padx=20, pady=20)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 120, text='boop', font=('Arial', 13, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        correct_image = PhotoImage(file='./images/right.png')
        self.correct_button = Button(image=correct_image,
                                     bg=BG,
                                     highlightthickness=0,
                                     borderwidth=0,
                                     command=self.answer_true)
        self.correct_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file='./images/wrong.png')
        self.wrong_button = Button(image=wrong_image,
                                   bg=BG,
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.answer_false)
        self.wrong_button.grid(column=1, row=2)

        self.next_question_ui()

        self.window.mainloop()

    def next_question_ui(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions() == True:
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f'End of quiz! Your final score is {self.quiz.score}/10')
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer(user_answer='True')
        self.feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer(user_answer='False')
        self.feedback(is_right)

    def feedback(self, is_right):
        def change_color():
            self.canvas.configure(bg='white')

        if is_right == True:
            self.canvas.configure(bg='#96C362')
        elif is_right == False:
            self.canvas.configure(bg='#FF7575')
        self.window.after(1000, self.next_question_ui)
