import cv2

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while(True):
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    height, width,_= frame.shape

    cx=int(width/2)
    cy=int(height/2)

    pixel_center_bgr=frame[cx,cy]
    b,g,r=int(pixel_center_bgr[0]),int(pixel_center_bgr[1]),int(pixel_center_bgr[2])
    pixel_center=hsv_frame[cx,cy]
    hue_value=pixel_center[0]

    color="Undefined"
    if hue_value<5:
        color="red"
    if hue_value<22:
        color="orange"
    if hue_value<33:
        color="yellow"
    if hue_value<78:
        color="green"
    if hue_value<131:
        color="blue"
    if hue_value<170:
        color="violet"
    else:
        color="red"

    cv2.rectangle(frame,(cx-220,10),(cx+200,120),(255,255,255),-1)
    cv2.putText(frame,color,(cx-200,100),0,3,(b,g,r),5)
    cv2.circle(frame,(cx,cy),5,(25,25,25),3)

    cv2.imshow("frame",frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
