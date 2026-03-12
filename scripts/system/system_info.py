import platform
import socket
import psutil


def get_system_information():
    """
    Displays basic system information such as OS, CPU and RAM.
    """

    print("\nSystem Information")
    print("--------------------------------")

    # Hostname
    print(f"Hostname: {socket.gethostname()}")

    # Operating System
    print(f"Operating System: {platform.system()} {platform.release()}")

    # Processor
    print(f"Processor: {platform.processor()}")

    # CPU
    print(f"CPU Cores (Physical): {psutil.cpu_count(logical=False)}")
    print(f"CPU Threads (Logical): {psutil.cpu_count(logical=True)}")

    # Memory
    memory = psutil.virtual_memory()

    total_ram = round(memory.total / (1024 ** 3), 2)
    available_ram = round(memory.available / (1024 ** 3), 2)

    print(f"Total RAM: {total_ram} GB")
    print(f"Available RAM: {available_ram} GB")

    print("--------------------------------\n")


if __name__ == "__main__":
    get_system_information()
