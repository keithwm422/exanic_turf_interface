# exanic_turf_interface
For developing TURF interface code using python sockets. The TURF firmware and UDP interface document can be found at: https://github.com/barawn/exanic_turf_test

Servers: turf_read_udp.py and turf_write_udp.py --> You need these both running before you try to run the client code. 

Use sfc_interface_udp.py and test_sfc_interface_udp.py to connect to the server

Use turf_data_interpreter.py to parse the packet data. This is not complete and will not work for every address/data sent to it. Currently using methodstrial.py to test the packet parser.
