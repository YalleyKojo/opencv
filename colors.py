import cv2 as cv
import sys

img=cv.imread("photos/nana.jpg")

img=cv.resize(img,(400,400))

img2hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)

img2lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)

cv.imshow("original",img)

cv.imshow("HSV",img2hsv)

cv.imshow("Lab",img2lab)


key=cv.waitKey(0)

