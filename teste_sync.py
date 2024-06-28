import os
import hashlib
import time


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


def run_command(src_file, dir_to_send):
    # If the system is Unix-Linux must be cp command
    if os.name == "posix":
        os.system(f'cp {src_file} {dir_to_send}')
        print(f"Info: The file {src_file} was copied to {dir_to_send} successfully")
        write_to_log(f"Info: The file {src_file} was copied to {dir_to_send} successfully", log_filename)
    elif os.name == "nt":
        os.system(f'copy "{src_file}" "{dir_to_send}" | clip')
        print(f"Info: The file {src_file} was copied to {dir_to_send} successfully")
        write_to_log(f"Info: The file {src_file} was copied to {dir_to_send} successfully", log_filename)


def check_folder(folder_check):
    if not os.path.exists(folder_check):
        print(f"Error: Folder '{folder_check}' does not exist.")
        write_to_log(f"Error: Folder '{folder_check}' does not exist.", log_filename)
        return False
    else:
        return True


def replica_files_check(replica_path, source_path, source_hash_md5, files):
    full_path = os.path.join(replica_path, files)
    srcpath = os.path.dirname(source_path)
    for filesreplica in os.listdir(replica_path):
        file_path = os.path.join(srcpath, filesreplica)
        if not os.path.exists(file_path):
            rmv_file = os.path.join(replica_path, filesreplica)
            os.remove(rmv_file)
            print(f"Info: The file {filesreplica} was removed from {replica_path} successfully")
            write_to_log(f"Info: The file {filesreplica} was removed from {replica_path} successfully",
                         log_filename)

    if len(os.listdir(replica_path)) == 0:
        run_command(source_path, replica_path)
    elif os.path.exists(full_path) and os.path.isfile(full_path):
        dict_replica.append(full_path)
        for filesrep in os.listdir(replica_path):
            replica_hash_md5 = calculate_md5(full_path)
            if source_hash_md5 == replica_hash_md5 and filesrep == files:
                print(f"Error: The file {files} exists in {replica_path}")
                write_to_log(f"Error: The file {files} exists in {replica_path}", log_filename)
            elif source_hash_md5 != replica_hash_md5:
                run_command(source_path, replica_path)
    else:
        run_command(source_path, replica_path)


def create_log_file():
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")  # Get current time in format YYYY-MM-DD_HH-MM-SS
    filelog = f"log_sync_{timestamp}.txt"
    with open(filelog, 'w') as f:
        f.write("Log File Created\n")

    return filelog


def write_to_log(message, filename):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
    formatted_message = f"[{timestamp}] {message}\n"
    with open(filename, 'a') as f:
        f.write(formatted_message)


def process_file(pathto, pathfrom, namefile):
    dict_source.append(pathfrom)
    hashes = calculate_md5(pathfrom)
    dict_source_md5.append(hashes)
    replica_files_check(pathto, pathfrom, hashes, namefile)


log_filename = create_log_file()

def_source_path = input("Define please your source path: ")
def_replica_path = input("Define please your replica path: ")

check_folder(def_source_path)
check_folder(def_replica_path)

dict_source = []
dict_replica = []
dict_source_md5 = []
dict_replica_md5 = []

