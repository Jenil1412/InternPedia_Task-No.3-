
import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    if strength_var.get() == "Weak":
        characters = string.ascii_lowercase
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Password Generator", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack(pady=5)

length_label = tk.Label(length_frame, text="Password Length:", bg="#f0f0f0")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame)
length_entry.pack(side=tk.LEFT, padx=5)
length_entry.insert(0, "12")  # Default length

strength_frame = tk.Frame(root, bg="#f0f0f0")
strength_frame.pack(pady=5)

strength_label = tk.Label(strength_frame, text="Password Strength:", bg="#f0f0f0")
strength_label.pack(side=tk.LEFT, padx=5)

strength_var = tk.StringVar(value="Strong")
weak_radio = tk.Radiobutton(strength_frame, text="Weak", variable=strength_var, value="Weak", bg="#f0f0f0")
weak_radio.pack(side=tk.LEFT, padx=5)
strong_radio = tk.Radiobutton(strength_frame, text="Strong", variable=strength_var, value="Strong", bg="#f0f0f0")
strong_radio.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="white", font=("Helvetica", 12))
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
password_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196f3", fg="white", font=("Helvetica", 12))
copy_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
