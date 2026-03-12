import os
import time

host = input("Enter host or IP: ")

while True:
    response = os.system(f"ping -n 1 {host} ^> nul")

    if response == 0:
        print(f"{host} is ONLINE")
    else:
        print(f"{host} is OFFLINE")

    time.sleep(5)