while True:

    try:
        # List of file used to import for the replica folder
        for file in os.listdir(def_source_path):
            SrcFilePath = os.path.join(def_source_path, file)
            if os.path.isfile(SrcFilePath):
                process_file(def_replica_path, SrcFilePath, file)
            elif os.path.isdir(SrcFilePath) and len(os.listdir(SrcFilePath)) > 0:
                create_folder = os.path.join(def_replica_path, file)
                if not os.path.exists(create_folder):
                    os.mkdir(create_folder)
                    print(f"Info: The folder {file} was created from {def_replica_path} successfully")
                    write_to_log(f"Info: The folder {file} was created from {def_replica_path} successfully",
                                 log_filename)
                    for fileSub in os.listdir(SrcFilePath):
                        SrcSubFilePath = os.path.join(SrcFilePath, fileSub)
                        if not os.path.isdir(SrcSubFilePath):

                            filePath = os.path.join(create_folder, fileSub)
                            process_file(create_folder, SrcSubFilePath, fileSub)
                        elif os.path.isdir(SrcSubFilePath) and len(os.listdir(SrcSubFilePath)) > 0:
                            sub_folder = os.path.join(create_folder, fileSub)
                            if not os.path.exists(sub_folder):
                                os.mkdir(sub_folder)
                                print(f"Info: The folder {fileSub} was created from {sub_folder} successfully")
                                write_to_log(f"Info: The folder {fileSub} was created from {sub_folder} "
                                             f"successfully", log_filename)
                                for fileNewSub in os.listdir(SrcSubFilePath):
                                    FilePathSrc = os.path.join(SrcSubFilePath, fileNewSub)
                                    if os.path.isfile(FilePathSrc):
                                        process_file(sub_folder, FilePathSrc, fileSub)
                                    elif os.path.isdir(FilePathSrc) and len(os.listdir(FilePathSrc)) > 0:
                                        NewSubSrcFilePath = os.path.join(sub_folder, fileNewSub)
                                        os.mkdir(NewSubSrcFilePath)
                                        for files in os.listdir(FilePathSrc):
                                            subfolderfile = os.path.join(FilePathSrc, files)
                                            if not os.path.isdir(subfolderfile):
                                                process_file(NewSubSrcFilePath, subfolderfile, files)
                                            elif os.path.isdir(subfolderfile) and len(os.listdir(subfolderfile)) > 0:
                                                new_sub_folder = os.path.join(create_folder, files)
                                                if not os.path.exists(new_sub_folder):
                                                    os.mkdir(new_sub_folder)
                elif os.path.exists(create_folder):
                    for fileNewSub in os.listdir(SrcFilePath):
                        SubFilePath = os.path.join(SrcFilePath, fileNewSub)
                        if not os.path.isdir(SubFilePath):
                            process_file(create_folder, SubFilePath, fileNewSub)
                        elif os.path.isdir(SubFilePath) and len(os.listdir(SubFilePath)) > 0:
                            new_sub_folder = os.path.join(create_folder, fileNewSub)
                            if not os.path.exists(new_sub_folder):
                                os.mkdir(new_sub_folder)
                                print(f"Info: The folder {fileNewSub} was created from {create_folder} "
                                      f"successfully")
                                write_to_log(f"Info: The folder {fileNewSub} was created from "
                                             f"{create_folder} "
                                             f"successfully", log_filename)
                            else:
                                for fileNewLevelSub in os.listdir(SubFilePath):
                                    NewSubFilePath = os.path.join(SubFilePath, fileNewLevelSub)
                                    if len(os.listdir(SubFilePath)) > 0:
                                        if not os.path.isdir(NewSubFilePath):
                                            filePath = os.path.join(SubFilePath, fileNewLevelSub)
                                            process_file(new_sub_folder, filePath, fileNewLevelSub)
                                        elif os.path.isdir(NewSubFilePath) and len(os.listdir(NewSubFilePath)) > 0:
                                            new_sub_under_folder = os.path.join(new_sub_folder, fileNewLevelSub)
                                            if not os.path.exists(new_sub_under_folder):
                                                os.mkdir(new_sub_under_folder)
                                                SubNewFolder = os.path.join(SubFilePath, fileNewLevelSub)
                                                print(
                                                    f"Info: The folder {fileNewLevelSub} was created from "
                                                    f"{SubFilePath} successfully")
                                                write_to_log(
                                                    f"Info: The folder {fileNewLevelSub} was created from "
                                                    f"{SubFilePath} "
                                                    f"successfully", log_filename)
                                                if len(os.listdir(SubNewFolder)) > 0:
                                                    for fileNewLevelSubFolder in os.listdir(SubNewFolder):
                                                        filePath = os.path.join(SubNewFolder, fileNewLevelSubFolder)
                                                        process_file(new_sub_under_folder, filePath,
                                                                     fileNewLevelSubFolder)
                                                elif len(os.listdir(SubNewFolder)) == 0:
                                                    for files_in_dir in os.listdir(new_sub_under_folder):
                                                        file_to_remove = os.path.join(new_sub_under_folder,
                                                                                      files_in_dir)
                                                        os.remove(file_to_remove)
                                                        print(
                                                            f"Info: The file {files_in_dir} was removed from "
                                                            f"{new_sub_under_folder} successfully")
                                                        write_to_log(
                                                            f"Info: The file {files_in_dir} was removed "
                                                            f"from {new_sub_under_folder} successfully",
                                                            log_filename)

                                            else:
                                                SubNewFolder = os.path.join(SubFilePath, fileNewLevelSub)
                                                if len(os.listdir(SubNewFolder)) > 0:
                                                    for fileNewLevelSubFolder in os.listdir(SubNewFolder):
                                                        filePath = os.path.join(SubNewFolder, fileNewLevelSubFolder)
                                                        if not os.path.isdir(filePath):
                                                            newfile = os.path.join(new_sub_under_folder,
                                                                                   fileNewLevelSubFolder)
                                                            process_file(new_sub_under_folder, filePath,
                                                                         fileNewLevelSubFolder)
                                                        else:
                                                            if len(os.listdir(filePath)) > 0:
                                                                process_file(new_sub_under_folder, filePath,
                                                                             fileNewLevelSubFolder)

                                                elif len(os.listdir(SubNewFolder)) == 0:
                                                    for files_in_dir in os.listdir(SubNewFolder):
                                                        file_to_remove = os.path.join(new_sub_under_folder,
                                                                                      files_in_dir)
                                                        os.remove(file_to_remove)
                                                        print(
                                                            f"Info: The file {files_in_dir} was removed from "
                                                            f"{new_sub_under_folder} successfully")
                                                        write_to_log(
                                                            f"Info: The file {files_in_dir} was removed "
                                                            f"from {new_sub_under_folder} successfully",
                                                            log_filename)
    except OSError as e:
        print(f"{e}")
        write_to_log(f"{e}", log_filename)

    time.sleep(3 * 60)
