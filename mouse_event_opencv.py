import cv2
import numpy as np

def on_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 0, 0), 1)
        cv2.imshow("img", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ', ' + str(y)
        cv2.putText(img, text, (x,y), font, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow("img",img)



img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow("img", img)

cv2.setMouseCallback("img",on_click)

cv2.waitKey(0)
cv2.destroyAllWindows()
