#!/usr/bin/env python3

"""
This code is aiming at comparing the compute time cost
by the python opencv with labview.
"""
# import os
import matplotlib.pyplot as plt
import numpy as np
from time import clock
import cv2


# os.chdir('/home/nzj/Desktop')
# print(os.getcwd())

# print('fawefw')
img = cv2.imread('IMG30.JPG',0)
plt.figure(0)
plt.imshow(img), plt.show()

# img = img[:,1:225]
template = img[449:760, 270:610]
plt.figure(1)
plt.imshow(template), plt.show()
print(img.shape)
w, h = template.shape[::-1]
print(template.shape)

t_start = clock()
for i in range(1):
    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

t_end = clock()
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# cv2.imwrite('res.png',img)

print('fawefw',t_start - t_end)
# plt. imshow(img),plt.show()

# cv2.imshow(res);
# cv2.waitKey(0);

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
plt.figure(2)
plt.imshow(res), plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
