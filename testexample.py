import sfc_interface_udp

msg = b"\x00\x00\x00\x00"
print("Read address 0")
read_packet = sfc_interface_udp.packet(
    msg
) 
read_packet.print_ack()