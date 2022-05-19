TURF_IDS = {
    "0x54555246": "TURF",
    "0x5446534d": "TFSM",
    "0x54494f50": "TIOP",
    "0x5446494f": "TFIO",
    "0x53555246": "SURF",
    "0x5346534d": "SFSM",
    "0xFFFFFFFF": "No device present",
}

MONTH = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


class packetparser:
    def __init__(self, data, tag, addr):
        self.data = data  # saved as an int
        self.tag = tag
        self.addr = addr

        if hex(self.addr) == "0x0":
            self.ident()
        elif hex(self.addr) == "0x1":
            self.dateversion()
        elif hex(self.addr) == "0x2":
            self.control()

    def ident(self):  # IDENT [31:0]
        self.hexconv()
        self.identity = TURF_IDS[self.data]
        print("Address returned: {}, ID: {}".format(self.addr, self.identity))

    def dateversion(self):  # DATEVERSION [31:0]
        self.datevers = "{:032b}".format(int(self.data))
        self.dateparser()

        print(
            "The latest firmware version is {}.{}.{}".format(
                self.major, self.minor, self.revision
            )
        )
        print(
            "Last revised on {} {}, 20{}".format(MONTH[self.month], self.day, self.year)
        )

    def control(self):
        print()

    def hexconv(self):
        self.addr = hex(self.addr)
        self.data = hex(self.data)
        self.tag = hex(self.tag)

    def dateparser(self):
        self.dateverval = [
            self.datevers[0:7],
            self.datevers[7:11],
            self.datevers[11:16],
            self.datevers[16:20],
            self.datevers[20:24],
            self.datevers[24:32],
        ]

        for iter in range(len(self.dateverval)):
            self.binval = self.dateverval[iter]
            self.bintoint()
            self.dateverval[iter] = self.bintotal

        self.year, self.month, self.day, self.major, self.minor, self.revision = map(
            int, self.dateverval
        )

    def bintoint(self):
        self.bintotal = 0
        expo = 0
        for i in range(len(self.binval) - 1, -1, -1):
            if int(self.binval[i]) == 1:
                self.bintotal += 2 ** expo
            expo += 1
