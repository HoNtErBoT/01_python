#  Simple UDP receiver code
#  Rajeev TR

import socket                                               # import socket

UDP_IP = "192.168.1.4"                                      # Set our IP address
UDP_PORT = 2020                                             # Set PORT number
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # UDP
sock.bind((UDP_IP, UDP_PORT))                               # Initialize UDP socket
while True:                                                 # Start infinite loop
    data, addr = sock.recvfrom(1024)                        # buffer size is 1024 bytes
    data = data.decode("utf-8")                             # Decode received data
    print("received message: %s" % data)                    # Print Message
    if data == "stop":                                      # Check if stop command received
        print(" Communication terminated")                  # Print session termination message
        sock.close()                                        # kill UDP communication
        break
