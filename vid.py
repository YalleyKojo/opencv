import cv2 as cv

path='videos/kida.mp4'

vid=cv.VideoCapture(path)

while True:
    isTrue,frame=vid.read()
    if not isTrue:
        print("can't receive frame(stream end?).Exiting....")
        break
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('frame',frame)
    if cv.waitKey(1)==ord('q'):
        break
vid.release()
cv.destroyAllWindows()
