#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: nzj
"""


import socket
import sys

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(b"LocationRequest")

finally:
    sock.close()