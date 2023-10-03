import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 255, 255, nothing)
cv2.createTrackbar("V", "frame", 255, 255, nothing)

hsv=np.zeros((250,500,3),np.uint8)

while True:
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")

    hsv[:]=(h, s, v)
    bgr=cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    #cv2.imshow("hsv", hsv)
    cv2.imshow("frame", bgr)

    # display_height, display_width = 480, 640  # Change these values as desired
    # hsv = cv2.resize(hsv, (display_width, display_height))
    # bgr = cv2.resize(bgr, (display_width, display_height))

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
