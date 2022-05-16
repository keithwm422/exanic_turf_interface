import socket
import random

HOST = "127.0.0.3"
PORT = 21623

while True: 
    print("UDP Socket is waiting for connection")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))
    cont = True
    while cont is True:
        data, addr = s.recvfrom(1024)
        print(f"Connected by {addr}")
        quit = b'q'
        newdata = ''
        #while cont is True:
        if newdata != data: 
            print("Message from client: {}".format(data))
        if len(data) != 0 and quit != data:
            ack = random.randrange(0, 10)
            # ack = 4
            if ack < 5:
                response = data
                s.sendto(response, addr)
        elif len(data) != 0 and quit == data:
            print("Connection by {} lost".format(addr))
            print()
            cont = False
        print(newdata)
        newdata = data
