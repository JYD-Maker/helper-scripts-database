import os
import stat

def check_permissions(filepath):
    try:
        file_stat = os.stat(filepath)

        print("File Permission Checker")
        print(f"File: {filepath}")

        if file_stat.st_mode & stat.S_IRUSR:
            print("Readable ✅")
        else:
            print("Not readable ❌")

        if file_stat.st_mode & stat.S_IWUSR:
            print("Writable ✅")
        else:
            print("Not writable ❌")

        if file_stat.st_mode & stat.S_IXUSR:
            print("Executable ✅")
        else:
            print("Not executable ❌")

    except FileNotFoundError:
        print("File not found ❌")

if __name__ == "__main__":
    file = input("Enter file path: ")
    check_permissions(file)
