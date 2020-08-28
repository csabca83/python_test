import os
import winsound
import time

ip_list = ["8.8.8.8", "8.8.4.4"]

while True:
    for ip in ip_list:
        response = os.popen(f"ping {ip}").read()
        if f"Reply from {ip}: bytes=32" in response:
            print(f"Network is up, ping on {ip} was successful.")
            winsound.Beep(450, 250)
        else:
            print(f"Network is down, {ip} unreachable.")