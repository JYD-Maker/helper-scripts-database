import psutil
import datetime


def get_system_uptime():
    """
    Displays how long the system has been running.
    """

    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)

    now = datetime.datetime.now()
    uptime = now - boot_time

    print("\nSystem Uptime")
    print("--------------------------------")
    print(f"System started at: {boot_time}")
    print(f"Uptime: {uptime}")
    print("--------------------------------\n")


if __name__ == "__main__":
    get_system_uptime()
