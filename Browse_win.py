# browse_file_win.py
import tkinter as tk
from tkinter import filedialog

def browse_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    try:
        file_path = filedialog.askopenfilename()  # Open the file dialog
        
        if file_path:  # Check if a file was selected
            print("Selected file:", file_path)
            return file_path
        else:
            print("No file selected.")
            return None
    except Exception as e:
        print(e)