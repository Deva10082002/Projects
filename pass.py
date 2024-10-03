import tkinter as tk
from tkinter import simpledialog

def get_password(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    password = simpledialog.askstring("Input", prompt, show='*')
    return password

password = get_password("Enter the password:")
print("Your password is:", password)
