#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:22:19 2017

@author: nzj
"""

from socketserver import BaseRequestHandler, TCPServer
# import the cam read and objectdetection class

class EchoHandler(BaseRequestHandler):
    
    # set the objectDetection algorithm class 
    od = 123; 


    def handle(self):
            msg = self.request.recv(64)
            print (msg)
            
            if msg == b"LocationRequest":
                print ('calling LocationRequest() command')
                print (msg)

                self.request.send( tmp )   
            
    def finish(self):
        pass
    

if __name__ == '__main__':
    serv = TCPServer(('', 9999), EchoHandler)
    serv.serve_forever()

