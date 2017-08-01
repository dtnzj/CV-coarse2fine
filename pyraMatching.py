# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os



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
    pos = np.array( pos ).T[0]

    return pos

# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates(RD_loc, width, RD_th=50):
    # RD_aa is the point group list, the first element of every group is the average location
    RD_aa = [[RD_loc[0], RD_loc[0]]]
    # print(RD_aa)
    for i in RD_loc[1::]:
        flag = 0
        for j in RD_aa :
            # print('j=',j[0],'i=',i)
            if np.linalg.norm(i-j[0]) < RD_th :
                j.append(i)
                j[0]= np.mean(j[1::],axis=0)  
                flag = 1
                break    

        # print(flag)
        if flag == 0 :
            # add a new point group and insert the average location at the first element
            RD_aa.append([i,i])

    RD_bb = []
    for i in RD_aa:
        # print('befor=',i)
        i = np.append(np.min(i, axis=0),(np.max(i, axis=0)+width))
        i = np.int16(i)
        print('after=',i)
        RD_bb = RD_bb + [i.tolist()]
        
    # print(RD_bb)
    return RD_bb# remove the points that closed to each other, the highest scored one left.


# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates(RD_loc, width, RD_th=50):
    # RD_aa is the point group list, the first element of every group is the average location
    RD_aa = [[RD_loc[0], RD_loc[0]]]
    # print(RD_aa)
    for i in RD_loc[1::]:
        flag = 0
        for j in RD_aa :
            # print('j=',j[0],'i=',i)
            if np.linalg.norm(i-j[0]) < RD_th :
                j.append(i)
                j[0]= np.mean(j[1::],axis=0)  
                flag = 1
                break    

        # print(flag)
        if flag == 0 :
            # add a new point group and insert the average location at the first element
            RD_aa.append([i,i])

    RD_bb = []
    for i in RD_aa:
        # print('befor=',i)
        i = np.append(np.min(i, axis=0),(np.max(i, axis=0)+width))
        i = np.int16(i)
        print('after=',i)
        RD_bb = RD_bb + [i.tolist()]
        
    # print(RD_bb)
    return RD_bb


# matching the full image with the lowest resolution
def FirstMatching(img_pyr, templ):
    res = cv2.matchTemplate(img_pyr, templ, cv2.TM_CCOEFF_NORMED)

    # cv2.waitKey(0)

    loc = np.where( res >= 0.8)
    loc = np.array(loc).T
    print('templ.shape=',templ.shape[::-1])
    bb = RemoveDuplicates(loc,templ.shape[::-1])
    
    print(bb)
    
    # c = input()
    
    # print('bb=',bb)
# #    loc = 
    # loc = np.array(loc)
    # loc = loc[bb]
    # loc_T = list(zip(*loc[::-1]))
# #    res[loc[0], loc[1]]
    # loc = loc[:, ::-1]
    # print('loc=', loc)
    return res, bb


if __name__ == '__main__':
    pyrLevelMax = 2
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
    # h, w = templ[0].shape
    # print('templ[0].shape=', templ[0].shape)
    # print('templ[0].shape[::-1]=', templ[0].shape[::-1])
    
    res, loc = FirstMatching(img_pyr[0], templ[0])
    loc = np.array(loc)
    # cv2.namedWindow('res', cv2.WINDOW_NORMAL)
    # cv2.imshow('res', res)
    # plt.imshow(res), plt.show()

    # for pt in loc:
    #     cv2.rectangle(img_pyr[0], tuple(loc[0][0:2][::-1]), tuple(loc[0][2:4][::-1]), (0, 0, 255), 1)
        # tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2, pt[0]*2:(pt[0]+h+1)*2]
    
    cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
    cv2.imshow('image2', img_pyr[0])
    cv2.waitKey(0)
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
            print(pos)
            # h, w = templ[i].shape
            tst = img_pyr[i][pos[0]:pos[2], pos[1]:pos[3]]
            cv2.namedWindow('tst', cv2.WINDOW_NORMAL)
            cv2.imshow('tst', tst)
            # print(len(tst), len(templ[i]), i)
            
            cv2.waitKey(0)
            abc = MaxScoreMatch(tst, templ[i])
            # print('abc=', abc.append(abc))
            print('pos=', pos)
            pos[0:2] = pos[0:2]+ abc
            pos[2:4] = pos[0:2]+ templ[i].shape
            print('pos(after)=', pos)
            
            # pos = np.int16(pos)
            # pos=pos[0]

            # print('pos=', type(pos[0]))

        posOut.append(pos)
        
        # k=k+1
        # plt.figure(3)
        # plt.subplot(2, 2, k)
        # plt.imshow(tst)
    # print(posOut)
    for pt in posOut:
        cv2.rectangle(im, tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        # cv2.rectangle(img_pyr[0], tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        # tst = img_pyr[4][pt[1]*2:(pt[1]+w+1)*2, pt[0]*2:(pt[0]+h+1)*2]
    
    cv2.namedWindow('OutPutImage', cv2.WINDOW_NORMAL)
    cv2.imshow('OutPutImage', im)
            

    plt.show()
    

        
    #     
    
    
    # cv2.destroyAllWindows()
    cv2.waitKey(0)

