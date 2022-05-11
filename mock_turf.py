import socket
import random

HOST = "127.0.0.2"
PORT = 21623

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    print("UDP Socket is listening")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn:
        data = conn.recv(1024)  # 1024 bytes --> buffer size
        print("Message from client:", data)
        ack = random.randrange(0, 10)
        # ack = 6
        print(ack)
        if ack < 5:
            response = "Connection successful"
            conn.send(response.encode("utf-8"))
