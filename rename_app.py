import os
import tkinter as tk
from tkinter import messagebox

def populate_file_photo_tree(path):
    valid_files = [".jpg", ".gif", ".png", ".jpeg", ".webp"]
    clear_window()
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() in valid_files:
            image_path = os.path.join(path, f)
            if os.path.isfile(image_path):
                try:
                    label_photo = tk.Label(windows, text=f"{image_path}")
                    label_photo.pack()
                except Exception as e:
                    messagebox.showerror("Error load data..", f"An unexpected error occurred: {e}")

def populate_file_video_tree(path):
    valid_files = [".mov", ".mp4"]
    clear_window()
    for f in os.listdir(path):
        ext = os.path.splitext(f)[1]
        if ext.lower() in valid_files:
            image_path = os.path.join(path, f)
            if os.path.isfile(image_path):
                try:
                    label_video = tk.Label(windows,text=f"{image_path}")
                    label_video.pack()
                except Exception as e:
                    messagebox.showerror("Error load data..", f"An unexpected error occurred: {e}")

def clear_window():
    for widget in windows.winfo_children():
        if widget not in (menubar, menu, menu_2):
            widget.destroy()

folder = "C:/Users/Nuno/Downloads/"

# Create the main window
windows = tk.Tk()
windows.title("Change Name")
windows.iconbitmap("185095_icon.ico")
windows.geometry("800x600")

# Create a menu bar
menubar = tk.Menu()
windows.config(menu=menubar)

# Create entries menu
menu = tk.Menu(menubar, tearoff=0)
menu_2 = tk.Menu(menubar, tearoff=0)

# Menu open and load data Excel file and insert new data
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="Load Foto", command=lambda: populate_file_photo_tree(folder))
menu.add_command(label="Load Videos", command=lambda: populate_file_video_tree(folder))

# Menu close menu window
menubar.add_cascade(label="Windows", menu=menu_2)
menu_2.add_command(label="Exit", command=windows.quit)

windows.mainloop()