import tkinter as tk

def convert_to_uppercase():
    input_string = entry.get()
    result_label.config(text=input_string.upper())

root = tk.Tk()
root.title("String to Uppercase")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_to_uppercase)
convert_button.grid(row=1, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, padx=10, pady=10)

root.mainloop()
