import turf_packet
msg = b'\x12\x00\xB1\x05'
print(msg)
# debug code if needed to check turf packet vars 
# #print(type(tag)) #print(tag) #print(type(msg)) #print(msg.hex('x'))
packet_1=turf_packet.packet(msg) # construct a 'packet' instance with an iniatilized byte array
packet_1.print_all() # print the msg and its addr and its tag
badmsg = b'\x12\x00'
badpacket=turf_packet.packet(badmsg) # construct a 'packet' instance with an iniatilized byte array
badpacket.print_all() # print the msg and its addr and its tag
print(packet_1.tag4bit)