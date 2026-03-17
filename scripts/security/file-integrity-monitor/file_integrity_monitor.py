import hashlib
import json
import os

BASELINE_FILE = "baseline.json"

def hash_file(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline(directory):
    baseline = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            file_hash = hash_file(path)
            if file_hash:
                baseline[path] = file_hash

    with open(BASELINE_FILE, "w") as f:
        json.dump(baseline, f, indent=4)

    print("Baseline created ✅")

def check_integrity():
    if not os.path.exists(BASELINE_FILE):
        print("No baseline found ❌")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    for path, old_hash in baseline.items():
        new_hash = hash_file(path)

        if new_hash is None:
            print(f"[DELETED] {path}")
        elif new_hash != old_hash:
            print(f"[MODIFIED] {path}")
        else:
            print(f"[OK] {path}")

if __name__ == "__main__":
    print("File Integrity Monitor")
    print("1 = Create baseline")
    print("2 = Check integrity")

    choice = input("Select option: ")

    if choice == "1":
        directory = input("Enter directory path: ")
        create_baseline(directory)
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid option")
