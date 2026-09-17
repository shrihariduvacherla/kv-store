import socket
import time

def start_server(host='127.0.0.1', port=6380):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"Listening on {host}:{port}")

    while True:
        client_conn, addr = server.accept()
        handle_client(client_conn)

def handle_client(conn):
    while True:
        data = conn.recv(1024).decode().strip()
        if not data:
            break
        response = handle_command(data)
        conn.sendall((response + "\n").encode())
    conn.close()

store = {}

def handle_command(command_str):
    parts = command_str.split()
    cmd = parts[0]

    if cmd == "SET":
        key = parts[1]

        if "EX" in parts:
            value = parts[2]
            seconds = int(parts[4])
            expire_at = time.time() + seconds
            store[key] = (value, expire_at)
        else:
            value = " ".join(parts[2:])
            store[key] = (value, None)

        return "OK"

    elif cmd == "GET":
        key = parts[1]

        if key in store:
            value = store[key][0]
            expire_at = store[key][1]

            if expire_at is not None and time.time() > expire_at:
                del store[key]
                return "(nil)"

            return value
        else:
            return "(nil)"

    elif cmd == "DEL":
        key = parts[1]
        if key in store:
            del store[key]
        return "OK"

    else:
        return "ERROR unknown command"
if __name__ == "__main__":
    start_server()