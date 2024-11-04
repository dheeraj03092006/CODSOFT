import tkinter as tk
from tkinter import StringVar, messagebox
import random
import string

# Function to generate random password
def generate_password():
    password_length = length_var.get()  # Retrieve the value from length_var

    if password_length.isdigit():
        password_length = int(password_length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length")

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Password Copied", "Password copied to clipboard")

# Create GUI
root = tk.Tk()
root.title("Random Password Generator")
root.geometry('400x400')
root.configure(bg="black")

label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 12, "bold")
button_font = ("Helvetica", 12, "bold")

# Title label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="black", fg="yellow")
title_label.pack(pady=10)

# Password length input
length_frame = tk.Frame(root, bg="black")
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Password Length", font=label_font, bg="white", fg="red")
length_label.grid(row=0, column=0, padx=5)

length_var = StringVar()  # Define length_var as a StringVar
length_entry = tk.Entry(length_frame, textvariable=length_var, font=entry_font, width=5)
length_entry.grid(row=0, column=1, padx=5)

# Password display
password_frame = tk.Frame(root, bg="black")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Generated Password", font=label_font, bg="black", fg="green")
password_label.grid(row=0, column=0, padx=10)

password_entry = tk.Entry(password_frame, font=entry_font, width=25, bg="purple")
password_entry.grid(row=0, column=1)

# Buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

generate_button = tk.Button(button_frame, text="Generate Password", font=button_font, bg="white", fg="black", command=generate_password)
generate_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(button_frame, text="Copy to Clipboard", font=button_font, bg="white", fg="black", command=copy_to_clipboard)
copy_button.grid(row=0, column=1, padx=10)

# Footer label
footer_label = tk.Label(root, text="Copyright © 2024 Dheeraj Soma", font=("Helvetica", 10), bg="black", fg="white")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
