#########################################
# Use this script only for Windows OS
#########################################
import os
import hashlib


def remove_files(dire, checkdir):
    for files_in_dir in os.listdir(checkdir):
        file_to_remove = os.path.join(dire, files_in_dir)
        if not os.path.exists(file_to_remove):
            os.remove(os.path.join(checkdir, files_in_dir))


def calculate_md5(data):
    with open(data, 'rb') as f:
        buffer_size = 65536
        hasher = hashlib.md5()
        while True:
            data = f.read(buffer_size)
            if not data:
                break
            hasher.update(data)
        return hasher.hexdigest()


def list_all_files(dire, replica):
    files, list_files = [], []
    if len(os.listdir(dire)) != 0:
        for content in os.listdir(dire):
            path_folder = os.path.join(dire, content)
            if os.path.isdir(path_folder):
                list_all_files(path_folder, replica + "\\" + content)
            elif os.path.isfile(path_folder):
                remove_files(dire, replica)
                files += [path_folder]
                replica_folder = os.path.join(replica, content)
                if (not os.path.exists(replica_folder)
                        or calculate_md5(path_folder) != calculate_md5(replica_folder)):
                    list_files.append(files[-1:])
        return list_files


print(list_all_files("folder_src", "folder_dst"))
