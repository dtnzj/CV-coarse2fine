# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np

# remove the points that closed to each other, the highest scored one left.
# input:    RD_loc:    points' positions
#           RD_sc :    scores
# output      
def RemoveDuplicates_new(RD_loc, RD_th=100):
    # RD_loc = np.array(RD_loc)
    # N = len(RD_loc)
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
        i = np.append(np.max(i, axis=0),np.min(i, axis=0))
        i = np.int16(i)
        # print('after=',i)
        RD_bb = RD_bb + [i.tolist()]
        
    print(RD_bb)
    return RD_bb


def RemoveDuplicates_test(img, loc, bb):
    
    print("img = ")
    # for cc in loc:
    #     print(img[cc[0]][cc[1]][1])
    #     img[cc[0]][cc[1]][1] = 0
    for cc in loc:
        # print("cc = ",cc[0:2])
        cv2.circle(img, tuple(cc[0:2]), 10, (0, 0, 255), 1)
    
    for cc in bb:
        print("cc = ",cc[0:2],cc[2:4])
        cv2.rectangle(img, tuple(cc[0:2]), tuple(cc[2:4]), (0, 0, 255), 1)
    
    cv2.namedWindow('RemoveDuplicates_img_In', cv2.WINDOW_NORMAL)
    cv2.imshow('RemoveDuplicates_img_In', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    img = np.zeros([1000,1000,3])
    img[:,:,1] = np.random.randint(0, 255,size=(1000, 1000))
    loc = np.random.randint(0, 1000,size=(100, 2))
    
    
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