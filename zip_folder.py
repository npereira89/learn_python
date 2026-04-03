import os, glob
import shutil
from datetime import datetime

def remove_files(fldr):
    if len(os.listdir(fldr)) > 0:
        for fi in os.listdir(fldr):
            os.unlink(os.path.join(fldr, fi))

def load_list_files(path_src):
    try:
        valid_files = [".jpg", ".jpeg", ".gif", ".png", ".rar", ".mp4", ".jfif", ".webp", ".webm", ".mov", ".m4v"]
        if len(os.listdir(path_src)) != 0:
            for f in os.listdir(path_src):
                ext = os.path.splitext(f)[1]
                if ext.lower() in valid_files:
                    path_f = os.path.join(path_src, f)
                    if os.path.isfile(path_f):
                        os.system(f'copy "{path_f}" "{dst}" | clip')
                        os.unlink(path_f)
                elif ext.lower() == '':
                    load_list_files(os.path.join(path_src, f))
            print("Copy finished!!")
    except OSError as e:
        print(f"{e}")

now = datetime.now()

path_folder = input("What's the folder: ")
dst = os.path.join(os.getcwd(), "copy_gdrive")

if not os.path.exists(dst):
    os.mkdir("copy_gdrive")

remove_files(dst)

# Copy all files to zip
load_list_files(path_folder)
    
# Create and Move the file
try:
    shutil.make_archive(f"zip_file_{now.strftime('%m%d%Y_%H%M%S')}", 'zip', dst)
    zip_files_str = ", ".join(glob.glob("*.zip"))
    file_to_copy = os.path.join(os.getcwd(), f"{zip_files_str}")
    shutil.move(f"{file_to_copy}", 'C:\\Users\\Nuno\\Documents\\X\\')
    print("Zip file done and moved with success!!")
except FileNotFoundError:
    print("Error: Zip file not found")
except Exception as e:
    print(f"An error occurred during file move: {e}")

remove_files(dst)