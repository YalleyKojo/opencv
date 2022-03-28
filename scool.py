import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys

img1=cv.imread("photos/Opencv.png")
rows,cols=img1.shape[0:2]

img1_zero=np.zeros_like(img1)


img2=cv.imread("photos/nana.jpg")
roi=img2[0:rows,0:cols]
roi_zero=np.zeros_like(roi)

img1_gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
cv.imshow("gray",img1_gray)

ret,img1_thres=cv.threshold(img1_gray,20,255,cv.THRESH_BINARY)
cv.imshow("thres",img1_thres)


img1_fg=cv.add(img1,img1_zero,mask=img1_thres)
cv.imshow("fg",img1_fg)
img1_thres_inv=cv.bitwise_not(img1_thres)
cv.imshow("thres_inv",img1_thres_inv)

roi_bg=cv.add(roi,roi_zero,mask=img1_thres_inv)
cv.imshow("bg",roi_bg)
img_add=cv.add(img1_fg,roi_bg,mask=img1_thres)
img2[0:rows,0:cols]=img_add

cv.imshow("img2",img2)

images=[img1_gray,img1_thres,img1_fg,img1_thres_inv,roi_bg,img_add,img2]
titles=["gray","thres","fg","thres_inv","roi_bg","img_add","img2"]
for i in range (7):
    plt.subplot(2,4,i+1),plt.imshow(images[i]),plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
cv.waitKey(0)
cv.destroyAllWindows()    
