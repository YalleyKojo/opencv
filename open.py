import cv2 as cv
import sys

def rescale(frame,scale=0.2):
    height=int(frame.shape[0]*scale/2)
    width=int(frame.shape[1]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

path='photos/nana.jpg'
img=cv.imread('photos/nana.jpg')
img=rescale(img)
img_gray=cv.imread(path,cv.IMREAD_GRAYSCALE)
img_gray=rescale(img_gray)
cv.imshow('img',img)
cv.imshow('img_gray',img_gray)

k=cv.waitKey(0)

if k== ord('q'):
    sys.end
