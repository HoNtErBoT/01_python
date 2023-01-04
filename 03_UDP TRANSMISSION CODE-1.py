#    SIMPLE UDP TRANSMISSION PYTHON

import socket                                                                       # import socket

UDP_IP = "192.168.1.3"                                                              # Configure Receiver IP Address
UDP_PORT = 2020                                                                     # Configure PORT number
MESSAGE = b"Hello, World!"                                                          # Set message to be transmitted

print("UDP target IP: %s" % UDP_IP)                                                 # Print UDP IP
print("UDP target port: %s" % UDP_PORT)                                             # Print UDP PORT
print("message: %s" % MESSAGE)                                                      # Print Message
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                             # UDP Socket initialization
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))                                            # Send Message
