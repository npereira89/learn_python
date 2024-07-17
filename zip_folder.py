import os
import shutil
from datetime import datetime

now = datetime.now()
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
print("This is a HTML webpage using PyScript!!")

path_folder = input("What's the folder!!")
dst = os.path.join(os.getcwd(), "copy_gdrive")

if not os.path.exists(dst):
    os.mkdir("copy_gdrive")

if len(os.listdir(dst)) > 0:
    for files in os.listdir(dst):
        os.unlink(os.path.join(dst, files))

if len(os.listdir(dst)) == 0:
    try:
        # List of file used to import for the replica folder
        valid_files = [".jpg", ".jpeg", ".gif", ".png", ".rar", ".mp4", ".jfif", ".webp"]
        for files in os.listdir(path_folder):
            ext = os.path.splitext(files)[1]
            if ext.lower() in valid_files:
                image_path = os.path.join(path_folder, files)
                os.system(f'copy "{image_path}" "{dst}" | clip')
                os.unlink(image_path)
        print("Copy finished!!")
    except OSError as e:
        print(f"{e}")

shutil.make_archive(f"zip_file_{now.strftime('%m%d%Y_%H%M%S')}", 'zip', dst)
print("Zip done!! ☺")
