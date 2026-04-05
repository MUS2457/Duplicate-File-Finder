from DATA.input_fc import get_folder_path
from LOGIC.core import group_files_size, find_possible_duplicates, get_files
from LOGIC.tools import search_files, search_by_extension

def show_menu():
    print("\n--- File Analyzer Menu ---")
    print("1. Group files by size")
    print("2. Show possible duplicate files")
    print("3. Search file by name")
    print("4. Search files by extension")
    print("5. Number of files founded ")
    print("6. Exit")

def main():
    folder_path = get_folder_path()
    if not folder_path:
        return  # user chose exit

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            sized = group_files_size(folder_path)
            for size, files in sized.items():
                print(f"\nSize: {size} bytes")
                for file in files:
                    print(f"  {file}")

        elif choice == "2":
            duplicates = find_possible_duplicates(folder_path)
            if not duplicates:
                print("No possible duplicates found.")
            else:
                for size, files in duplicates.items():
                    print(f"\nSize: {size} bytes")
                    for file in files:
                        print(f"  {file}")

        elif choice == "3":
            results = search_files(folder_path)
            if not results:
                print("No file found with that name.")
            else:
                for size, file in results.items():
                    print(f"Found: {file} (Size: {size} bytes)")

        elif choice == "4":
            results = search_by_extension(folder_path)
            if not results:
                print("No files found with that extension.")
            else:
                for file in results:
                    print(f"  {file}")

        elif choice == "5":
            files = get_files(folder_path)
            if not files:
                print("No files found.")
            else :
                print(f"the number of files: {len(files)}")


        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1-5.")

if __name__ == "__main__":
    main()