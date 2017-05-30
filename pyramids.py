# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np


def compare():
    
    
    
    a = np.array(a)
    b = np.array(b)
    np.linalg.norm(a-b,2)
    pass



pyrLevelMax = 6

#def Py_PatternMatching():
    
im = cv2.imread ('IMG30.JPG',1) 
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#    plt.imshow(im),plt.show()
#im = im[:,:,(1,2,0)]
#    templ_range = np.array([[285,634],[1743,2085]])
#    sh = np.array(im.shape[:2])
#    templ_range = templ_range.T / sh.T * np.ones((2,1))

templ = [im_gray[285:634,1743:2085].copy()]
img_pyr = [im_gray.copy()]

plt.figure(1)
plt.subplot(2,3,1)
plt.imshow(img_pyr[0])

plt.figure(2)
plt.subplot(2,3,1)
plt.imshow(templ[0])

for i in range(1,pyrLevelMax):
    
    img_pyr.append( cv2.pyrDown(img_pyr[i-1]))
    plt.figure(1)
    plt.subplot(2,3,i+1)
    plt.imshow(img_pyr[i])
    
    
    templ.append(cv2.pyrDown(templ[i-1]))
    plt.figure(2)
    plt.subplot(2,3,i+1)
    plt.imshow(templ[i])
    
cv2.waitKey(100) 
cv2.waitKey(0) 

res = cv2.matchTemplate(img_pyr[i],templ[i],cv2.TM_CCOEFF_NORMED)

w, h = templ[i].shape[::-1]
loc = np.where( res >= 0.8)
res[loc[0],loc[1]]
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_pyr[i], pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
    

plt.figure(1)
plt.subplot(2,3,i+1)
plt.imshow(img_pyr[i])

#    cv2.namedWindow( 'orgin', cv2.WINDOW_NORMAL )
#    cv2.imshow('orgin',im) 
cv2.waitKey(100) 
cv2.waitKey(0) 
#    dst = im.copy()
#    sh = np.int8(im.shape[0]/2, im.shape[1]/2)
#    print(sh)
#    dst = cv2.pyrDown(im)
#    
#    plt.imshow(dst),plt.show()

#    cv2.namedWindow( 'matched', cv2.WINDOW_NORMAL )
#    cv2.imshow('matched',dst)
#    

cv2.destroyAllWindows()
    
    
#cv2.waitKey(0) 
#Py_PatternMatching()