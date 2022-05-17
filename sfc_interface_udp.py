# class for turf packet interface, bytes object is created at initialization, 4 bytes long only or else 4 bytes of all 0.
# to get just a byte from a bytes object, .,...
# eventually, need a packet class that expands on this, initializing with zero-filled bytes object of max length: bytes(MAX_LENGTH)
import socket

ADDR_C = b"\x0F\xFF\xFF\xFF"  # this is a bytes class
ADDR_bytearray = 0x0FFFFFFF  # this is a bytes ARRAY
TAG_C = b"\xF0\x00\x00\x00"  # this is a bytes class
TAG_bytearray = 0b11110000  # this is a bytes class ARRAY

# 2 byte ascii are b'Tr' and b'Tw' respectively, these are ports (note difference to addresses in a packet which is sent to a port)
UDP_RD = b"\x54\x72"  # this is in hex, instead decimal: 21618 # obviously for reads
UDP_WR = b"\x54\x77"  # this is in hex, instead decimal: 21623 # obviously for writes

# listen for return packets on the b'Tx' port.
UDP_TX = b"Tx"  # in hex would be: 0x5478, instead decimal: 21,624
ENDI = "little"
UDP_IP = "127.0.0.3"

ATTEMPT = 1  #  this is the number of times to attempt a connection
TIMEOUT = 1  #  the time to wait for a response, written in seconds

MY_IP = "127.0.0.1"
MY_PORT = 21347

cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a control socket
cs.bind((MY_IP, MY_PORT))  # have to bind to port to make it bidirectional


class packet:
    def __init__(
        self, hdr, data=[]
    ):  # default data to empty list, so its a read by default
        # methods for header
        if len(hdr) == 4:  # 32 bit "hdr" --> 28 bit address and 4 bit tag
            self.hdr = hdr
            self.is_badPacket = False
        else:
            self.is_badPacket = True
        if len(data) == 4:  # 32-bits of data per write
            self.data = data
            self.is_read = False
        else:  # if not 32 bits in data, then default to a read
            self.data = []
            self.is_read = True
        if self.is_badPacket is False:
            self.address = (
                int.from_bytes(self.hdr, ENDI) & int.from_bytes(ADDR_C, ENDI)
            ).to_bytes(max(len(self.hdr), len(ADDR_C)), ENDI)
            self.tag = (
                int.from_bytes(self.hdr, ENDI) & int.from_bytes(TAG_C, ENDI)
            ).to_bytes(max(len(self.hdr), len(TAG_C)), ENDI)

            self.tag4bit = self.tag[0] & TAG_bytearray

            self.addr28bit = (
                ((self.address[0] & int.from_bytes(b"\x0F", ENDI)) << 24)
                | (self.address[1] << 16)
                | (self.address[2] << 8)
                | self.address[3]
            ) & ADDR_bytearray

            if self.is_read is False:
                self.send_write()
            else:
                self.send_read()

    def send_read(self):
        self.sending_port = 21618  # 'Tr' --> receives read requests
        self.recd()

    def send_write(self):
        self.sending_port = 21623  # 'Tw' --> receives write requests
        self.recd()

    def recd(self):
        self.control_sock = cs
        self.attempt = ATTEMPT
        self.control_sock.settimeout(
            TIMEOUT
        )  # sets the parameter for how long you want to listen for a response on the client side
        self.control_sock.connect(
            (UDP_IP, self.sending_port)
        )  # connect to the correct port
        while True:
            if self.attempt == 0:  # if you finish an alloted amount of attempts
                # self.quit() # sends a quit message to server
                break
            else:
                self.conn()
                if self.is_recv is True:
                    # self.quit()
                    break
                self.attempt -= 1

    def conn(self):
        self.is_recv = False  # indicates whether a response has been received
        if len(self.data) != 0:  # if read request
            message = self.data + self.hdr
            self.control_sock.sendto(message, (UDP_IP, self.sending_port))
        else:
            self.control_sock.sendto(self.hdr, (UDP_IP, self.sending_port))
        try:  # attempts to receive a response
            # if a response is received, save value
            self.ack, _ = self.control_sock.recvfrom(
                1024
            )  # can format to save receiving port address
            self.is_recv = True
        except Exception:
            self.ack = (
                ""  # if no response is received, indicate there wasn't a response
            )

    def quit(self):  # most likely not required because this needs a specific
        # server set up --> sends quit message
        message = "q"
        self.nmessage = message.encode()
        self.control_sock.sendto(self.nmessage, (UDP_IP, self.sending_port))

    def print_ack(self):  # prints what is send back from the server
        if self.is_recv is True:
            print("Received: {}".format(self.ack))
            print(
                "Acknowledged after {} attempt(s)".format((ATTEMPT + 1) - self.attempt)
            )
        else:
            print("No acknowledgement after {} attempts".format(ATTEMPT))

    def print_rd(self):  # prints the info from read request
        print(
            "reading addr {}, and data should be empty: {}".format(
                self.address.hex("x"), self.data
            )
        )
        print(
            "hdr is : x{} \t addr is: x{} \t tag is: x{} \t data is: {}".format(
                self.hdr.hex("x"),
                self.address.hex("x"),
                self.tag.hex("x"),
                self.data,
            )
        )

    def print_wr(self):  # prints the info from write request
        print(
            "writing addr {}, with data: {}".format(
                self.address.hex("x"), self.data.hex("x")
            )
        )
        print(
            "hdr is : x{} \t addr is: x{} \t tag is: x{}".format(
                self.hdr.hex("x"), self.address.hex("x"), self.tag.hex("x")
            )
        )


    def print_all(self):  # prints everything in print_rd(), print_wr(), print_ack()
        if self.is_badPacket is True:
            print("Bad packet format")
        else:
            if self.is_read is False:
                self.print_wr()
                self.print_ack()
            else:
                self.print_rd()
                self.print_ack()
