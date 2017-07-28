# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# remove the points that closed to each other, the highest scored one left.
# input:    loc:    points' positions
#           sc :    scores
# output      
def RemoveDuplicates(loc, sc,th):
    loc = np.array(loc).T
    N = len(loc)
    aa = [0]
    for i in range(1,N):
        flag = 0
        for j in aa:
            if np.linalg.norm(loc[i]-loc[j]) < th :
                j = i if sc[i] > sc [j] else j
                flag =  1
                break
        
        if flag == 0 :
            aa.append(i)

    return aa

def MaxScoreMatch(img,tmpl):
    
    res = cv2.matchTemplate( img, tmpl, cv2.TM_CCOEFF_NORMED )
    print (res)
    return np.where( res >= res.max() )
    
    pass


# matching the full image with the lowest resolution
def FirstMatching(img_pyr,templ,matchPrecise=50):
    res = cv2.matchTemplate(img_pyr,templ,cv2.TM_CCOEFF_NORMED)
    # cv2.waitKey(0)

    loc = np.where( res >= 0.8)
    bb = RemoveDuplicates(loc, res[loc],matchPrecise)
    print('bb=',bb)
# #    loc = 
    loc = np.array(loc).T
    loc = loc[bb]
    loc_T = list(zip(*loc[::-1]))
# #    res[loc[0],loc[1]]
    loc = loc[:,::-1]
    print('loc=',loc)
    return res,loc


if __name__ == '__main__':
    pyrLevelMax = 1
    # os.chdir('./CV course2fine')
    np.set_printoptions(threshold=100)
    #def Py_PatternMatching():
        
    im = cv2.imread ('IMG30.JPG',1) 
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #    plt.imshow(im),plt.show()
    #im = im[:,:,(1,2,0)]
    #    templ_range = np.array([[285,634],[1743,2085]])
    #    sh = np.array(im.shape[:2])
    #    templ_range = templ_range.T / sh.T * np.ones((2,1))
    
    templ = [im_gray[285:634, 1743:2085].copy()]
    img_pyr = [im_gray.copy()]
    
    plt.figure(1)
    plt.subplot(2,3,1)
    plt.imshow(img_pyr[0])
    
    plt.figure(2)
    plt.subplot(2,3,1)
    plt.imshow(templ[0])
    
    for i in range(1,pyrLevelMax):
        
        img_pyr.append( cv2.pyrDown(img_pyr[i-1]))
    #    plt.figure(1)
    #    plt.subplot(2,3,i+1)
    #    plt.imshow(img_pyr[i])
        
        
        templ.append(cv2.pyrDown(templ[i-1]))
    #    plt.figure(2)
    #    plt.subplot(2,3,i+1)
    #    plt.imshow(templ[i])
    for i in range(1,pyrLevelMax):        
        plt.figure(1)
        plt.subplot(2,3,i+1)
        plt.imshow(img_pyr[i])        

        plt.figure(2)
        plt.subplot(2,3,i+1)
        plt.imshow(templ[i])
    
    w, h = templ[0].shape[::-1]
    res,loc = FirstMatching(img_pyr[0],templ[0],50)
    
    cv2.namedWindow('image',cv2.WINDOW_NORMAL)
    cv2.imshow('image',res)
    plt.imshow(res),plt.show()

    k = 1
    for pt in loc:
        cv2.rectangle(img_pyr[0], tuple(pt), tuple((pt + [w, h])), (0,0,255), 1)
        # tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2,pt[0]*2:(pt[0]+h+1)*2]
    
    cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
    cv2.imshow('image2',img_pyr[0])
    
    # k = 1
    # for pt in loc[:,::-1]:
    #     cv2.rectangle(img_pyr[5], tuple(pt), tuple((pt + [w, h])), (0,0,255), 1)
    #     tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2,pt[0]*2:(pt[0]+h+1)*2]
        
        
    #     pos = MaxScoreMatch(tst,templ[4])
        
    
    # for i in range(1,pyrLevelMax):
        
    #     plt.figure(1)
    #     plt.subplot(2,3,i+1)
    #     plt.imshow(img_pyr[i])        

    #     plt.figure(2)
    #     plt.subplot(2,3,i+1)
    #     plt.imshow(templ[i])
    
    
    # cv2.destroyAllWindows()
    cv2.waitKey(0)

