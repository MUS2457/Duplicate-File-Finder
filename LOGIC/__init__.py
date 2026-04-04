import os

def get_files(folder_path) :
    list_of_files = []

    for files in os.listdir(folder_path):
        current_path = os.path.join(folder_path, files)

        if os.path.isfile(current_path):
            list_of_files.append(current_path)

    return list_of_files

def group_files_size(folder_path):
    list_of_files = get_files(folder_path)

    if not list_of_files:
        return {}

    files = {}

    for file in list_of_files:
        size = os.path.getsize(file)

        if size not in files:
            files[size] = []

        files[size].append(file)

    return files





