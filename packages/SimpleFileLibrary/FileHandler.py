#A bunch of functions that open a file/folder dialog
import tkinter as tk
from tkinter import filedialog as fd

#Prompts the user to select a single file
def open_file():
    # Create a root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    # Open the file dialog and get the selected file name
    file_name = fd.askopenfilename()
    # Return the file name
    # Destroy the root window
    root.destroy()
    return file_name

#Prompts the user to select multiple files
def open_files():
    # Create a root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    # Open the file dialog and get the selected file name
    file_name = fd.askopenfilenames()
    # Return the file name
    # Destroy the root window
    root.destroy()
    return file_name

#Prompts the user to select a folder
def open_folder():
    # Create a root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    # Open the file dialog and get the selected file name
    file_name = fd.askdirectory()
    # Return the file name
    # Destroy the root window
    root.destroy()
    return file_name

#Prompts the user to select a file of a specific type
def open_type(definition, extension):
    root = tk.Tk()
    root.withdraw()
    file_name = fd.askopenfilename(filetypes=[(definition, extension)])
    root.destroy()
    return file_name

#This is the same as the last one but it allows you to open multiple files of that type
def open_types(definition, extension):
    root = tk.Tk()
    root.withdraw()
    file_name = fd.askopenfilenames(filetypes=[(definition, extension)])
    root.destroy()
    return file_name
