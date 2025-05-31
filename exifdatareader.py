import exifread
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select a JPG/JPEG image",
    filetypes=[("JPEG files", "*.jpg *.jpeg")]
)

def get_exif_data_exifread(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    return tags

exif = get_exif_data_exifread(file_path)
for tag in exif:
    print(f"{tag}: {exif[tag]}")
    
input()
