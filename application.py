import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from openpyxl import load_workbook

# Function to print the text
def print_text():
    name = text_widget.get("1.0", "end-1c")
    if label_name == '':
        messagebox.showwarning(title="Greeting", message="You must input your name!!", option='OK')
    else:
        label_name_greet = tk.Label(root, text=f"Hello, {name}")
        label_name_greet.pack(padx=1, pady=1)

def load_excel_data():
    global tree, root
    workbook = load_workbook("formatted_table.xlsx")
    sheet = workbook.active

    # Create a Treeview widget
    tree = ttk.Treeview(root)
    tree.pack(expand=True, fill="both")

    # # Get column names from the first row
    columns = list(sheet.iter_rows(values_only=True))[1]

    # Configure columns
    tree["columns"] = columns
    tree["show"] = "headings"

    # Set column headings
    for col in columns:
        tree.heading(col, text=col)

    # Insert data into the Treeview
    for row in list(sheet.iter_rows(values_only=True))[2:]:
        tree.insert("", 2, values=row)

# Create the main window
root = tk.Tk()
root.title("AforroApp")
root.iconbitmap("python_icon.ico")

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

# Create a button to trigger the function
button = tk.Button(root, text="Print", command=print_text)
button.pack()

# Create a button to load the Excel file
load_button = tk.Button(root, text="Load Excel File", command=load_excel_data)
load_button.pack()

# Run the main loop
root.mainloop()