import hashlib
import json
import os

DB_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as file:
        return json.load(file)

def save_users(users):
    with open(DB_FILE, "w") as file:
        json.dump(users, file, indent=4)

def register():
    users = load_users()
    username = input("Enter username: ")

    if username in users:
        print("User already exists ❌")
        return

    password = input("Enter password: ")
    users[username] = hash_password(password)
    save_users(users)

    print("User created ✅")

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    if username in users and users[username] == hashed:
        print("Login successful 🔓")
    else:
        print("Login failed ❌")

if __name__ == "__main__":
    print("Login System")
    print("1 = Register")
    print("2 = Login")

    choice = input("Select option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    else:
        print("Invalid option")
