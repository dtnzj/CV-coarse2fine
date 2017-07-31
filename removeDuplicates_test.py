# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np

# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates_new(RD_loc, RD_th=100):
    RD_loc = np.array(RD_loc)
    N = len(RD_loc)
    # RD_aa is the point group list, the first element of every group is the average location
    RD_aa = [[RD_loc[0]]]
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
            # add a new point group
            RD_aa.append([i])
            # insert the average location at the first element
            RD_aa.insert(0,[i])
    print(RD_aa)
    print('\n\n\nshape=',np.shape(RD_aa),'\n\n\n')
    
    for i in RD_aa:
        print('befor=',i)
        i = [np.max(i, axis=1), np.min(i, axis=1)]
        print('after=',i)
        
        pass
    return RD_aa


def RemoveDuplicates_test(img, loc, bb):
    
    img[loc] = 0
    cv2.rectangle(img, tuple(loc[0:1]-1), tuple(loc[2:3]+1), (0, 0, 255), 1)
    
    cv2.namedWindow('RemoveDuplicates_img_In', cv2.WINDOW_NORMAL)
    cv2.imshow('RemoveDuplicates_img_In', img)


if __name__ == '__main__':
    img = np.zeros([1000,1000,3])
    img[:,:,1] = np.random.randint(0, 255,size=(1000, 1000))
    loc = np.random.randint(0, 1000,size=(50, 2))
    
    
    # cv2.namedWindow('RemoveDuplicates_img_In', cv2.WINDOW_NORMAL)
    # cv2.imshow('RemoveDuplicates_img_In', img)
    # img[:,:,1:2] = np.zeros([1000,1000])
    # plt.imshow(img)
    # plt.show()
    # print(np.shape(img))
    # print(loc)
    # cv2.waitKey(0)
    bb = RemoveDuplicates_new(loc)
    
    RemoveDuplicates_test(img, loc, bb)
    pass