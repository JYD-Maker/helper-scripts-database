import socket


def resolve_domain(domain):
    """
    Resolves a domain name using DNS.
    """

    try:
        ip_address = socket.gethostbyname(domain)

        print("\nDNS Resolver")
        print("---------------------------")

        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")

        print("---------------------------\n")

    except socket.gaierror:
        print("Error: Unable to resolve domain.")


if __name__ == "__main__":

    domain = input("Enter domain name: ")

    resolve_domain(domain)
