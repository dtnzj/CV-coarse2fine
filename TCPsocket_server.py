#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:22:19 2017

@author: nzj
"""

from socketserver import BaseRequestHandler, TCPServer
import struct
# import the cam read and objectdetection class
from DetectionAlgorithm.pyramidTM import pyramidTM

class EchoHandler(BaseRequestHandler):
    
    # set the objectDetection algorithm class 
    od = 123; 


    def handle(self):
        msg = self.request.recv(1024)
        print (msg)
        x = (0, 0)
        if msg == b"LocationRequest":
            print ('calling LocationRequest() command')
            x = (1.23,2.45)
            t = struct.pack("2d", *x)
            print(t)
            self.request.send( t )
        else:
            print("Undefined Command!")
            
    def finish(self):
        pass
    

if __name__ == '__main__':
    # serv = TCPServer(("localhost", 9998), EchoHandler)
    # serv.serve_forever()
    pass

