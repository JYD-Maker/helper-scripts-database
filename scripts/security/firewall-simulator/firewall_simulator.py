def check_ip(ip, blocked_ips):
    if ip in blocked_ips:
        print(f"Access denied for {ip} ❌")
    else:
        print(f"Access allowed for {ip} ✅")

if __name__ == "__main__":
    print("Firewall Simulator")

    blocked_ips = ["192.168.1.10", "10.0.0.5"]

    ip = input("Enter IP address: ")
    check_ip(ip, blocked_ips)
