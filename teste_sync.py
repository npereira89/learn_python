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


###
# https://gist.github.com/allanfreitas/e2cd0ff49bbf7ddf1d85a3962d577dbf
# to get some information about loop for execute something between
###

def replica_files_check(replica_path, source_path, source_hash_md5, files):
    if len(os.listdir(replica_path)) == 0:
        run_command(source_path, replica_path)
    else:
        full_path = os.path.join(replica_path, files)
        srcpath = os.path.dirname(source_path)
        for filesReplica in os.listdir(replica_path):
            file_path = os.path.join(srcpath, filesReplica)
            if not os.path.exists(file_path):
                rmv_file = os.path.join(replica_path, filesReplica)
                os.remove(rmv_file)
                print(f"Info: The file {filesReplica} was removed from {replica_path} successfully")
                write_to_log(f"Info: The file {filesReplica} was removed from {replica_path} successfully",
                             log_filename)
        if os.path.exists(full_path):
            if os.path.isfile(full_path):
                dict_replica.append(full_path)
                for filesRep in os.listdir(replica_path):
                    if filesRep == files:
                        replica_hash_md5 = calculate_md5(full_path)
                        if source_hash_md5 == replica_hash_md5:
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
                dict_source.append(SrcFilePath)
                md5_hash = calculate_md5(SrcFilePath)
                dict_source_md5.append(md5_hash)
                replica_files_check(def_replica_path, SrcFilePath, md5_hash, file)
            elif os.path.isdir(SrcFilePath):
                if len(os.listdir(SrcFilePath)) == 0:
                    pass
                else:
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
                                dict_source.append(SrcSubFilePath)
                                md5_hash = calculate_md5(SrcSubFilePath)
                                dict_source_md5.append(md5_hash)
                                replica_files_check(create_folder, SrcSubFilePath, md5_hash, fileSub)
                            elif os.path.isdir(SrcSubFilePath):
                                sub_folder = os.path.join(create_folder, fileSub)
                                if not os.path.exists(sub_folder):
                                    os.mkdir(sub_folder)
                                    print(f"Info: The folder {fileSub} was created from {sub_folder} successfully")
                                    write_to_log(f"Info: The folder {fileSub} was created from {sub_folder} "
                                                 f"successfully", log_filename)
                                    for fileNewSub in os.listdir(SrcSubFilePath):
                                        FilePathSrc = os.path.join(SrcSubFilePath, fileNewSub)
                                        if os.path.isfile(FilePathSrc):
                                            dict_source.append(FilePathSrc)
                                            md5_hash = calculate_md5(FilePathSrc)
                                            dict_source_md5.append(md5_hash)
                                            replica_files_check(sub_folder, FilePathSrc, md5_hash, fileSub)
                                        elif os.path.isdir(FilePathSrc):
                                            NewSubSrcFilePath = os.path.join(sub_folder, fileNewSub)
                                            os.mkdir(NewSubSrcFilePath)
                                            for files in os.listdir(FilePathSrc):
                                                subfolderfile = os.path.join(FilePathSrc, files)
                                                dict_source.append(subfolderfile)
                                                md5_hash = calculate_md5(subfolderfile)
                                                dict_source_md5.append(md5_hash)
                                                replica_files_check(NewSubSrcFilePath, subfolderfile, md5_hash,
                                                                    files)
                    elif os.path.exists(create_folder):
                        for fileNewSub in os.listdir(SrcFilePath):
                            SubFilePath = os.path.join(SrcFilePath, fileNewSub)
                            if not os.path.isdir(SubFilePath):
                                dict_source.append(SubFilePath)
                                md5_hash = calculate_md5(SubFilePath)
                                dict_source_md5.append(md5_hash)
                                replica_files_check(create_folder, SubFilePath, md5_hash, fileNewSub)
                            elif os.path.isdir(SubFilePath):
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
                                                dict_source.append(filePath)
                                                md5_hash = calculate_md5(filePath)
                                                dict_source_md5.append(md5_hash)
                                                replica_files_check(new_sub_folder, filePath, md5_hash,
                                                                    fileNewLevelSub)
                                            else:
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
                                                            dict_source.append(filePath)
                                                            md5_hash = calculate_md5(fileNewLevelSubFolder)
                                                            dict_source_md5.append(md5_hash)
                                                            replica_files_check(new_sub_under_folder, filePath,
                                                                                md5_hash,
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
                                                            dict_source.append(filePath)
                                                            md5_hash = calculate_md5(filePath)
                                                            dict_source_md5.append(md5_hash)
                                                            replica_files_check(new_sub_under_folder, filePath,
                                                                                md5_hash,
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
