# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


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

gserdwfwefrgserg
gserdwfwefrgserg
sergdwfwefrg
sgredwfwefergsgrg
sgredwfwefergsgrg

def MaxScoreMatch(img,tmpl):
    
    res = cv2.matchTemplate( img, tmpl, cv2.TM_CCOEFF_NORMED )
    print (res)
    return np.where( res >= res.max() )
    
    pass






if __name__ == '__main__':        
    pyrLevelMax = 6
    os.chdir('./CV course2fine')
    np.set_printoptions(threshold=100)
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
        
    res = cv2.matchTemplate(img_pyr[i],templ[i],cv2.TM_CCOEFF_NORMED)
    
    w, h = templ[i].shape[::-1]
    loc = np.where( res >= 0.8)
    
    bb = RemoveDuplicates(loc, res[loc].copy(),10)
#    loc = 
    loc = np.array(loc).T
    loc = loc[bb]
#    loc_T = list(zip(*loc[::-1]))
#     res[loc[0],loc[1]]
#    loc = loc[:,::-1]
    k = 1
    for pt in loc[:,::-1]:
        cv2.rectangle(img_pyr[5], tuple(pt), tuple((pt + [w, h])), (0,0,255), 1)
        tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2,pt[0]*2:(pt[0]+h+1)*2]
        
        
        pos = MaxScoreMatch(tst,templ[4])
        
    
    for i in range(1,pyrLevelMax):
        
        plt.figure(1)
        plt.subplot(2,3,i+1)
        plt.imshow(img_pyr[i])        

        plt.figure(2)
        plt.subplot(2,3,i+1)
        plt.imshow(templ[i])
    
    
    cv2.destroyAllWindows()
    