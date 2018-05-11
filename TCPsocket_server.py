#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:22:19 2017

@author: nzj
"""

from socketserver import BaseRequestHandler, TCPServer
import struct
# import cv2
# import the cam read and objectdetection class
from DetectionAlgorithm.pyramidTM import pyramidTM

class EchoHandler(BaseRequestHandler):
    
    # set the objectDetection algorithm class 
    ptm = pyramidTM(cam_enable = 0)
    ptm.templateSet()
    

    def handle(self):
        msg = self.request.recv(1024)
        print (msg)
        x = (0, 0)
        if msg == b"LocationRequest":
            print ('calling LocationRequest() command')
            self.ptm.imageRead()
            kk = self.ptm.getMatchResult()
            print('Matched Location= ', kk)
            # self.ptm.camDispMatched()

            t = struct.pack("4d", *(kk[0].tolist()))
            print('Packed Command:', t)
            self.request.send( t )
        else:
            print("Undefined Command!")
            
    def finish(self):
        pass
    

if __name__ == '__main__':
    serv = TCPServer(("localhost", 9998), EchoHandler)
    serv.serve_forever()
    # while   cv2.waitKey(20)!='q':
    #     pass


    pass

