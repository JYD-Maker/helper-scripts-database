import psutil
import time


def monitor_cpu(interval=2):
    """
    Displays CPU usage in real time.
    """

    print("\nCPU Monitor")
    print("------------------------------")
    print("Press CTRL + C to stop\n")

    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=interval)

            print(f"CPU Usage: {cpu_percent}%")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    monitor_cpu()
