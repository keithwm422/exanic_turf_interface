import turf_data_intepreter

ADDR_C = b"\x0F\xFF\xFF\xFF"  # this is a bytes class
ADDR_bytearray = 0x0FFFFFFF  # this is a bytes ARRAY
TAG_C = b"\xF0\x00\x00\x00"  # this is a bytes class
TAG_bytearray = 0b11110000  # this is a bytes class ARRAY
TAG_REC = b"\x00\x00\x00\x00\xF0\x00\x00\x00"
TAG_REC_bytearray = 0x00000000F000
ADDR_REC = b"\x00\x00\x00\x00\x0F\xFF\xFF\xFF"
ADDR_REC_bytearray = 0x0FFFFFFF
DATA_REC = b"\xFF\xFF\xFF\xFF\x00\x00\x00\x00"
DATA_REC_bytearray = 0xFFFFFFFF
ENDI = "little"
msg = b"\x10\x00\x00\x01"  # Bits 31:28 are tag, 27:0 are address
data = b"\x2c\xa5\x00\x05"
# data = b"\x54\x55\x52\x46"
bytestr = data + msg

address = (int.from_bytes(bytestr, ENDI) & int.from_bytes(ADDR_REC, ENDI)).to_bytes(
    (len(bytestr)), ENDI
)

addr28bitrecd = (
    (address[4]) << 24 | (address[5] << 16) | (address[6] << 8) | address[7]
) & ADDR_bytearray
 
tag = (int.from_bytes(bytestr, ENDI) & int.from_bytes(TAG_REC, ENDI)).to_bytes(
    (len(bytestr)), ENDI
)



tag4bitrecd = tag[4] & TAG_bytearray


data = (int.from_bytes(bytestr, ENDI) & int.from_bytes(DATA_REC, ENDI)).to_bytes(
    (len(bytestr)), ENDI
)

data32bitrecd = (
    (data[0] << 24) | (data[1] << 16) | (data[2] << 8) | data[3]
) & DATA_REC_bytearray


value = turf_data_intepreter.packetparser(data32bitrecd, tag4bitrecd, addr28bitrecd)


value = ('{:032b}'.format(int(data32bitrecd)))
year = value[0:7]
month =value[7:11]
day = value[11:16]
