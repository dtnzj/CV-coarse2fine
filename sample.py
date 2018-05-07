import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from time import clock
#  from 

if __name__ == '__main__':
    # np.set_printoptions(threshold=100)
        
    im = cv2.imread ('IMG00166.JPG', 1) 
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    templ = cv2.imread('template.jpg',0)
    # templ = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
    
    # templ = im_gray[1009:1510, 460:1052]
    # cv2.namedWindow('TemplateImage',cv2.WINDOW_NORMAL)
    # cv2.imshow('TemplateImage',templ)
    # plt.figure(1)
    # plt.imshow(im_gray)
    
    # plt.figure(2)
    # plt.imshow(templ)
    # plt.show()

    # cv2.imwrite('template.jpg',templ)
    # cv2.waitKey(0)
    
    # exit()

    t_start = clock()
    posOut = PyramidTemplatMatching(im_gray, templ, pyrLevelMax=3, ratio=0.3)
    t_end = clock()
    dt = t_end - t_start
    print('Compute Time:',dt, 1/dt)

    for pt in posOut:
        cv2.rectangle(im, tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        
    cv2.namedWindow('OutPutImage', cv2.WINDOW_NORMAL)
    cv2.imshow('OutPutImage', im)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
