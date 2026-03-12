import os
import shutil


def organize_files(directory):
    """
    Organizes files in a directory based on file extensions.
    """

    print("\nFile Organizer")
    print("--------------------------------")

    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Archives": [".zip", ".rar", ".7z"],
        "Scripts": [".py", ".js", ".sh"]
    }

    for filename in os.listdir(directory):

        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):

            file_ext = os.path.splitext(filename)[1].lower()

            for folder, extensions in file_types.items():

                if file_ext in extensions:

                    target_folder = os.path.join(directory, folder)

                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(file_path, os.path.join(target_folder, filename))

                    print(f"Moved {filename} → {folder}")

                    break

    print("--------------------------------\n")


if __name__ == "__main__":

    directory = input("Enter directory to organize: ")

    organize_files(directory)
