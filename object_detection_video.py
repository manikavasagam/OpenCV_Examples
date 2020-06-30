import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "Tracking", 255, 255, nothing)

while True:
    #frame = cv2.imread('media/smarties.png')
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower Hue", "Tracking")
    l_s = cv2.getTrackbarPos("Lower Saturation", "Tracking")
    l_v = cv2.getTrackbarPos("Lower Value", "Tracking")

    u_h = cv2.getTrackbarPos("Upper Hue", "Tracking")
    u_s = cv2.getTrackbarPos("Upper Saturation", "Tracking")
    u_v = cv2.getTrackbarPos("Upper Value", "Tracking")


    #lower and upper range of a color. here it is blue
    #l_b = np.array([110, 50, 50])
    #u_b = np.array([130, 255, 255])
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)
    if key == 27 :
        break

cap.release()
cv2.destroyAllWindows()