import tkinter as tk
import math

def compute_square_root():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        result_label.config(text=f"Square Root: {result:.2f}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Square Root Calculator")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=10, pady=10)

compute_button = tk.Button(root, text="Compute", command=compute_square_root)
compute_button.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
