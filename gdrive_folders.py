import os
import shutil
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from gdown.download_folder import download_folder

link = "https://drive.google.com/drive/folders/"

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
now = datetime.now()

file_list = drive.ListFile({'q': " title='Fotos'"}).GetList()
tmp_dir = os.path.join(os.getcwd(), "gdrive_folder")

for file1 in file_list:
    link = link + file1['id']
    download_folder(url=link, output=tmp_dir, skip_download=False, use_cookies=False)

shutil.make_archive(f"zip_file_{now.strftime('%m%d%Y_%H%M%S')}", 'zip', tmp_dir)
