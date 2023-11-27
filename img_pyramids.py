import cv2
import numpy as np

img = cv2.imread("lena.jpg")
layer = img.copy()
gaussian_pyramid_list = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)     
    gaussian_pyramid_list.append(layer)

layer = gaussian_pyramid_list[5]
cv2.imshow('upper level Gaussian Pyramid', layer)

laplacian_pyramid_list = [layer]

for i in range(5, 0, -1):
    # Resize the Gaussian pyramid layer to match the size of the original image
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    h, w, _ = gaussian_extended.shape
    layer = cv2.resize(gaussian_pyramid_list[i - 1], (w, h))
    
    # Compute the Laplacian by subtracting the resized Gaussian layer
    laplacian = cv2.subtract(layer, gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
