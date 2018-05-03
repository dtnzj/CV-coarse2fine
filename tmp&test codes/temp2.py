# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np
#from time import Time

def Py_PatternMatching():
    im = cv.imread ('IMG30.JPG',1) 
    #im = im[:,:,(1,2,0)]
    im = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#    plt.imshow(im),plt.show()
    cv.namedWindow( 'orgin', cv.WINDOW_NORMAL )
    cv.imshow('orgin',im)
    

    
    templ = im[285:634,1743:2085]
    w, h = templ.shape[::-1]
    cv.namedWindow( 'template', cv.WINDOW_AUTOSIZE )
    cv.imshow('template',templ)
    cv.imwrite('template.jpg',templ)
    
    
    res = cv.matchTemplate(im,templ,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(im, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    cv.namedWindow( 'matched', cv.WINDOW_NORMAL )
    cv.imshow('matched',im)
    
    
    
#    cv.waitKey(0)
    
#    cv.destroyAllWindows()
    
    

Py_PatternMatching()

from timeit import Timer

t1=Timer("Py_PatternMatching()","from __main__ import Py_PatternMatching")

print (t1.timeit(1))