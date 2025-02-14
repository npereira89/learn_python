import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Testing")

text = tk.StringVar()

# Add a label welcome
label = tk.Label(root, text="You're using Tkinter! Let's practise!")
label.pack()

# Label for name
label_name = tk.Label(root, text="Name: ")
label_name.pack(padx=1, pady=1)

# Create a Text widget
text_widget = tk.Text(root, height=1, width=15)
text_widget.pack()

# Function to print the text
def print_text():
    name = text_widget.get("1.0", "end-1c")
    messagebox.showinfo(title="Greeting", message=f"Hello, {name}")

# Create a button to trigger the function
button = tk.Button(root, text="Print", command=print_text)
button.pack()

# Run the main loop
root.mainloop()