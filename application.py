import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from openpyxl import load_workbook
from openpyxl.styles import Border, Side
from datetime import datetime
from dateutil.relativedelta import relativedelta

def load_excel_data():
    try:
        file_xlsx = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_xlsx:
            workbook = load_workbook(file_xlsx)
            sheet = workbook.active

            label = tk.Label(text="Tabela Certificados Aforro\n", font=("Courier New", 13, "bold underline"))
            label.pack()

            # Create a Treeview widget
            tree = ttk.Treeview()
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
                tree.insert("", sheet.max_row, values=row)

            messagebox.showinfo("", "All information was loaded.")
    except Exception as e:
        messagebox.showerror("Error!!", f"Error loading Excel file: {e}")

def refresh_tree_data(file):

    workbook = load_workbook(file)
    sheet = workbook.active

    # Create a Treeview widget
    tree = ttk.Treeview()
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
        tree.insert("", sheet.max_row, values=row)

def save_excel_info():
    try:
        file_xlsx = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_xlsx:
            wb = load_workbook(file_xlsx)
            sheet_ranges = wb.active

            now = datetime.now()
            new_date = now + relativedelta(months=3)
            value_invest = value.get()

            data = [
                [now.strftime("%d/%m/%Y"), int(value_invest), new_date.strftime("%d/%m/%Y"), 0.0275, "FALSE"]
            ]

            for row in range(2, len(data) + 2):
                max_row = sheet_ranges.max_row + 1
                for col in range(1, len(data[0]) + 1):
                    sheet_ranges.cell(row=max_row, column=col).value = data[row - 2][col - 1]
                    cell = sheet_ranges.cell(row=max_row, column=col)

                    # Formatting borders data
                    cell.border = Border(top=Side(style='thin'), bottom=Side(style='thin'), left=Side(style='thin'),
                                         right=Side(style='thin'))

                    # Formatting cells
                    if col == 2 and cell.row == max_row:
                        cell.number_format = '#,##0€'
                    elif col == 4 and cell.row == max_row:  # Format tax applied
                        cell.value = round(cell.value * 100, 2)

            wb.save(file_xlsx)
            messagebox.showinfo("Success!", "The invest was added with success!")
            wb.close()

            refresh_tree_data(file_xlsx)

    except Exception as e:
        messagebox.showerror("Error!!", f"Error loading Excel file: {e}")

# Create the main window
windows = tk.Tk()
windows.title("AforroApp")
windows.iconbitmap("python_icon.ico")
windows.geometry("800x600")

# Create a menu bar
menubar = tk.Menu()
windows.config(menu=menubar)

# Create entries menu
menu = tk.Menu(menubar, tearoff=0)
menu_2 = tk.Menu(menubar, tearoff=0)

# Menu open and load data Excel file and insert new data
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="Open", command=load_excel_data)

# Menu close menu window
menubar.add_cascade(label="Windows", menu=menu_2)
menu_2.add_command(label="Exit", command=windows.quit)

label_value_invest = tk.Label(text="Value (€):")
label_value_invest.pack()

value = tk.Entry(windows)  # Create the entry widget
value.pack()

get_button = tk.Button(windows, text="OK", command=save_excel_info)  # Button to get value investments
get_button.pack()

windows.mainloop()