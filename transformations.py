#image transformations
# resize, transalation, rotation, 


import cv2 as cv
import numpy as np

img=cv.imread("photos/nana.jpg")


img=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)

#translation fucction
def translate(img,x,y):
    transMatrix=np.float32([[0,1,x],[1,0,y]])
    dimensions=(500,500)
    return cv.warpAffine(img,transMatrix,dimensions)

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)

    #get the rotation matrix
    rotationMatrix=cv.getRotationMatrix2D(rotPoint,angle,1.0)   

    dimensions=(height,width) 
    return cv.warpAffine(img,rotationMatrix,dimensions)



img2= translate(img,-100,-50)

cv.imshow('transformed',img2)

img3=rotate(img,90)

cv.imshow("rotated",img3)

cv.waitKey(0)