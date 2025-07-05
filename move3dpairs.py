import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


# This script provides a simple GUI to select a folder and duplicate its tree structure,
# copying only the '_pairs' subfolders and their contents.
# It ignores any '_singles' subfolders and creates a new tree named 'x2' + parent folder name.

def choose_folder():
    """
    Open a dialog to let the user select a folder.
    Sets the selected folder path in the folder_var StringVar.
    """
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def delete_if_empty(path):
    """
    Delete the folder at 'path' if it is empty.
    """
    if os.path.isdir(path) and not os.listdir(path):
        os.rmdir(path)

def process_tree():
    """
    Duplicate the selected folder tree, copying only subfolders named '_pairs'
    (and their files) into the new tree. Ignores subfolders named '_singles'.
    The duplicate tree is named 'x2' + parent folder name and is created
    alongside the original. After moving files, deletes any now-empty '_pairs' folders.
    """
    src_root = folder_var.get()
    if not src_root:
        messagebox.showerror("Error", "Please select a folder.")
        return

    parent_dir = os.path.dirname(src_root)
    base_name = os.path.basename(src_root)
    dst_root = os.path.join(parent_dir, f"x2{base_name}")

    if os.path.exists(dst_root):
        messagebox.showerror("Error", f"Destination '{dst_root}' already exists.")
        return

    os.makedirs(dst_root)

    for dirpath, dirnames, filenames in os.walk(src_root):
        # Remove '_singles' subfolders from the list of directories to traverse
        dirnames[:] = [d for d in dirnames if d != '_singles']

        rel_path = os.path.relpath(dirpath, src_root)
        dst_path = os.path.join(dst_root, rel_path)

        # Only process folders with a '_pairs' subfolder
        if '_pairs' in dirnames:
            pairs_src = os.path.join(dirpath, '_pairs')
            pairs_dst = os.path.join(dst_path, '_pairs')
            os.makedirs(pairs_dst, exist_ok=True)

            # Move each file from the '_pairs' subfolder to the new tree
            for item in os.listdir(pairs_src):
                src_file = os.path.join(pairs_src, item)
                dst_file = os.path.join(pairs_dst, item)
                if os.path.isfile(src_file):
                    shutil.move(src_file, dst_file)
            # After moving, delete the '_pairs' folder if it is empty
            delete_if_empty(pairs_src)

    messagebox.showinfo("Done", f"Tree duplicated at:\n{dst_root}")

def close_app():
    """
    Close the application window.
    """
    root.destroy()

# --- GUI setup ---

# Create the main application window
root = tk.Tk()
root.title("Duplicate Folder Tree (Pairs Only)")

# StringVar to hold the selected folder path
folder_var = tk.StringVar()

# GUI layout
tk.Label(root, text="Select Folder:").pack(padx=10, pady=5)
tk.Entry(root, textvariable=folder_var, width=50).pack(padx=10)
tk.Button(root, text="Browse...", command=choose_folder).pack(pady=5)
tk.Button(root, text="Start", command=process_tree).pack(pady=5)
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
# End of the script