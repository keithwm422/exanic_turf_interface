import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = "Hello"
    s.send(message.encode("utf-8"))
    nmessage = s.recv(1024)
    nmessage = nmessage.decode("utf-8")
    print(f"Received {nmessage!r}")
