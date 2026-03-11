import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip}")
    except socket.gaierror:
        print("Error: Domain could not be resolved.")

if __name__ == "__main__":
    domain = input("Enter a domain: ")
    dns_lookup(domain)
