#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:25:06 2017

@author: nzj
"""

import numpy as np
import cv2


cap = cv2.VideoCapture(0)
print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))

cv2.namedWindow( 'frame', cv2.WINDOW_NORMAL )

while(not cap.isOpened()):  
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
pass   
#while(cap.isOpened()):  
# Capture frame-by-frame
ret, frame = cap.read()
# Our operations on the frame come here
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# Display the resulting frame
cv2.imshow('frame',gray)
#if cv2.waitKey(20) & 0xFF == ord('q'):
#    break

print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# When everything done, release the capture
cap.release()

#cv2.destroyAllWindows()