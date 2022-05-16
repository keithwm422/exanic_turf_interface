import socket
import random

HOST = "127.0.0.2"
PORT = 21623
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print("UDP Socket is waiting for connection")
conn, addr = s.accept()
print(f"Connected by {addr}")
quit = b"q"
while True:
    data = conn.recv(1024)  # 1024 bytes --> buffer size
    print(bytes(data))
    if len(data) != 0 and quit != bytes(data):
        print("Message from client:", data)
        # ack = random.randrange(0, 10)
        ack = 6
        print(ack)
        print(type(conn))
        if ack < 5:
            response = "Connection successful"
            conn.send(response.encode("utf-8"))
    else:
        break
