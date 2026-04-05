import os
from LOGIC.core import get_files


def search_files(folder_path):

    files = get_files(folder_path)

    if not files:
        return []

    while True:
        user = input("Please enter a file name to search or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Exiting...")
            break

        elif not user:
            print("Please enter a valid file name or 'exit' to quit")
            continue

        result = []

        for file in files:
            filename = os.path.basename(file)  # extract file name from the path

            if user.lower() in filename.lower():
                result.append(file)

        return result

def search_by_extension(folder_path):
    files = get_files(folder_path)
    results = []

    if not files:
        return []

    while True:
        user = input("Please enter a file extension ex :(.py, .png) to search or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Exiting...")
            break

        elif not user:
            print("Please enter a valid file extension or 'exit' to quit")
            continue

        for file in files:

            filename = os.path.basename(file)
            _, extension = os.path.splitext(filename)

            if user.lower() == extension.lower():
                results.append(file)

        return results



