import sfc_interface_udp


msg = b"\x12\x55\xB1\xA5"  # Bits 31:28 are tag, 27:0 are address
data = b"\x15\x26\x37\x48"
# so far a bad message still does a read by default of addr: 0x0000000 with tag 0x0
badmsg = b"\x12\x00"
badpacket = sfc_interface_udp.packet(
    badmsg
)  # construct a 'packet' instance with an iniatilized byte array
badpacket.print_all()  # print the msg and its addr and its tag
print()
# print(msg.hex())
# debug code if needed to check turf packet vars
# print(type(tag)) #print(tag) #print(type(msg)) #print(msg.hex('x'))

read_packet_1 = sfc_interface_udp.packet(
    msg
)  # construct a 'packet' instance with an iniatilized byte array
read_packet_1.print_all()  # print the hdr and its addr and its tag
print()
# print(hex(read_packet_1.tag4bit))  # get them as byte arrays
# print(hex(read_packet_1.addr28bit))  # get them as byte arrays
read_packet_1.print_rd()
read_packet_1.print_ack()
print()

msg = b"\x12\x55\xB1\xA5"  # Bits 31:28 are tag, 27:0 are address
data = b"\x15\x26\x37\x48"

write_packet_1 = sfc_interface_udp.packet(
    msg, data
)  # construct a 'packet' instance with an iniatilized byte array
write_packet_1.print_all()
print()
# print(hex(write_packet_1.addr28bit))
# print(hex(write_packet_1.tag4bit))
write_packet_1.print_wr()
write_packet_1.print_ack()

