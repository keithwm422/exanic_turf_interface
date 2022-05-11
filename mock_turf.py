import socket

HOST = "127.0.0.2"
PORT = 21623

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("UDP Socket is listening")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    with conn: 
        data = conn.recv(1024)  # 1024 bytes --> buffer size
        print("Message from client:", data)
        response = "Connection successful"
        conn.send(response.encode("utf-8"))
