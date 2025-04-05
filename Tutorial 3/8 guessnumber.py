import tkinter as tk
from tkinter import messagebox
import random

class GuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        self.number = random.randint(1, 100)
        self.guesses = 0

        self.label = tk.Label(self.master, text="Guess a number between 1 and 100:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guesses += 1
            if guess < self.number:
                self.result_label.config(text="Too small, try again.")
            elif guess > self.number:
                self.result_label.config(text="Too large, try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.guesses} guesses!")
                self.master.quit()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

root = tk.Tk()
game = GuessGame(root)
root.mainloop()
