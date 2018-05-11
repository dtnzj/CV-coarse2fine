#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nzj
"""


import socket
import sys
import struct
HOST, PORT = "localhost", 9998

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(b"LocationRequest")

    received = sock.recv(1024)
    t = struct.unpack("4d",received)
    print(received,'\n',t)
finally:
    sock.close()