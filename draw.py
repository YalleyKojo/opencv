import cv2 as cv
import numpy as np
import sys
import matplotlib.pyplot as plot

blank=np.zeros((500,500,3),dtype='uint8')
img=cv.imread('photos/nana.jpg')

print(img.shape)

width,height=500,500

dimensions=width,height

img=cv.resize(img,dimensions,interpolation=cv.INTER_AREA)
circle=cv.circle(blank,(250,250),200,(0,0,255),-1)

cv.imshow("img",blank)

blank_rgb=cv.cvtColor(blank,cv.COLOR_BGR2RGB)

plot.imshow(blank_rgb)
plot.show()


if cv.waitKey(0)==ord('q'):
    sys.end