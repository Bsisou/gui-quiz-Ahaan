import tkinter as tk
from tkinter import messagebox

class StartScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Quiz")
        self.root.geometry("500x500")

        self.bg = tk.PhotoImage(file="first.png")
        self.bglabel = tk.Label(self.root, image=self.bg)
        self.bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.name_label = tk.Label(self.root, text="Please enter your name:", font=("Arial", 12))
        self.name_label.place(relx=0.5, rely=0.3, anchor="center")

        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.place(relx=0.5, rely=0.55, anchor="center")

        self.start_button = tk.Button(self.root, text="Start", command=self.start_quiz, font=("Arial", 12), bg="black", fg="white")
        self.start_button.place(relx=0.5, rely=0.7, anchor="center")

    def start_quiz(self): #This is where the name verfication sys
        name = self.name_entry.get()
        if not name.isalpha():
            messagebox.showerror("Error", "Please enter your name.")
            return
        elif len(name)>15:
            messagebox.showerror("Error", "Please enter a name with less than or 15 characters.")
            return

        self.root.destroy()
        quiz_root = tk.Tk()
        quiz_app = QuizScreen(quiz_root, name)
        quiz_root.mainloop()

class QuizScreen:
    def __init__(self, root, name):
        self.root = root
        self.root.title("Space Quiz")
        self.root.geometry("500x500")

        self.bg = tk.PhotoImage(file="second.png")
        self.bglabel = tk.Label(self.root, image=self.bg)
        self.bglabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.name = name

        self.questions = [
            {
                "question": "Which planet is known as the Red Planet?",
                "answers": ["Mercury", "Mars", "Jupiter", "Saturn"],
                "correct_idx": 1
            },
            {
                "question": "What is the largest planet in our solar system?",
                "answers": ["Earth", "Saturn", "Jupiter", "Neptune"],
                "correct_idx": 2
            },
            {
                "question": "Who was the first human to walk on the Moon?",
                "answers": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"],
                "correct_idx": 1
            },
            {
                "question": "Which planet is known for its beautiful rings?",
                "answers": ["Mars", "Jupiter", "Saturn", "Uranus"],
                "correct_idx": 2
            }
            # Add more questions as needed
        ]

        self.current_question = 0
        self.score = 0

        self.quiz_font = ("Helvetica", 12)

        self.create_widgets()

    def create_widgets(self):
        welcome_label = tk.Label(self.root, text=f"Welcome, {self.name}!", font=("Arial", 14))
        welcome_label.pack(pady=10)

        self.question_label = tk.Label(self.root, text=self.questions[self.current_question]["question"], font=self.quiz_font)
        self.question_label.pack(pady=10)

        self.answers_var = tk.IntVar()
        self.answers_var.set(-1)  # Default value

        self.create_radio_buttons()

        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def create_radio_buttons(self):
        # Clear previous radio buttons
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Radiobutton):
                widget.destroy()

        # Create new radio buttons for the current question
        for idx, answer in enumerate(self.questions[self.current_question]["answers"]):
            tk.Radiobutton(self.root, text=answer, variable=self.answers_var, value=idx, font=self.quiz_font).pack(anchor=tk.W)

    def check_answer(self):
        selected_idx = self.answers_var.get()
        if selected_idx == -1:
            messagebox.showerror("Error", "Please select an answer.")
            return

        correct_idx = self.questions[self.current_question]["correct_idx"]
        if selected_idx == correct_idx:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_next_question()
        else:
            self.show_final_score()

    def show_next_question(self):
        self.question_label.config(text=self.questions[self.current_question]["question"])
        self.answers_var.set(-1)  # Reset selection

        self.create_radio_buttons()

    def show_final_score(self):
        messagebox.showinfo("Quiz Completed", f"Congratulations, {self.name}!\nYou have completed the quiz!\nYour final score is: {self.score}/{len(self.questions)}")
        self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    start_app = StartScreen(root)
    root.mainloop()
