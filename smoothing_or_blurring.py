import numpy as np
import cv2
from matplotlib import pyplot as plt

img=cv2.imread('s0001_02381_0_0_1_0_0_01.png')
img2=cv2.imread('salt.png')
avg=cv2.blur(img,(11,11))
gblur=cv2.GaussianBlur(img,(5,5),0)
median=cv2.medianBlur(img2,5) #perfect for salt and paper images
bilateral=cv2.bilateralFilter(img2,9,75,75)  #preserves the edges but not for improvement

titles=['img','img2','avg','gblur','median','bilateral']
images=[img,img2,avg,gblur,median,bilateral]

for i in range (6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()