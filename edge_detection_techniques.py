import numpy as np
import cv2
from matplotlib import pyplot as plt
img=cv2.imread('messi.webp',cv2.IMREAD_GRAYSCALE)

laplace=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
laplace=np.uint8(np.absolute(laplace))

sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0)
sobel_x=np.uint8(np.absolute(sobel_x))

sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1)
sobel_y=np.uint8(np.absolute(sobel_y))

sobel_xy=cv2.bitwise_or(sobel_x,sobel_y)

canny=cv2.Canny(img,100,200)

titles=['img','laplace','sobel_x','sobel_y','sobel_xy','canny']
images=[img,laplace,sobel_x,sobel_y,sobel_xy,canny]

for i in range (6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
