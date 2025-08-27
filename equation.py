###############################################################
## CALCULO DE EQUAÇÕES - APLICAÇÃO
###############################################################

import os
import tkinter as tk
from sympy import symbols, solve
from tkinter import ttk, font, messagebox

def equation_calc(frm, equ1):
    # Define the symbolic variable
    x = symbols('x')
    solution = solve(equ1, x)
    result = tk.Label(frm, text=f"The solution of equation is {solution}").grid(row=0, column=0, padx=3, pady=3)
    return result

# Create the main window
windows = tk.Tk()
windows.title("Calculo Equação")
windows.iconbitmap("185095_icon.ico")
windows.geometry("350x150")

# Define the equation (SymPy requires the equation to be equal to zero)
frm_insert = tk.Frame(windows, padx=25, pady=10)
frm_insert.pack(expand=True, fill="both")

frm_result = tk.Frame(windows, padx=50, pady=20)
frm_result.pack(expand=True, fill="both")

tk.Label(frm_insert, text="Input equation: ", fg="black", font=font.Font(weight="bold")).grid(row=0, column=0, padx=3, pady=3)
value_entry = tk.Entry(frm_insert)
value_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frm_insert, text="OK", width=2, height=1, fg="blue", command=lambda: equation_calc(frm_result, value_entry.get()), font=font.Font(weight="bold")).grid(row=0, column=2, padx=5, pady=5)

windows.mainloop()
