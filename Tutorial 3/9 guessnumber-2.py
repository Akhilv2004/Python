import tkinter as tk

class GuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.guesses = 0

        self.label = tk.Label(self.master, text=f"Computer's guess: {self.guess}")
        self.label.pack()

        self.too_small_button = tk.Button(self.master, text="Too small", command=self.too_small)
        self.too_small_button.pack()

        self.too_large_button = tk.Button(self.master, text="Too large", command=self.too_large)
        self.too_large_button.pack()

        self.correct_button = tk.Button(self.master, text="Correct", command=self.correct)
        self.correct_button.pack()

        self.new_game_button = tk.Button(self.master, text="New game", command=self.new_game)
        self.new_game_button.pack()
        self.new_game_button.config(state=tk.DISABLED)

    def too_small(self):
        self.low = self.guess + 1
        self.make_guess()

    def too_large(self):
        self.high = self.guess - 1
        self.make_guess()

    def correct(self):
        self.too_small_button.config(state=tk.DISABLED)
        self.too_large_button.config(state=tk.DISABLED)
        self.correct_button.config(state=tk.DISABLED)
        self.new_game_button.config(state=tk.NORMAL)

    def make_guess(self):
        self.guesses += 1
        self.guess = (self.low + self.high) // 2
        self.label.config(text=f"Computer's guess: {self.guess}")

    def new_game(self):
        self.low = 1
        self.high = 100
        self.guess = (self.low + self.high) // 2
        self.guesses = 0
        self.too_small_button.config(state=tk.NORMAL)
        self.too_large_button.config(state=tk.NORMAL)
        self.correct_button.config(state=tk.NORMAL)
        self.label.config(text=f"Computer's guess: {self.guess}")
        self.new_game_button.config(state=tk.DISABLED)

root = tk.Tk()
game = GuessGame(root)
root.mainloop()
