import cv2 as cv
import numpy as np
# contour detection

img=cv.imread("photos/nana.jpg")


img=cv.resize(img,(500,500),cv.INTER_AREA)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny=cv.Canny(gray,125,175)

contours,hierachies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)


draw=np.zeros((500,500),dtype="uint8")
cv.drawContours(draw,contours,-1,(0,0,255))

cv.imshow("draw",draw)
cv.imshow("canny",canny)

cv.waitKey(0)