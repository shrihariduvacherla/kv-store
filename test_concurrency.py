import socket
import time

hog = socket.socket()
hog.connect(('127.0.0.1', 6380))
print("Client 1 connected, holding")
time.sleep(1)

s = socket.socket()
s.settimeout(3)
s.connect(('127.0.0.1', 6380))
s.sendall(b"GET name\n")
try:
    print("Client 2 got:", s.recv(1024).decode().strip())
except socket.timeout:
    print("Client 2: NO reply in 3s")

hog.close()
print("Client 1 disconnected")
