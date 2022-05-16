import socket

HOST = "127.0.0.2"
PORT = 21623

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    message =  b"\x12\x55\xB1\xA5"
    s.send(message)
    nmessage = s.recv(1024)
    nmessage = nmessage.decode("utf-8")
    print(f"Received {nmessage!r}")

