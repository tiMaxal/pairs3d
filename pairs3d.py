# pairs3d.py

import os
import shutil
from datetime import datetime
from tkinter import filedialog, messagebox, Tk, Label, Button, Listbox, END
from PIL import Image
import imagehash

TIME_DIFF_THRESHOLD = 2
HASH_DIFF_THRESHOLD = 10

def get_image_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

def get_image_timestamp(path):
    try:
        return datetime.fromtimestamp(os.path.getmtime(path))
    except Exception:
        return None

def is_similar_image(file1, file2):
    try:
        img1 = Image.open(file1)
        img2 = Image.open(file2)
        hash1 = imagehash.phash(img1)
        hash2 = imagehash.phash(img2)
        return abs(hash1 - hash2) < HASH_DIFF_THRESHOLD
    except Exception:
        return False

def find_pairs(image_paths):
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
    image_files = get_image_files(folder)
    pairs = find_pairs(image_files)

    pairs_dir = os.path.join(folder, 'pairs')
    singles_dir = os.path.join(folder, 'singles')
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
    root = Tk()
    root.title("pairs3d - Stereo Image Sorter")

    label = Label(root, text="Select a folder containing images to sort:")
    label.pack(pady=10)

    label_selected_folder = Label(root, text="No folder selected", fg="gray")
    label_selected_folder.pack()

    listbox_results = Listbox(root, width=40)
    listbox_results.pack(pady=10)

    def browse_folder():
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

if __name__ == '__main__':
    main()
