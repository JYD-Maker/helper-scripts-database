import os


def scan_network(base_ip):
    """
    Scans a local network by pinging IP addresses.
    """

    print("\nLocal Network Scanner")
    print("----------------------------")

    for i in range(1, 255):

        ip = f"{base_ip}.{i}"

        response = os.system(f"ping -n 1 -w 100 {ip} > nul")

        if response == 0:
            print(f"Device found: {ip}")


if __name__ == "__main__":

    print("Example network: 192.168.1")

    base_ip = input("Enter base network (without last number): ")

    scan_network(base_ip)
