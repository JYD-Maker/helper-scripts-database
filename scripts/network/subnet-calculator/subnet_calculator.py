import ipaddress


def calculate_subnet(network_input):
    """
    Calculates subnet information from a network address.
    """

    try:
        network = ipaddress.ip_network(network_input, strict=False)

        print("\nSubnet Information")
        print("----------------------------")

        print(f"Network Address : {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask     : {network.netmask}")
        print(f"Total Hosts     : {network.num_addresses}")
        print(f"Usable Hosts    : {network.num_addresses - 2}")

        print("----------------------------\n")

    except ValueError:
        print("Invalid network format.")


if __name__ == "__main__":

    print("\nSubnet Calculator")
    print("----------------------------")

    network_input = input("Enter network (example 192.168.1.0/24): ")

    calculate_subnet(network_input)
