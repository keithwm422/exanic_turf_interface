import socket
import random

HOST = "127.0.0.2"
PORT = 21623
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    print("UDP Socket is waiting for connection")
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    quit = b'q'
    newdata = ''
    cont = True
    with conn:
        while cont is True:
            data = conn.recv(1024)  # 1024 bytes --> buffer size
            if newdata != data: 
                print("Message from client: {}".format(data))
            if len(data) != 0 and quit != data:
                ack = random.randrange(0, 10)
                if ack < 5:
                    response = "Connection successful"
                    conn.send(response.encode("utf-8"))
            elif len(data) != 0 and quit == data:
                print("Connection by {} lost".format(addr))
                print()
                cont = False
            newdata = data
