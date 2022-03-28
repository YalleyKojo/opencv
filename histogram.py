import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys


img=cv.imread("photos/nana.jpg")
img=cv.resize(img,(500,500))

blank=np.zeros(img.shape[:2],dtype="uint8")

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("mask",masked)


plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("#of pixels")

colors=('b','g','r')

for i,col in enumerate(colors):
    hist=cv.calcHist(img,[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()