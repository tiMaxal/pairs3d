"""
pairs3d.py

A utility for sorting stereo image pairs in a folder.
Pairs are detected based on file modification timestamps and perceptual image similarity.
Pairs are moved into a 'pairs' subfolder, and unpaired images into a 'singles' subfolder.
A simple Tkinter GUI allows users to select a folder and view results.
"""


"""
original ai prompt [20250624]:

 a way to separate pairs from folders also containing singles .. software that compares for image-similarity and closeness of time-created

"""


import os
import shutil
from tkinter import filedialog, messagebox, Tk, Label, Button, Listbox, END
from datetime import datetime
from PIL import Image
import imagehash

TIME_DIFF_THRESHOLD = 2
HASH_DIFF_THRESHOLD = 10


def get_image_files(directory):
    """
    Retrieve a list of image file paths from the given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        list: List of image file paths with extensions .jpg, .jpeg, or .png.
    """
    return [
        os.path.join(directory, f)
        for f in os.listdir(directory)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]


def get_image_timestamp(path):
    """
    Get the modification timestamp of an image file.

    Args:
        path (str): Path to the image file.

    Returns:
        datetime or None: Modification time as a datetime object, or None if unavailable.
    """
    try:
        return datetime.fromtimestamp(os.path.getmtime(path))
    except Exception:
        return None


def is_similar_image(file1, file2):
    """
    Determine if two images are perceptually similar using phash.

    Args:
        file1 (str): Path to the first image.
        file2 (str): Path to the second image.

    Returns:
        bool: True if images are similar within the hash threshold, False otherwise.
    """
    try:
        img1 = Image.open(file1)
        img2 = Image.open(file2)
        hash1 = imagehash.phash(img1)
        hash2 = imagehash.phash(img2)
        return abs(hash1 - hash2) < HASH_DIFF_THRESHOLD
    except Exception:
        return False


def find_pairs(image_paths):
    """
    Find and return pairs of images that are close in time and visually similar.

    Args:
        image_paths (list): List of image file paths.

    Returns:
        list: List of tuples, each containing two paired image paths.
    """
    image_paths.sort(key=get_image_timestamp)
    used = set()
    pairs = []
    for i, path1 in enumerate(image_paths):
        if path1 in used:
            continue
        time1 = get_image_timestamp(path1)
        for j in range(i + 1, len(image_paths)):
            path2 = image_paths[j]
            if path2 in used:
                continue
            time2 = get_image_timestamp(path2)
            if time2 and abs((time2 - time1).total_seconds()) <= TIME_DIFF_THRESHOLD:
                if is_similar_image(path1, path2):
                    pairs.append((path1, path2))
                    used.add(path1)
                    used.add(path2)
                    break
    return pairs


def sort_images(folder):
    """
    Sort images in the given folder into 'pairs' and 'singles' subfolders.

    Args:
        folder (str): Path to the folder containing images.

    Returns:
        tuple: (number of pairs moved, number of singles moved)
    """
    image_files = get_image_files(folder)
    pairs = find_pairs(image_files)
    pairs_dir = os.path.join(folder, "pairs")
    singles_dir = os.path.join(folder, "singles")
    os.makedirs(pairs_dir, exist_ok=True)
    os.makedirs(singles_dir, exist_ok=True)
    paired_files = set([f for pair in pairs for f in pair])
    for pair in pairs:
        for file in pair:
            shutil.move(file, os.path.join(pairs_dir, os.path.basename(file)))
    for file in image_files:
        if file not in paired_files:
            shutil.move(file, os.path.join(singles_dir, os.path.basename(file)))
    return len(pairs), len(image_files) - len(paired_files)


def main():
    """
    Launch the Tkinter GUI for selecting a folder and sorting images.
    """
    root = Tk()
    root.title("pairs3d - Stereo Image Sorter")
    label = Label(root, text="Select a folder containing images to sort:")
    label.pack(pady=10)
    label_selected_folder = Label(root, text="No folder selected", fg="gray")
    label_selected_folder.pack()
    listbox_results = Listbox(root, width=40)
    listbox_results.pack(pady=10)

    def browse_folder():
        """
        Handle folder selection, sorting, and displaying results in the GUI.
        """
        folder = filedialog.askdirectory()
        if not folder:
            return
        label_selected_folder.config(text=folder)
        pairs, singles = sort_images(folder)
        listbox_results.delete(0, END)
        listbox_results.insert(END, f"Pairs moved: {pairs}")
        listbox_results.insert(END, f"Singles moved: {singles}")
        messagebox.showinfo("Done", f"Sorted {pairs} pairs and {singles} singles.")

    button_browse = Button(root, text="Browse", command=browse_folder)
    button_browse.pack(pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
