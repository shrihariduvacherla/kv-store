import socket
import time

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 6380))
        s.sendall((command + "\n").encode())
        response = s.recv(1024).decode().strip()
        return response

print("--- Permanent key (no expiry) ---")
print(send_command("SET city hyderabad"))
print(send_command("GET city"))

print("--- Expiring key ---")
print(send_command("SET name shrihari EX 5"))
print(send_command("GET name"))
time.sleep(6)
print(send_command("GET name"))

print("--- DEL ---")
print(send_command("SET temp value1"))
print(send_command("DEL temp"))
print(send_command("GET temp"))

print("--- GET missing key ---")
print(send_command("GET nosuchkey"))