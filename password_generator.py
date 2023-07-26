import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Set the window size (width x height)
app.geometry("400x250")

# Center the window on the screen
window_width = 400
window_height = 250
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set background color for the entire window
app.configure(bg="#f0f0f0")

# Password Length Label and Entry
length_label = tk.Label(app, text="Password Length:", bg="#f0f0f0", fg="#333", font=("Helvetica", 12, "bold"))
length_label.pack(pady=10)
length_entry = tk.Entry(app, font=("Helvetica", 12))
length_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(app, text="Generate Password", command=generate_password, bg="#007BFF", fg="white", font=("Helvetica", 12, "bold"))
generate_button.pack(pady=15)

# Generated Password Label
password_var = tk.StringVar()
password_label = tk.Label(app, textvariable=password_var, bg="#f0f0f0", fg="#333", font=("Helvetica", 12), wraplength=350, justify="center")
password_label.pack(pady=10)

# Start the GUI event loop
app.mainloop()
