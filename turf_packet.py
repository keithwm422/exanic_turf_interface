# class for turf packet interface, bytes object is created at initialization, 4 bytes long only or else 4 bytes of all 0.
# to get just a byte from a bytes object, .,...
# eventually, need a packet class that expands on this, initializing with zero-filled bytes object of max length: bytes(MAX_LENGTH)
ADDR_C = b'\xFF\xFF\xFF\xF0'
TAG_C = b'\x00\x00\x00\x0F'
ENDI='little'
class packet:
      def __init__(self,msg):
            #methods for msg
            if len(msg) == 4:
                  self.msg = msg
            else:
                  self.msg=b'\x00\x00\x00\x00'
            self.address = (int.from_bytes(msg, ENDI) & 
                            int.from_bytes(ADDR_C,ENDI)).to_bytes(max(len(msg), len(ADDR_C)), ENDI)
            self.tag = (int.from_bytes(msg, ENDI) & 
                        int.from_bytes(TAG_C, ENDI)).to_bytes(max(len(msg), len(TAG_C)), ENDI)

            self.tag4bit = self.tag[-1] & 0b1111
      def print_all(self):
            print('msg is : x{} \t addr is: x{} \t tag is: x{}'.format(self.msg.hex('x'),self.address.hex('x'),self.tag.hex('x')))