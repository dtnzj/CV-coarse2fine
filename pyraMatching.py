# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates_new(RD_loc, RD_th=50):
    RD_loc = np.array(RD_loc).T
    N = len(RD_loc)
    # RD_aa is the point group list, the first element of every group is the average location
    RD_aa = [[]]
    for i in RD_loc:
        flag = 0
        for j in RD_aa :
            if np.linalg.norm(i-j[0]) < RD_th :
                j.append(i)
                j[0]= np.mean(j[1::])
                flag = 1
                break    

        if flag == 0 :
            # add a new point group
            RD_aa.append(i)
            # insert the average location at the first element
            RD_aa.insert(0,i)
    for i in RD_aa:
        i = [np.max(i, axis=1), np.min(i, axis=1)]
        pass
    return RD_aa


# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates(RD_loc, RD_sc, RD_th=50):
    RD_loc = np.array(RD_loc).T
    N = len(RD_loc)
    RD_aa = [0]
    for i in range(1, N):
        flag = 0
        for j in RD_aa:
            if np.linalg.norm(RD_loc[i]-RD_loc[j]) < RD_th :
                j = i if RD_sc[i] > RD_sc [j] else j
                flag = 1
                break
        
        if flag == 0 :
            RD_aa.append(i)

    return RD_aa

def MaxScoreMatch(img, tmpl):
    
    plt.figure(11)
    plt.subplot(1, 2, 1)
    plt.imshow(img)  
    plt.subplot(1, 2, 2)
    plt.imshow(tmpl)  
    plt.show()
        
    # print('tmpl: ', len(templ), len(tmpl[0]))
    # print('img : ', len(img), len(img[0]))
    # print('img = ', img)
    # print('tmpl= ', tmpl)
    res = cv2.matchTemplate( img, tmpl, cv2.TM_CCOEFF_NORMED )
    # print (res)
    pos = np.where( res >= res.max() )
    pos = np.array( pos ).T

    return pos


def RemoveDuplicates_test(img, loc, bb):
    
    img[loc] = 0
    cv2.rectangle(img, tuple(loc[0:1]-1), tuple(loc[2:3]+1), (0, 0, 255), 1)
    
    cv2.namedWindow('RemoveDuplicates_img_In', cv2.WINDOW_NORMAL)
    cv2.imshow('RemoveDuplicates_img_In', img)



# matching the full image with the lowest resolution
def FirstMatching(img_pyr, templ):
    res = cv2.matchTemplate(img_pyr, templ, cv2.TM_CCOEFF_NORMED)
    # cv2.waitKey(0)

    loc = np.where( res >= 0.8)
    bb = RemoveDuplicates_new(loc)
    RemoveDuplicates_test(img, loc, bb)

    # print('bb=',bb)
# #    loc = 
    loc = np.array(loc).T
    loc = loc[bb]
    loc_T = list(zip(*loc[::-1]))
# #    res[loc[0], loc[1]]
    loc = loc[:, ::-1]
    # print('loc=', loc)
    return res, loc


if __name__ == '__main__':
    pyrLevelMax = 3
    # os.chdir('./CV course2fine')
    np.set_printoptions(threshold=100)
    # def Py_PatternMatching():
        
    im = cv2.imread ('IMG30.JPG', 1) 
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #    plt.imshow(im), plt.show()
    #    im = im[:, :, (1, 2, 0)]
    #    templ_range = np.array([[285, 634], [1743, 2085]])
    #    sh = np.array(im.shape[:2])
    #    templ_range = templ_range.T / sh.T * np.ones((2, 1))
    
    
    
    # generate the pyramid images and templates
    templ = [im_gray[285:634, 1743:2085].copy()]
    img_pyr = [im_gray.copy()]
    for i in range(1, pyrLevelMax+1):        
        img_pyr.insert(0, cv2.pyrDown(img_pyr[0]))
        templ.insert(0, cv2.pyrDown(templ[0]))
        
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
    h, w = templ[0].shape
    # print('templ[0].shape=', templ[0].shape)
    # print('templ[0].shape[::-1]=', templ[0].shape[::-1])
    
    res, loc = FirstMatching(img_pyr[0], templ[0])
    
    # cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    # cv2.imshow('res', res)
    # plt.imshow(res), plt.show()

    # k = 1
    # for pt in loc:
    #     cv2.rectangle(img_pyr[0], tuple(pt), tuple((pt + [w, h])), (0, 0, 255), 1)
        # tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2, pt[0]*2:(pt[0]+h+1)*2]
    
    # cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
    # cv2.imshow('image2', img_pyr[0])
    
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
            # print('i=', i)
            # print(pos[1]*2, (pos[1]+w+5)*2, pos[0]*2, (pos[0]+h+5)*2)
            pos = pos *2
            h, w = templ[i].shape
            tst = img_pyr[i][pos[1]:(pos[1]+w+10), pos[0]:(pos[0]+h+10)]
            cv2.namedWindow('tst', cv2.WINDOW_NORMAL)
            cv2.imshow('tst', tst)
            # print(len(tst), len(templ[i]), i)
            
            cv2.waitKey(0)
            abc = MaxScoreMatch(tst, templ[i])
            # print('abc=', abc)
            # print('pos=', pos)
            pos = pos +abc[::-1]
            # print('pos(after)=', pos)
            
            # pos = np.int16(pos)
            pos=pos[0]

            # print('pos=', type(pos[0]))
            
            pass
        posOut.append(pos)
        
        # k=k+1
        # plt.figure(3)
        # plt.subplot(2, 2, k)
        # plt.imshow(tst)
    k = 1
    h, w = templ[-1].shape
    
    for pt in posOut:
        cv2.rectangle(im, tuple(pt), tuple((pt + [w, h])), (0, 0, 255), 1)
        # tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2, pt[0]*2:(pt[0]+h+1)*2]
    
    cv2.namedWindow('OutPutImage', cv2.WINDOW_NORMAL)
    cv2.imshow('OutPutImage', im)
            

    plt.show()
    

        
    #     
    
    
    # cv2.destroyAllWindows()
    cv2.waitKey(0)

