import socket

#ignore
MY_IP = "192.168.1.1"
MY_PORT = 21347

UDP_IP = "192.168.1.128"
UDP_RD = 21618
UDP_WR = 21623

#this is a rd of address 0 
msg = b'\x00\x00\x00\x00'

#create socket (control socket)
cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#have to bind to port to make it bidirectional
cs.bind( (MY_IP, MY_PORT) )

#now send to... 
cs.sendto( msg, (UDP_IP, UDP_RD) )

#and receive back 
data, addr = cs.recvfrom(1024)
print(data)
