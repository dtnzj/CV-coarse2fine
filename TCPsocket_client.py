#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nzj
"""


import socket
import sys
import struct
HOST, PORT = "localhost", 9998
import cv2
# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server and send data

sock.connect((HOST, PORT))

while cv2.waitKey(50) != 'q':
    
    sock.sendall(b"LocationRequest")
    received = sock.recv(32)
    t = struct.unpack("4d",received)
    print(received,'\n',t)

sock.close()