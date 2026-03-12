import psutil


def check_services():
    """
    Lists Windows services and their status.
    """

    print("\nService Checker")
    print("-------------------------------------------")
    print(f"{'Service Name':<35}{'Status':<15}")
    print("-------------------------------------------")

    try:
        for service in psutil.win_service_iter():

            service_info = service.as_dict()

            name = service_info['name']
            status = service_info['status']

            print(f"{name:<35}{status:<15}")

    except Exception as error:
        print("Error retrieving services.")
        print(error)

    print("-------------------------------------------\n")


if __name__ == "__main__":
    check_services()
