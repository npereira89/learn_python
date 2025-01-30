import os, glob
import shutil
from datetime import datetime

def remove_files(fldr):
    if len(os.listdir(fldr)) > 0:
        for fi in os.listdir(fldr):
            os.unlink(os.path.join(fldr, fi))

now = datetime.now()

path_folder = input("What's the folder: ")
dst = os.path.join(os.getcwd(), "copy_gdrive")

if not os.path.exists(dst):
    os.mkdir("copy_gdrive")

remove_files(dst)

# Copy all files to zip
try:
    valid_files = [".jpg", ".jpeg", ".gif", ".png", ".rar", ".mp4", ".jfif", ".webp", ".webm", ".mov"]
    for files in os.listdir(path_folder):
        ext = os.path.splitext(files)[1]
        if ext.lower() in valid_files:
            image_path = os.path.join(path_folder, files)
            os.system(f'copy "{image_path}" "{dst}" | clip')
            os.unlink(image_path)
    print("Copy finished!!")
except OSError as e:
    print(f"{e}")

# Create and Move the file
try:
    shutil.make_archive(f"zip_file_{now.strftime('%m%d%Y_%H%M%S')}", 'zip', dst)
    zip_files_str = ", ".join(glob.glob("*.zip"))
    file_to_copy = os.path.join(os.getcwd(), f"{zip_files_str}")
    shutil.move(f"{file_to_copy}", 'C:\\Users\\Nuno\\Documents\\')
    print("Zip file done and moved with success!!")
except FileNotFoundError:
    print("Error: Zip file not found")
except Exception as e:
    print(f"An error occurred during file move: {e}")

remove_files(dst)