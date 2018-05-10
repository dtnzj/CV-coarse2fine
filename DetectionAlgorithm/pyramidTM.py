# -*- coding: utf-8 -*-


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from time import clock

# from DetectionAlgorithm.pyramidTM import pyramidTM
class pyramidTM:
    # the camera object
    cap = None
    cam_enable = 0
    self.templ = None
    self.im    = None
    self.gray  = None


    #def __init__(self, cam_enable=0):
    def __init__(self, cam_enable=0):
        if cam_enable==1:
            self.cap = cv2.VideoCapture(0)
            
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
            print (self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            while(not self.cap.isOpened()):  
                cv2.waitKey(50)
            self.cam_enable = 1

            cv2.namedWindow('Cam')
        pass

    
    def __del__(self):
        if self.cam_enable==1:
            self.cap.release()
        
        cv2.destroyAllWindows()
        pass


    # camerea read 
    def cam_read(self):
        # Capture frame-by-frame
        ret, frame = self.cap.read()
        # Our operations on the frame come here
        self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.im = frame

        return gray

    # camerea display the origin images
    def camDispOrigin(self):
        cv2.imshow('Cam', self.im)
    
    # camerea display the matched images
    def camDispMatched(self):
        imLocal = self.im
        for pt in self.posOut:
            cv2.rectangle(imLocal, tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        
        # cv2.namedWindow('Cam', cv2.WINDOW_NORMAL)
        cv2.imshow('Cam', imLocal)
        # cv2.imshow('Cam', [])
        

    # 
    def getMatchResult(self):
        if self.templ != None and self.gray != None:
            self.posOut = ptm.PyramidTemplatMatching(   self.gray, 
                                                        self.templ, 
                                                        pyrLevelMax=3, 
                                                        ratio=0.3)
        return self.posOut
        
    def imageRead(self, path = './test images/IMG00166.JPG'):
        self.im = cv2.imread (path, cv2.IMREAD_GRAYSCALE) 
        

    def templateSet(self, path = './test images/template.jpg'):
        self.templ = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        
    # 
    def MaxScoreMatch(self, img, tmpl):
        
        # plt.figure(11)
        # plt.subplot(1, 2, 1)
        # plt.imshow(img)
        # plt.subplot(1, 2, 2)
        # plt.imshow(tmpl)
        # plt.show()
        res = cv2.matchTemplate( img, tmpl, cv2.TM_CCOEFF_NORMED )

        pos = np.where(res>=res.max())
        pos = np.array(pos).T[0]

        return pos

    # remove the points that closed to each other, the highest scored one left.
    # input:    RD_loc:    points' positions
    #           RD_sc :    scores
    # output      
    def RemoveDuplicates(self, RD_loc, width, RD_th=10):
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
    def FirstMatching(self, img_pyr, templ, thr = 0.8):
        res = cv2.matchTemplate(img_pyr, templ, cv2.TM_CCOEFF_NORMED)
        
        loc = np.where( res >= thr)
        loc = np.array(loc).T
        
        bb = self.RemoveDuplicates(loc,templ.shape[::-1], RD_th = templ.shape[0])
        
        return res, bb


    # the pyramid matching function
    def PyramidTemplatMatching(self, img, tmpl, pyrLevelMax=3, ratio=0.5, thr = 0.8):

        l = len(img. shape)
        if l>3 or l<2:
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
        res, loc = self.FirstMatching(img_pyr[0], templ[0], thr)
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
                abc = self.MaxScoreMatch(tst, templ[i])
                # print('abc=', abc.append(abc))
                
                pos[0:2] = pos[0:2]+ abc
                pos[2:4] = pos[0:2]+ templ[i].shape
                
            posOut.append(pos)
            
        return posOut



if __name__ == '__main__':
    # np.set_printoptions(threshold=100)
    
    ptm = PTM();
    im = cv2.imread ('./test images/IMG00166.JPG', cv2.IMREAD_GRAYSCALE) 
    # im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    templ = cv2.imread('./test images/template.jpg', cv2.IMREAD_GRAYSCALE)
    # templ = cv2.cvtColor(templ, cv2.COLOR_BGR2GRAY)
    
    # templ = im_gray[1009:1510, 460:1052]
    # cv2.namedWindow('TemplateImage',cv2.WINDOW_NORMAL)
    # cv2.imshow('TemplateImage', im)
    # plt.figure(1)
    # plt.imshow(im)
    # plt.show()
    # plt.figure(2)
    # plt.imshow(templ)
    # plt.show()

    # cv2.imwrite('template.jpg',templ)
    # cv2.waitKey(0)
    
    t_start = clock()
    posOut = ptm.PyramidTemplatMatching(im, templ, pyrLevelMax=3, ratio=0.3)
    t_end = clock()
    dt = t_end - t_start
    print('Compute Time:',dt, 1/dt)

    for pt in posOut:
        cv2.rectangle(im, tuple(pt[0:2][::-1]), tuple(pt[2:4][::-1]), (0, 0, 255), 1)
        
    cv2.namedWindow('OutPutImage', cv2.WINDOW_NORMAL)
    cv2.imshow('OutPutImage', im)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()