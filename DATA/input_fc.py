def get_folder_path() :
    while True:
        user = input("Enter folder path ,or 'exit' to quit : ").strip()

        if user.lower() == 'exit' :
            return False

        elif not user :
            print("Please enter a valid folder path")
            continue

        return user

