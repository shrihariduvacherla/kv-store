import socket

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 6380))
        s.sendall((command + "\n").encode())
        response = s.recv(1024).decode().strip()
        return response

if __name__ == "__main__":
    print(send_command("SET name shrihari"))
    print(send_command("GET name"))
    print(send_command("GET missing"))
    print(send_command("DEL name"))
    print(send_command("GET name"))