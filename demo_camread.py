# -*- coding: utf-8 -*-

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from time import clock

from DetectionAlgorithm.pyramidTM import pyramidTM


if __name__ == '__main__':
    ptm = pyramidTM(cam_enable = 1)
    # ptm.camList()

    # ptm.cam_read()
    # ptm.camDispOrigin()
    # cv2.waitKey(20)
    # input('wait to next')
    # ptm.templateSet()
    ptm.templateRead()
    cv2.imshow('Templ',ptm.templ)
    cv2.waitKey(20)
    # exit()
        
    while True:
        t_start = clock()
        ptm.cam_read()
        # ptm.camDispOrigin()
        kk = ptm.getMatchResult()
        ptm.camDispMatched()
        t_end = clock()
        dt = t_end - t_start
        print('Compute Time:',dt, 1/dt, 'posOut= ', kk)

        cv2.waitKey(50)
    input('Waiting to End!')


    pass