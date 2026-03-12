import psutil


def list_processes():
    """
    Displays running processes and their CPU usage.
    """

    print("\nRunning Processes")
    print("-------------------------------------------")
    print(f"{'PID':<10}{'Name':<25}{'CPU %':<10}")
    print("-------------------------------------------")

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            pid = process.info['pid']
            name = process.info['name']
            cpu = process.info['cpu_percent']

            print(f"{pid:<10}{name:<25}{cpu:<10}")

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


if __name__ == "__main__":
    list_processes()
