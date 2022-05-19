import socket
import random

HOST = "127.0.0.3"
PORT = 21618

while True: 
    print("UDP Socket is waiting for connection")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        print("Message from client: {}".format(data.hex("x")))
        print()
        # ack = random.randrange(0, 10)
        ack = 4
        if ack < 5:
            response = data + b'\x11\x12\x14\x15' 
            s.sendto(response, addr)
       
