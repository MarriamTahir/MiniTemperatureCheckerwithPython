import tkinter as tk
from tkinter import messagebox


def check_temperature():
    try:
        temp = int(entry.get())
        if (temp >= 0 and temp <= 30):
            messagebox.showinfo(
                "Result", "The temperature outside is Good! Go Play Outside")
        else:
            messagebox.showinfo(
                "Result", "The temperature outside is not Good! Stay Home and Take Care!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


# Tkinter window setup
window = tk.Tk()
window.title("Temperature Checker")

label = tk.Label(window, text="Enter the temperature:")
label.pack()

entry = tk.Entry(window)
entry.pack()

check_button = tk.Button(window, text="Check", command=check_temperature)
check_button.pack()

window.mainloop()
