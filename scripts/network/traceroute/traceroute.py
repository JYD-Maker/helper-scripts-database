import subprocess


def run_traceroute(host):
    """
    Runs a traceroute to the specified host.
    """

    print("\nTraceroute Tool")
    print("-----------------------------")

    try:
        subprocess.run(["tracert", host])
    except Exception as error:
        print("Error running traceroute:")
        print(error)


if __name__ == "__main__":

    target = input("Enter a host or IP address: ")

    run_traceroute(target)
