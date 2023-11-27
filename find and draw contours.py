import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("OpenCV_Logo.png")
img=cv2.resize(img,(512,512))
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres=cv2.threshold(grayimg,180,255,0)
contours,hierarchy=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print("number of contours= ",len(contours))
print(contours[0])

cv2.drawContours(img, contours,-1,(0,255,0),3)

titles=['img','grayimg','thres']
images=[img,grayimg,thres]

for i in range (3):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()