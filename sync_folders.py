#########################################
# Use this script only for Windows OS
#########################################
import os
import hashlib
import time


def remove_files(dire, check_dir):
    for files_in_dir in os.listdir(check_dir):
        file_to_remove = os.path.join(dire, files_in_dir)
        if not os.path.exists(file_to_remove):
            os.remove(os.path.join(check_dir, files_in_dir))
            print(f"Removing... {os.path.join(check_dir, files_in_dir)}")


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
    files = []
    if len(os.listdir(dire)) != 0:
        remove_files(dire, replica)
        for content in os.listdir(dire):
            path_folder = os.path.join(dire, content)
            replica_folder = os.path.join(replica, content)
            if len(os.listdir(path_folder)) != 0 and not os.path.exists(replica_folder):
                os.mkdir(replica_folder)
            elif os.path.isdir(path_folder):
                list_all_files(path_folder, replica_folder)
            elif os.path.isfile(path_folder):
                files += [path_folder]
                replica_folder = os.path.join(replica, content)
                if not os.path.exists(replica_folder) or calculate_md5(path_folder) != calculate_md5(replica_folder):
                    os.system(f"copy {path_folder} {replica} | clip")
                    print(f"Copying... {path_folder}")
        return files[-1:]

while True:
    print("Beginning...\n")
    list_all_files("src", "dst")
    time.sleep(3 * 60)
