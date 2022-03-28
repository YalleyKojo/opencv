import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
path="C:/Users/Yoga/OneDrive/Pictures/jojo.jpg"
path_2="C:/Users/Yoga/OneDrive/Pictures/kojo.jpg"
img_1=cv.imread(path)
img2=cv.imread(path_2)
print(img_1.shape)
print(img2.shape)
dimensions=(500,500)

img_1r=cv.resize(img_1,dimensions,interpolation=cv.INTER_AREA)
img2r=cv.resize(img2,dimensions,interpolation=cv.INTER_AREA)

img_added_weight=cv.addWeighted(img_1r,0.5,img2r,0.5,0)

cv.imshow("add_weighted",img_added_weight)


key=cv.waitKey(0)
if key==ord('q'):
    sys.end
cv.destroyAllWindows()