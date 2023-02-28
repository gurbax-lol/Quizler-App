from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Smarty Party")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"),
                           highlightthickness=0)
        self.score.grid(row=0, column=1)

        self.question = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question.create_text(150, 125, width=280,
                                                       font=("Arial", 20, "italic"),
                                                       fill=THEME_COLOR)
        self.question.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_image = PhotoImage(file=r"images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, bd=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file=r"images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, bd=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score} / 10")
            next_question_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=next_question_text)
        else:
            self.question.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def answer_false(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, user_answer):
        if user_answer:
            self.question.config(bg="#CDE990")
            self.window.after(1000, self.get_next_question)
        else:
            self.question.config(bg="#A7727D")
            self.window.after(1000, self.get_next_question)
