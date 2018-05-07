#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:22:19 2017

@author: nzj
"""

from socketserver import BaseRequestHandler, TCPServer
class EchoHandler(BaseRequestHandler):
    # set the objectDetection algorithm class 
    self.od = 

    def handle(self):
            msg = self.request.recv(64)
            print (msg)
            
            if msg[0:6] == b"sutter":
                print ('calling CurrentPos() command')
                print (tmp)
                self.request.send( tmp )   
            
    def finish(self):
        pass
    

if __name__ == '__main__':
    serv = TCPServer(('', 9999), EchoHandler)
    serv.serve_forever()

