import cv2 as cv
import sys

img=cv.imread("photos/nana.jpg")
img=cv.resize(img,(500,500))

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple thresholding
threshold,thresh= cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)


#adaptive thresholding
adaptivethresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,13,3)
cv.imshow("adaptive thresh",adaptivethresh)

#otsu threshholding
otsu_thresh,threshOtsu=cv.threshold(gray,150,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("otsu thresholding",threshOtsu)


z=cv.waitKey(0)

if z==ord('q'):
    sys.exit
