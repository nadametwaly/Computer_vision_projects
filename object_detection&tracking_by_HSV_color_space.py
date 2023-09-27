import cv2
import numpy as np

def nothing(x):
    print(x)

cv2.namedWindow("Tracking")
cv2.createTrackbar("lh", "Tracking", 0, 255, nothing)
cv2.createTrackbar("uh", "Tracking", 255, 255, nothing)

cv2.createTrackbar("ls", "Tracking", 0, 255, nothing)
cv2.createTrackbar("us", "Tracking", 255, 255, nothing)

cv2.createTrackbar("lv", "Tracking", 0, 255, nothing)
cv2.createTrackbar("uv", "Tracking", 255, 255, nothing)

while True:
    img = cv2.imread("./balls.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("lh", "Tracking")
    u_h = cv2.getTrackbarPos("uh", "Tracking")

    l_s = cv2.getTrackbarPos("ls", "Tracking")
    u_s = cv2.getTrackbarPos("us", "Tracking")

    l_v = cv2.getTrackbarPos("lv", "Tracking")
    u_v = cv2.getTrackbarPos("uv", "Tracking")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img, img, mask=mask)

    #l_b=np.array([110,50,50])
    #u_b=np.array([130,255,255])
    
    # Resize the displayed images (adjust the dimensions as needed)
    display_height, display_width = 480, 640  # Change these values as desired
    img = cv2.resize(img, (display_width, display_height))
    res = cv2.resize(res, (display_width, display_height))
    mask = cv2.resize(mask, (display_width, display_height))

    cv2.imshow("img", img)
    cv2.imshow("res", res)
    cv2.imshow("mask",mask)

    k = cv2.waitKey(1)
    if k == 27:
        break

cv2.destroyAllWindows()
