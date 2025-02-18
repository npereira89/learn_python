import tkinter as tk
from tkinter import ttk
from openpyxl import load_workbook
from openpyxl.styles import Border, Side
from datetime import datetime
from dateutil.relativedelta import relativedelta
from colorama import Fore, Style

def load_excel_data():
    global tree, root
    workbook = load_workbook("formatted_table.xlsx")
    sheet = workbook.active

    # Create a Treeview widget
    tree = ttk.Treeview(windows)
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

def save_excel_info():
    wb = load_workbook("formatted_table.xlsx")
    sheet_ranges = wb.active

    now = datetime.now()
    new_date = now + relativedelta(months=3)
    value_invest = int(input("Value invest: "))

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

    print(Style.BRIGHT + "The invest was added with success!")

    wb.save("formatted_table.xlsx")

    print(Style.BRIGHT + Fore.GREEN + "Document saved!")
    wb.close()
    print(Style.BRIGHT + Fore.WHITE + "Document close!")

# Create the main window
windows = tk.Tk()
windows.title("AforroApp")
windows.iconbitmap("python_icon.ico")

# Create a menu bar
menubar = tk.Menu()
windows.config(menu=menubar)

# Create entries menu
menu = tk.Menu(menubar, tearoff=0)
menu_2 = tk.Menu(menubar, tearoff=0)

# Menu open and load data Excel file and insert new data
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="Open", command=load_excel_data)
menu.add_command(label="Insert new data", command=save_excel_info)

# Menu close menu window
menubar.add_cascade(label="Windows", menu=menu_2)
menu_2.add_command(label="Exit", command=windows.quit)

windows.mainloop()