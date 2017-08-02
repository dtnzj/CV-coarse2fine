# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from time import clock



def MaxScoreMatch(img, tmpl):
    
    # plt.figure(11)
    # plt.subplot(1, 2, 1)
    # plt.imshow(img)  
    # plt.subplot(1, 2, 2)
    # plt.imshow(tmpl)  
    # plt.show()

    res = cv2.matchTemplate( img, tmpl, cv2.TM_CCOEFF_NORMED )

    pos = np.where( res >= res.max() )
    pos = np.array( pos ).T[0]

    return pos

# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates(RD_loc, width, RD_th=10):
    # RD_aa is the point group list, the first element of every group is the average location
    RD_aa = [[RD_loc[0], RD_loc[0]]]
    
    for i in RD_loc[1::]:
        flag = 0
        for j in RD_aa :
            
            if np.linalg.norm(i-j[0]) < RD_th :
                j.append(i)
                j[0]= np.mean(j[1::],axis=0)  
                flag = 1
                break    

        if flag == 0 :
            # add a new point group and insert the average location at the first element
            RD_aa.append([i,i])

    RD_bb = []
    for i in RD_aa:
        
        i = np.append(np.min(i, axis=0)-1,(np.max(i, axis=0)+width)+1)
        i = np.int16(i)
        
        RD_bb = RD_bb + [i.tolist()]
    
    return RD_bb

# matching the full image with the lowest resolution
def FirstMatching(img_pyr, templ, thr = 0.8):
    res = cv2.matchTemplate(img_pyr, templ, cv2.TM_CCOEFF_NORMED)
    
    loc = np.where( res >= thr)
    loc = np.array(loc).T
    
    bb = RemoveDuplicates(loc,templ.shape[::-1], RD_th = templ.shape[0])
    
    return res, bb


# the pyramid matching function
def PyramidTemplatMatching(img, tmpl, pyrLevelMax=3, ratio=0.5, thr = 0.8):
    
    l = len(img.shape)
    if  l>3 or l<2:
        return
    elif l==3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # generate the pyramid images and templates
    templ = [tmpl]
    img_pyr = [img]
    
    for i in range(1, pyrLevelMax+1):        
        sh_i  = np.int16(np.array(img_pyr[0].shape[:2])[::-1]*ratio)
        sh_t  = np.int16(np.array(  templ[0].shape[:2])[::-1]*ratio)
        
        img_pyr.insert(0, cv2.resize(img_pyr[0],tuple(sh_i)))
        templ.insert(  0, cv2.resize(  templ[0],tuple(sh_t)))
    
    # show the pyramid images 
    # for i in range(0, pyrLevelMax):        
    #     plt.figure(1)
    #     plt.subplot(2, 2, i+1)
    #     plt.imshow(img_pyr[i])  
    #     tmp= ['img_pyr[', str(i), ']']   
    #     plt.title(tmp) 
    #     plt.figure(2)
    #     plt.subplot(2, 2, i+1)
    #     plt.imshow(templ[i])
    #     tmp= ['templ[', i, ']']
    #     plt.title(tmp) 
    # plt.show()

    # coarse matching 
    res, loc = FirstMatching(img_pyr[0], templ[0], thr)
    loc = np.array(loc)
    # for pt in loc:
    #     cv2.rectangle(img_pyr[0], tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
    
    # cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    # cv2.imshow('res', res)
    # plt.imshow(res), plt.show()

    # cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
    # cv2.imshow('image2', img_pyr[0])
    # cv2.waitKey(0)
    
    # fine matching, improve the resolution    
    posOut = list()
    k = 0
    for pt in loc:
        # cv2.rectangle(img_pyr[5], tuple(pt), tuple((pt + [w, h])), (0, 0, 255), 1)
        # cv2.namedWindow('img_pyr[1]', cv2.WINDOW_NORMAL)
        # cv2.imshow('img_pyr[1]', tst)
        # cv2.waitKey(0)
        
        pos = pt
        for i in range(1, pyrLevelMax+1):  
            
            pos = np.int16(pos /ratio)
            tst = img_pyr[i][pos[0]:pos[2], pos[1]:pos[3]]
            # cv2.namedWindow('tst', cv2.WINDOW_NORMAL)
            # cv2.imshow('tst', tst)
            # print(len(tst), len(templ[i]), i)
            # cv2.waitKey(0)
            abc = MaxScoreMatch(tst, templ[i])
            # print('abc=', abc.append(abc))
            
            pos[0:2] = pos[0:2]+ abc
            pos[2:4] = pos[0:2]+ templ[i].shape
            
        posOut.append(pos)
        
    return posOut
    pass


if __name__ == '__main__':
    # np.set_printoptions(threshold=100)
        
    im = cv2.imread ('IMG30.JPG', 1) 
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    templ = im_gray[285:634, 1743:2085]
    
    t_start = clock()
    posOut = PyramidTemplatMatching(im_gray, templ, pyrLevelMax=3, ratio=0.3)
    t_end = clock()
    dt = t_end - t_start
    print('fawefw',dt, 1/dt)

    for pt in posOut:
        cv2.rectangle(im, tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        
    cv2.namedWindow('OutPutImage', cv2.WINDOW_NORMAL)
    cv2.imshow('OutPutImage', im)
    
    cv2.waitKey(0)

