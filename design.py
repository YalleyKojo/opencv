# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:13:31 2021

@author: Yoga
"""

import cv2 as cv
import numpy as np

def nothing(args):
    pass

img = cv.imread("C:Users\Yoga\OneDrive\Pictures\jojo.jpg") # Here you need to give an image

img_hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
img_zeros = np.zeros_like(img)
cv.namedWindow('tracks')
cv.createTrackbar("LH","tracks",0, 180,nothing)
cv.createTrackbar("LS","tracks",0, 255,nothing)
cv.createTrackbar("LV","tracks",0, 255,nothing)

cv.createTrackbar("UH","tracks",180, 180,nothing)
cv.createTrackbar("US","tracks",255, 255,nothing)
cv.createTrackbar("UV","tracks",255, 255,nothing)

while(1):
    l_h = cv.getTrackbarPos("LH","tracks")
    l_s = cv.getTrackbarPos("LS","tracks")
    l_v = cv.getTrackbarPos("LV","tracks")
    u_h = cv.getTrackbarPos("UH","tracks")
    u_s = cv.getTrackbarPos("US","tracks")
    u_v = cv.getTrackbarPos("UV","tracks")
    
    lower_b = np.array([l_h,l_s,l_v])
    upper_b = np.array([u_h,u_s,u_v])
    
    mask = cv.inRange(img_hsv,lower_b,upper_b)
    res = cv.add(img,img_zeros,mask=mask)
    
    cv.imshow("img",img)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    k = cv.waitKey(1)
    if k==27:
        break
    
cv.destroyAllWindows()
