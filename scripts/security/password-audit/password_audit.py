import re

def check_strength(password):
    length = len(password) >= 12
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([length, upper, lower, digit, special])

    if score == 5:
        return "Strong 🔥"
    elif score >= 3:
        return "Medium ⚠️"
    else:
        return "Weak ❌"

def audit_file(filepath):
    try:
        with open(filepath, "r") as f:
            passwords = f.readlines()

        for pw in passwords:
            pw = pw.strip()
            if pw:
                result = check_strength(pw)
                print(f"{pw} → {result}")

    except FileNotFoundError:
        print("File not found ❌")

if __name__ == "__main__":
    print("Password Audit Tool")
    file = input("Enter password list file: ")
    audit_file(file)
