from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quiz Game")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(158, 125, text=f"placeholder", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"), width=280)
        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button = Button(image=self.true_img, pady=10, command=self.true_button)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_img, pady=10, command=self.false_button)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.windows.mainloop()

    def get_next_question(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="END OF QUIZ")

    def true_button(self):
        response = self.quiz.check_answer("True")
        self.get_next_question()
        self.update_score()

    def false_button(self):
        response = self.quiz.check_answer("False")
        self.get_next_question()
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
