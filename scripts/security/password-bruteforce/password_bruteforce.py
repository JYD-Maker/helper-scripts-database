import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def bruteforce(target_hash, wordlist):
    try:
        with open(wordlist, "r") as file:
            for line in file:
                word = line.strip()
                if hash_password(word) == target_hash:
                    print(f"[FOUND] Password: {word}")
                    return
        print("Password not found ❌")
    except FileNotFoundError:
        print("Wordlist not found ❌")

if __name__ == "__main__":
    print("Password Bruteforce Simulator")
    target = input("Enter target hash: ")
    wordlist = input("Enter wordlist file: ")

    bruteforce(target, wordlist)
