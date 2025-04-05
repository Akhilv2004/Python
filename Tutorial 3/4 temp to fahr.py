import tkinter as tk

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_entry.delete(0, tk.END)
        celsius_entry.insert(0, f"{celsius:.1f}")
    except ValueError:
        pass

def celsius_to_fahrenheit():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, f"{fahrenheit:.1f}")
    except ValueError:
        pass

root = tk.Tk()
root.title("Temperature Converter")

fahrenheit_label = tk.Label(root, text="Fahrenheit:")
celsius_label = tk.Label(root, text="Celsius:")

fahrenheit_entry = tk.Entry(root)
celsius_entry = tk.Entry(root)

fahrenheit_entry.insert(0, "32")
celsius_entry.insert(0, "0.0")

convert_to_celsius_button = tk.Button(root, text=">>>>", command=fahrenheit_to_celsius)
convert_to_fahrenheit_button = tk.Button(root, text="<<<<", command=celsius_to_fahrenheit)

fahrenheit_label.grid(row=0, column=0, padx=10, pady=10)
celsius_label.grid(row=0, column=1, padx=10, pady=10)

fahrenheit_entry.grid(row=1, column=0, padx=10, pady=10)
celsius_entry.grid(row=1, column=1, padx=10, pady=10)

convert_to_celsius_button.grid(row=2, column=0, padx=10, pady=10)
convert_to_fahrenheit_button.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
