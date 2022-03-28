import cv2 as cv
import matplotlib.pyplot as plt
path="photos/nana.jpg"

img=cv.imread(path)



#how to get region of interest

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
constant=cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_CONSTANT,value=[0,255,0])
reflect=cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_REFLECT)
reflect_101=cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_REFLECT_101)
replicate=cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_REPLICATE)
wrap=cv.copyMakeBorder(img,50,50,50,50,cv.BORDER_WRAP)
titles=["constant","reflect","reflect101","replicate","wrap"]
images=[constant,reflect,reflect_101,replicate,wrap]

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.show    
