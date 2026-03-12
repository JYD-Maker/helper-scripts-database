def analyze_log(file_path, keyword):
    """
    Searches a log file for lines containing a specific keyword.
    """

    print("\nLog Analyzer")
    print("--------------------------------")

    matches = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as log_file:

            for line_number, line in enumerate(log_file, start=1):

                if keyword.lower() in line.lower():
                    matches.append((line_number, line.strip()))

        if matches:
            print(f"\nFound {len(matches)} matching entries:\n")

            for line_number, text in matches:
                print(f"[Line {line_number}] {text}")

        else:
            print("No matching entries found.")

    except FileNotFoundError:
        print("Log file not found.")

    print("--------------------------------\n")


if __name__ == "__main__":

    log_file = input("Enter log file path: ")
    keyword = input("Enter keyword to search for: ")

    analyze_log(log_file, keyword)
