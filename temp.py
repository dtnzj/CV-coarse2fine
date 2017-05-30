# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
from time import clock


os.chdir('/home/nzj/Desktop')
os.getcwd()

img = cv2.imread('mario.jpg',0)
img = img[:,1:225]
template = img[82:96,72:81]
print (img.shape)
w, h = template.shape[::-1]
print (template.shape)

t_start = clock()
for i in range(100):
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

t_end = clock()
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imwrite('res.png',img)

plt.imshow(img),plt.show()

print(t_start - t_end)

