import os
import shutil
import tempfile


def clean_temp_folder():
    """
    Deletes files from the system temporary directory.
    """

    temp_dir = tempfile.gettempdir()

    print("\nTemporary File Cleaner")
    print("------------------------------")
    print(f"Temp Directory: {temp_dir}\n")

    deleted_files = 0

    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)

        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                deleted_files += 1

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                deleted_files += 1

        except Exception:
            continue

    print(f"Deleted items: {deleted_files}")
    print("------------------------------\n")


if __name__ == "__main__":
    clean_temp_folder()
