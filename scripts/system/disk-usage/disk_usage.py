import shutil


def get_disk_usage(path="/"):
    """
    Displays disk usage statistics.
    """

    total, used, free = shutil.disk_usage(path)

    total_gb = round(total / (1024**3), 2)
    used_gb = round(used / (1024**3), 2)
    free_gb = round(free / (1024**3), 2)

    print("\nDisk Usage")
    print("--------------------------")
    print(f"Path: {path}")
    print(f"Total Space: {total_gb} GB")
    print(f"Used Space: {used_gb} GB")
    print(f"Free Space: {free_gb} GB")
    print("--------------------------\n")


if __name__ == "__main__":
    get_disk_usage()
