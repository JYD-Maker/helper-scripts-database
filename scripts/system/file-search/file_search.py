import os


def search_files(directory, keyword):
    """
    Searches for files containing a specific keyword in their name.
    """

    print("\nFile Search")
    print("--------------------------------")

    matches = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword.lower() in file.lower():
                full_path = os.path.join(root, file)
                matches.append(full_path)

    if matches:
        print("Matching files:\n")
        for match in matches:
            print(match)
    else:
        print("No matching files found.")

    print("--------------------------------\n")


if __name__ == "__main__":

    directory = input("Enter directory to search: ")
    keyword = input("Enter file name keyword: ")

    search_files(directory, keyword)
