import secrets

def generate_token(length=32):
    token = secrets.token_hex(length)
    print(f"Secure Token: {token}")

if __name__ == "__main__":
    print("Secure Token Generator")
    
    try:
        length = int(input("Enter token length (e.g. 16, 32): "))
        generate_token(length)
    except ValueError:
        print("Invalid input ❌")
