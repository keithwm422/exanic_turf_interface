import socket

HOST = "127.0.0.2"
PORT = 21623

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("UDP Socket is listening")
    data, addr = s.recvfrom(1024)
    print(f"Connected by {addr}")
    print("Message from client:", data)
    response = "Connection successful"
    s.sendto(response.encode("utf-8"), addr)
