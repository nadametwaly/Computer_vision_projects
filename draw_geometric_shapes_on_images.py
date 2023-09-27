import numpy as np
import cv2 as cv
img=np.zeros([512,512,3],np.uint8)

img=cv.line(img,(0,0),(256,256),(255,0,0),10)
img=cv.arrowedLine(img,(0,255),(256,256),(0,255,0),5)
img=cv.rectangle(img,(255,255),(510,510),(255,0,255),-1)
img=cv.circle(img,(255,255),50,(0,0,255),8)

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()