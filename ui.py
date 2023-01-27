THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzy")

        self.score_label = Label(text=f"Score {quiz_brain.score}", font=("Arial", 20, "bold"), fg="white",
                                 bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text_box = self.canvas.create_text(150, 125, text=quiz_brain.next_question(), font=("Arial", 15, "italic"),
                                                fill=THEME_COLOR, width=270)
        self.get_next_question()
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong_press)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score {self.quiz_brain.score}")
            targeted_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.text_box, text=targeted_text)

        else:
            self.canvas.itemconfig(self.text_box, text='The Quizz is Done :")')
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def wrong_press(self):
        self.give_feedback(self.quiz_brain.check_answer("True"))

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)




