import base64

def encode_text(text):
    encoded = base64.b64encode(text.encode()).decode()
    print(f"Encoded: {encoded}")

def decode_text(text):
    try:
        decoded = base64.b64decode(text.encode()).decode()
        print(f"Decoded: {decoded}")
    except:
        print("Invalid Base64 input ❌")

if __name__ == "__main__":
    print("Base64 Tool")
    print("1 = Encode")
    print("2 = Decode")

    choice = input("Select option: ")

    if choice == "1":
        text = input("Enter text: ")
        encode_text(text)
    elif choice == "2":
        text = input("Enter Base64: ")
        decode_text(text)
    else:
        print("Invalid option")
