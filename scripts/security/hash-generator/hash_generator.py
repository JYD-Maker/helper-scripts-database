import hashlib


def generate_hash(text, algorithm="sha256"):
    """
    Generates a hash for the given text using the selected algorithm.
    """

    try:
        hash_object = hashlib.new(algorithm)
        hash_object.update(text.encode())

        return hash_object.hexdigest()

    except ValueError:
        return "Invalid hashing algorithm."


if __name__ == "__main__":

    print("\nHash Generator")
    print("--------------------------------")

    text = input("Enter text: ")
    algorithm = input("Enter algorithm (md5, sha1, sha256): ").lower()

    result = generate_hash(text, algorithm)

    print(f"\nHash ({algorithm}):\n{result}\n")
