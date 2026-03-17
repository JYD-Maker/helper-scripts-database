import secrets
import string


def generate_password(length=16):
    """
    Generates a secure random password.
    """

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password


if __name__ == "__main__":

    print("\nPassword Generator")
    print("--------------------------------")

    length = int(input("Enter password length: "))

    password = generate_password(length)

    print(f"\nGenerated Password:\n{password}\n")
