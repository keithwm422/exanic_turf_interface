import sfc_interface_udp
import turf_data_intepreter

msg = b"\x00\x00\x00\x01"
print("Read address 0")
read_packet = sfc_interface_udp.packet(
    msg
)
read_packet.print_ack()

addr = read_packet.addr28bitrecd
tag = read_packet.tag4bitrecd
data = read_packet.data32bitrecd
print(hex(data))

interp_packet = turf_data_intepreter.packetparser (data, tag, addr)
