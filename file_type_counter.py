import os
import tkinter as tk
from tkinter import ttk

def count_file_types(path):
    file_types = {}

    # Iterate over all files and directories in the given path
    for root, dirs, files in os.walk(path):
        for file in files:
            # Get the file extension
            _, file_ext = os.path.splitext(file)

            # Increment the count for the file type
            if file_ext in file_types:
                file_types[file_ext] += 1
            else:
                file_types[file_ext] = 1

    return file_types

def display_table(file_types):
    root = tk.Tk()
    root.title("File Type Counts")

    # Create a treeview widget
    tree = ttk.Treeview(root)
    tree["columns"] = ("Count")
    tree.heading("#0", text="File Type")
    tree.column("#0", width=150)
    tree.heading("Count", text="Count")
    tree.column("Count", width=100)

    # Insert data into the treeview
    for file_type, count in file_types.items():
        tree.insert("", "end", text=file_type, values=(count,))

    # Pack the treeview widget
    tree.pack(expand="yes", fill="both")

    root.mainloop()

# Example usage
path = input("Enter the path: ")
file_type_counts = count_file_types(path)
display_table(file_type_counts)
