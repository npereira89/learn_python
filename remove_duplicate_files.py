import argparse
import os
import hashlib

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

def remove_file(directory):
    if calculate_md5(directory) in list_md5:
        os.remove(directory)
    else:
        list_md5.append(calculate_md5(directory))

def get_files(folder):
    if len(os.listdir(folder))>0:
        for f in os.listdir(folder):
            image_path = os.path.join(folder, f)
            if os.path.isdir(image_path):
                get_files(image_path)
            else:
                remove_file(image_path)
    else:
        exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path")
args = parser.parse_args()

list_md5 = []
path = args.path

if len(os.listdir(path))>0:
    get_files(path)
    print("Done!!")
else:
    exit(0)