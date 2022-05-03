import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("UDP Socket is listening")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn:
        message = conn.recv(1024)  # 1024 bytes --> buffer size
        message = message.decode("utf-8")
        print("Message from client:", message)
        response = "Connection successful"
        conn.send(response.encode("utf-8"))
