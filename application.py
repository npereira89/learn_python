import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font
from openpyxl import load_workbook
from openpyxl.styles import Border, Side
from datetime import datetime
from dateutil.relativedelta import relativedelta

def form_insert_data():

    for widget in windows.winfo_children():
        if widget not in (menubar, menu, menu_2):
            widget.destroy()

    label_value = tk.Label(windows, text="Value (€):", fg="black", font=font.Font(weight="bold"))
    label_value.grid(row=55)

    # Create the entry widget
    value_invest = tk.Entry(windows)
    value_invest.grid(row=55, column=19)

    # Button to get value investments
    button_submit = tk.Button(windows, text="OK", width=4, height=2, command=lambda: save_excel_info(int(value_invest.get())), fg="blue", font=font.Font(weight="bold"))
    button_submit.grid(row=55, column=20)

def on_right_click(event):
    popup_menu = tk.Menu(windows, tearoff=0)
    popup_menu.add_command(label="Do Something", command=do_something)
    popup_menu.add_command(label="Do Something Else", command=do_something_else)

def do_something():
    print("Do Something")

def do_something_else():
    print("Do Something Else")

def load_excel_data():

    for widget in windows.winfo_children():
        if widget not in (menubar, menu, menu_2):
            widget.destroy()

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

            messagebox.showinfo("SUCCESS", "All information was loaded.")
            tree.bind("<Button-3>", on_right_click)

    except Exception as e:
        messagebox.showerror("ERROR", f"Error loading Excel file: {e}")

def save_excel_info(value_invest):
    try:
        file_xlsx = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_xlsx:
            wb = load_workbook(file_xlsx)
            sheet_ranges = wb.active

            now = datetime.now()
            new_date = now + relativedelta(months=3)

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
            messagebox.showinfo("SUCCESS", "The invest was added with success!")
            wb.close()

    except Exception as e:
        messagebox.showerror("ERROR", f"Error loading Excel file: {e}")

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
menu.add_command(label="Insert data", command=form_insert_data)

# Menu close menu window
menubar.add_cascade(label="Windows", menu=menu_2)
menu_2.add_command(label="Exit", command=windows.quit)

windows.mainloop()