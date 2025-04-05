import tkinter as tk
import math

class BouncyBall:
    def __init__(self, master):
        self.master = master
        self.master.title("Bouncy Ball Distance")

        self.label1 = tk.Label(self.master, text="Initial height (m):")
        self.label1.pack()

        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label2 = tk.Label(self.master, text="Bounciness index (0-1):")
        self.label2.pack()

        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.label3 = tk.Label(self.master, text="Number of bounces:")
        self.label3.pack()

        self.entry3 = tk.Entry(self.master)
        self.entry3.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_distance)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def calculate_distance(self):
        try:
            height = float(self.entry1.get())
            bounciness = float(self.entry2.get())
            bounces = int(self.entry3.get())

            total_distance = height
            for _ in range(bounces):
                height *= bounciness
                total_distance += 2 * height

            self.result_label.config(text=f"Total distance traveled: {total_distance:.2f} meters")
        except ValueError:
            self.result_label.config(text="Please enter valid values.")

root = tk.Tk()
bouncy_ball = BouncyBall(root)
root.mainloop()
