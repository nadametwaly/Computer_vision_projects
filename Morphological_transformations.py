import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('balls.jpg',0)
_, mask=cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)
kernel=np.ones((3,3), np.uint8)
dilation=cv2.dilate(mask,kernel,iterations=2)
erosion=cv2.erode(mask,kernel,iterations=1)
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel,iterations=2)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2)

titles=['img','mask','dilation','erosion','closing','opening']
images=[img,mask,dilation,erosion,closing,opening]

for i in range (6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# cv2.imshow('img', img)
# cv2.imshow('mask', mask)
# cv2.imshow('dilation', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()